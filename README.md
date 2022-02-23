# Приложение "Застрахуй братуху"

<b>Запуск тестов</b><br>
<b>Юнит-тесты:</b><br>
`docker-compose exec web python manage.py test .`<br><br>
<b>Запуск `pylint`:</b><br>
<b>Запуск для приложения `accounts`</b><br>
`docker-compose exec web pylint accounts`<br><br>
<b>Запуск для приложения `main`</b><br>
`docker-compose exec web pylint main`<br><br>

<b>Команды Docker'а</b><br>
<b>Собрать новый образ и запустить два контейнера:</b><br>
`docker-compose up -d --build`<br><br>
<b>Запустить миграцию:</b><br>
`docker-compose exec web python manage.py migrate`<br><br>
<b>Создать администратора:</b><br>
`docker-compose exec web python manage.py createsuperuser`<br><br>
<b>Создание новой бд в postgres:</b><br>
`psql -Upostgres`<br><br>
`create database insure_brother;`<br><br>
<b>Удалить тома и контейнеры</b><br>
`docker-compose down -v`<br><br>

<b>Команды Elasticsearch</b><br>
<b>Создание индексов:</b><br>
`docker-compose exec web python manage.py search_index --rebuild`<br><br>

<b>Команды Celery</b><br>
Необходимо внести в `settings.py` пароль и логин электронной почты