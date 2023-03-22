import re

import django.core.exceptions
from django.utils.deconstruct import deconstructible


@deconstructible
class Validator:
    def __init__(self, *arg):
        self.words = arg

    def __call__(self, value):
        for it in self.words:
            regex = rf"\s*{it[0]}{it[1:]}[^a-z1-9A-Zа-яА-Я]*"
            print(regex)
            if re.search(regex, rf"{value.lower()}"):
                return True
        raise django.core.exceptions.ValidationError(
            f"В тексте должно быть одно из {self.words}"
        )


def text_validator(value):
    regex_r = r"\s*[Рр]оскошно[^a-z1-9A-Zа-яА-Я]*"
    regex_p = r"\s*[Пп]ревосходно[^a-z1-9A-Zа-яА-Я]*"
    if not (re.fullmatch(regex_r, rf"{value}")) and not (
        re.fullmatch(regex_p, rf"{value}")
    ):
        raise django.core.exceptions.ValidationError(
            "В тексте должно быть `роскошно` или `превосходно`"
        )
