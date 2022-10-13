# stas27
Для запуска проекта необходимо установить язык программирования Python 3.7 и выше.
Затем в терминале прописать следующую команду -> pip install -r (путь к файлу....)/requirements.txt.
Необходимо установить PostgreSQL версии выше 13.
После установки PostgresSQL перейти в папку с файлом settings.py и поменять настройки 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '(НАЗВАНИЕ БД)',
        'USER': '(ИМЯ ПОЛЬЗОВАТЕЛЯ)',
        'PASSWORD': '(ПАРОЛЬ)',
        'HOST': '(ХОСТ)',
        'PORT': '(ПОРТ)',
    }
}
Далее перейти в папку с файлом manage.py, ввести в терминале следующие команды:
1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py runserver
