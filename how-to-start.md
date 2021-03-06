## Virtual Environment for Django 
```bash
$ python3 -m pip install virtualenv
$ python3 -m venv djangoEnv #name
$ source djangoEnv/bin/activate # ($ deactivate) to quit
$ (djangoEnv) python3 -m pip install --upgrade pip
$ (djangoEnv) python3 -m pip install django~=2.1.0 #version
```

## Start Project
```bash
$ (djangoEnv) django-admin startproject hw2 . #name and location
```

## Start App
```bash
$ (djangoEnv) python manage.py startapp board #name

# hw2/settings.py
INSTALLED_APPS = [..., 'board.apps.BoardConfig',]
```

### Directory Structure
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
```python
# modify board/models.py
from django.db import models

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

# modify board/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```
```bash
$ (djangoEnv) python manage.py makemigrations
$ (djangoEnv) python manage.py migrate
```

## Update url
```python
# hw2/urls.py
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('board.urls')),
]

# create board/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
```

## Use Admin page
```bash
$ (djangoEnv) python manage.py createsuperuser
# go to localhost:8000/admin
```

## Create view
```python
# board/views.py
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'board/post_list.html', {'posts' : posts})
```
```html
{# create board/templates/board/post_list.html #}
{% for post in posts %} {# tag #}
    <div>
        <p>created: {{ post.created_at }}</p> {# variable #}
        <h1><a href="">{{ post.title }}</a></h1>
        <p>{{ post.content|linebreaksbr }}</p>
    </div>
{% endfor %}
```


## References
* [django girls](https://tutorial.djangogirls.org/ko/django_start_project/)
* [waffle seminar](https://waffle-skile.github.io/lecture/3/)
