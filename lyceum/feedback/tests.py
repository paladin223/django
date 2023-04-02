import shutil
import tempfile

from django.core import management
from django.core.files.base import ContentFile
from django.test import Client
from django.test import override_settings
from django.test import TestCase
from django.urls import reverse

from feedback.forms import AuthorForm
from feedback.forms import FeedbackForm
from feedback.models import Author
from feedback.models import Feedback

MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class ContextTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.author_form = AuthorForm()
        cls.feedback_form = FeedbackForm()
        cls.author = {"email": "example@example.ru"}
        cls.feedback = {"text": "Example text"}
        cls.data = cls.author | cls.feedback

    @classmethod
    def tearDown(cls):
        management.call_command("flush", verbosity=0, interactive=False)
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)

    def test_context_in_form(self):
        response = Client().get(reverse("feedback:feedback"))
        self.assertIn(
            "author_form",
            response.context,
            "В контесте обратной связи отсутствует форма автора",
        )
        self.assertIn(
            "feedback_form",
            response.context,
            "В контесте обратной связи отсутствует форма сообщения",
        )
        self.assertEqual(
            response.status_code,
            200,
            f"Страница обратной связи "
            f"возвращает неверный статус {response.status_code}",
        )

    def test_form_labels(self):
        self.assertEquals(
            self.author_form[Author.email.field.name].label,
            "Почта",
            "Заголовок поля почты имеет неверное значение",
        )
        self.assertEquals(
            self.feedback_form[Feedback.text.field.name].label,
            "Содержание",
            "Заголовок поля содержания сообщения имеет неверное значение",
        )

    def test_form_help_text(self):
        self.assertEquals(
            self.author_form.fields[Author.email.field.name].help_text,
            "Введите адрес своей электронной почты",
            "Подсказка поля почты имеет неверное значение",
        )
        self.assertEquals(
            self.feedback_form.fields[Feedback.text.field.name].help_text,
            "Введите сообщение",
            "Подсказка поля содержания сообщения имеет неверное значение",
        )

    def test_form_redirect(self):
        response = Client().post(
            reverse("feedback:feedback"), data=self.data, follow=True
        )
        self.assertRedirects(response, reverse("feedback:feedback"))

    def test_message_saves_to_db(self):
        response = Client().post(
            reverse("feedback:feedback"), data=self.data, follow=True
        )
        self.assertEqual(
            response.status_code,
            200,
            f"Страница обратной связи "
            f"возвращает неверный статус {response.status_code}",
        )

    def test_file_upload(self):
        file = ContentFile(b"Example file", name="File name")
        response = Client().post(
            reverse("feedback:feedback"),
            data=self.data | {"file": file},
            follow=True,
        )
        self.assertEqual(
            response.status_code,
            200,
            f"Страница обратной связи "
            f"возвращает неверный статус {response.status_code}",
        )