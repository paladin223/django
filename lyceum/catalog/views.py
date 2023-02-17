from django.http import HttpResponse


def item_detail(request, pk):
    return HttpResponse(f"<body>Подробно элемент {pk}</body>")


def item_list(request):
    return HttpResponse("<body>Список элементов</body>")


def reg_value(request, value):
    return HttpResponse(f"<body>value int {value}</body>")


def re_path_value(request, pk):
    return HttpResponse(f"<body>re_path int {pk}</body>")
