# Приложение "Застрахуй братуху"

<b>Команды Docker'а</b><br>
<b>Собрать новый образ и запустить два контейнера:</b><br>
`docker-compose up -d --build`<br><br>
<b>Запустить миграцию:</b><br>
`docker-compose exec web python manage.py migrate`<br><br>
<b>Создать администратора:</b><br>
`docker-compose exec web python manage.py createsuperuser`<br><br>
<b>Все бд пользователя postgres:</b><br>
`docker-compose exec db psql —username=postgres`<br><br>

<b>Команды Elasticsearch</b><br>
<b>Создание индексов:</b><br>
`docker-compose exec web python manage.py search_index --rebuild`<br><br>

<b>Команды Celery</b><br>
Необходимо ввести в `settings.py` пароль и логин электронной почты