from django.http import HttpResponse


def item_detail(request, pk):
    return HttpResponse("<body>Подробно элемент</body>")


def item_list(request):
    return HttpResponse("<body>Список элементов</body>")
