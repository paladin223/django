from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
import django.views

from feedback.forms import AuthorForm
from feedback.forms import FeedbackForm
from lyceum import settings


class FeedbackView(django.views.View):
    template = "feedback/feedback.html"
    author_form_class = AuthorForm
    feedback_form_class = FeedbackForm

    def get(self, request):
        author_form = self.author_form_class()
        feedback_form = self.feedback_form_class()

        context = {
            "author_form": author_form,
            "feedback_form": feedback_form,
        }
        return render(request, self.template, context=context)

    def post(self, request):
        author_form = self.author_form_class(request.POST)
        feedback_form = self.feedback_form_class(request.POST)

        if all(
            [
                author_form.is_valid(),
                feedback_form.is_valid(),
            ]
        ):
            email = author_form.cleaned_data["email"]
            text = feedback_form.cleaned_data["text"]
            send_mail(
                f"Feedback from {email}",
                text,
                email,
                [settings.FEEDBACK_EMAIL],
            )
            messages.success(request, "Сообщение успешно отправлено")
            return redirect(reverse("feedback:feedback"))

        context = {
            "author_form": author_form,
            "feedback_form": feedback_form,
        }
        return render(request, self.template, context=context)
