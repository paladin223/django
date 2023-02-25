import django.core.exceptions


def text_validator(value):
    if not ("превосходно" in value) and not ("роскошно" in value):
        raise django.core.exceptions.ValidationError(
            "В тексте должно быть `роскошно` или `превосходно`"
        )
