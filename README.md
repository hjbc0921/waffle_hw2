## Virtual Environment for Django 
```bash
python3 -m pip install virtualenv
python3 -m venv djangoEnv #name
source djangoEnv/bin/activate
(djangoEnv) python3 -m pip install --upgrade pip
(djangoEnv) python3 -m pip install django~=2.1.0 #version
```

## Start Project
```bash
django-admin startproject hw2 . #name and location
```

## Start App
```bash
(djangoEnv) python manage.py startapp board #name

# hw2/settings.py
INSTALLED_APPS = [..., 'board',]
```

```
waffle_hw2
├─── README.md
├─── hw2
|       __init__.py
|       settings.py
|       urls.py
|       wsgi.py
├── manage.py
└── board
    ├── migrations
    |       __init__.py
    ├── __init__.py
    ├── admin.py
    ├── models.py
    ├── tests.py
    └── views.py
```

## Migration
```bash
(djangoEnv) python manage.py makemigrations board
(djangoEnv) python manage.py migrate board
```

## References
* [django girls](https://tutorial.djangogirls.org/ko/django_start_project/)
* [waffle seminar](https://waffle-skile.github.io/lecture/3/)
