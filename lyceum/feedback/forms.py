from django import forms

from feedback.models import Author
from feedback.models import Feedback


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author

        fields = (Author.email.field.name,)
        labels = {Author.email.field.name: "Почта"}
        help_texts = {
            Author.email.field.name: "Введите адрес своей электронной почты"
        }
        widgets = {
            Author.email.field.name: forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "id": "floatingEmail",
                    "placeholder": Author.email.field.name,
                }
            )
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback

        fields = (Feedback.text.field.name,)

        labels = {Feedback.text.field.name: "Содержание"}
        help_texts = {Feedback.text.field.name: "Введите сообщение"}
        widgets = {
            Feedback.text.field.name: forms.Textarea(
                attrs={
                    "class": "form-control",
                    "id": "floatingText",
                    "placeholder": Feedback.text.field.name,
                    "style": "height: 20em",
                }
            )
        }
