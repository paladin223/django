import django.shortcuts


def description(request):
    template = ""
    context = {}
    return django.shortcuts(request, template, context)
