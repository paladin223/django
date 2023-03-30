# django

[![Django tests](https://github.com/paladin223/django/actions/workflows/django.yml/badge.svg)](https://github.com/paladin223/django/actions/workflows/django.yml)
[![Python Linting](https://github.com/paladin223/django/actions/workflows/python-package.yml/badge.svg)](https://github.com/paladin223/django/actions/workflows/python-package.yml)

# Описание
Создание первого приложения на джанго и CI/CD

# Технологии
Python 3.10 Django 3.2.16

# Запуск проекта dev-режиме
Для начала в `git bash` пропишите `git clone https://github.com/paladin223/django`, что бы создать папку проекта.

С помощью команды `cd /d путь к директории проекта` осуществите переход к папке проекта.

Для того чтобы создать виртуальное окружение (`venv`) пропишите `python -m venv venv`

Затем активируйте `venv` командой `source venv/*/activate`, где `*` у `Windows`: `scripts`, а у `linux/osx`: `bin`

Установите зависимости  `pip install -r *`, где `*` - файл. `requirements_dev` - для разаботки, `requirements_lint` - линтинг, `requirements_test` - тестирование

Создайте файл `.env` с помощью команды `cp example.env .env`. Если у вас есть доп. настройки для конфгурации проекта, то в файле `.env` измените соответствующие парметры, в противном случе изменять параметры не стоит.

Заполните базу данных командой `python3 lyceum/manage.py loaddata data.json`

Для запуска сервера выполните команду `python3 lyceum/manage.py runserver` для запуска сервера. 

Затем вернитесь в корневую папку проекта используя команду `cd ..`.

Логин/пароль для `/admin/` user/user

Cоздать админ пользователя командой `python manage.py createsuperuser `

## Полезные команды (исполнять из корня проекта)

| Задача | Команды |
| :---: | :--- |
| Создание фикстуры | <code>python -Xutf8 ./lyceum/manage.py dumpdata -e contenttypes -e auth.Permission -e thumbnail.kvstore -e sessions.session --indent 2 -o data.json |
| Подгрузка фикстуры | <code>python ./lyceum/manage.py makemigrations</code></br><code>python ./lyceum/manage.py migrate --run-syncdb</code></br><code>python ./lyceum/manage.py loaddata "data.json"</code>
| тестовый админ admin - admin |