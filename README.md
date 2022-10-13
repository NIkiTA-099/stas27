# stas27
Для запуска проекта необходимо установить язык программирования Python 3.7 и выше
Затем в терминале прописать следующую команду -> pip install -r (путь к файлу....)/requirements.txt
необходимо установить PostgreSQL версии выше 13
После установки PostgresSQL перейти в папку с файлом settings.py и поменять настройки 
DATABASES = {
    'default': {
        'ENGINE': environ.get('POSTGRES_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': environ.get('POSTGRES_DB', BASE_DIR / 'db.sqlite3'),
        'USER': environ.get('POSTGRES_USER', 'user'),
        'PASSWORD': environ.get('POSTGRES_PASSWORD', 'password'),
        'HOST': environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': environ.get('POSTGRES_PORT', '5432'),
    }
}
Далее перейти в папку с файлом manage.py, ввести в терминале следующие команды:
1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py runserver
