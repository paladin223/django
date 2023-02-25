import re

import django.core.exceptions


def text_validator(value):
    regex_r = r"\s*[Рр]оскошно[^a-z1-9A-Zа-яА-Я]*"
    regex_p = r"\s*[Пп]ревосходно[^a-z1-9A-Zа-яА-Я]*"
    if not (re.fullmatch(regex_r, rf"{value}")) and not (
        re.fullmatch(regex_p, rf"{value}")
    ):
        raise django.core.exceptions.ValidationError(
            "В тексте должно быть `роскошно` или `превосходно`"
        )
