# Book Store

## Content

- [Todo](#todo)
- [Commands](#commands)
- [Dockerfile](#dockerfile)
- [docker-compose](#docker-compose)


## Todo

- [ ] create a new app for managing users
- [ ] create custom user model

## Commands

| command | job |
| --- | --- |
| python3 -m venv `venv` | create a virtual environment named `venv` | 
| django-admin startproject config . | make a new django project named `config` in the current directory | 
| python manage.py startapp `accounts` | create a new django app |

## start

First create a new django application by the following command:

`python3 manage.py startapp accounts`

> [!IMPORTANT]
> Whenever you created a new app, you need to add it to the`settings.py` immediately.

There are two ways in order to add a new app to the project:

1. wrtie the name of the app

``` python
INSTALLED_APPS = [
    'django.contrib.admin',
    ...

    'accounts',
]
```

2. write the name of corresponding appConfig class

``` python
INSTALLED_APPS = [
    'django.contrib.admin',
    ...

    'accounts.app.AccountsConfig',
]
```

#### Custom User

> [!WARNING]
> So far we didn't use `migrate` command, because if we do then django will automatically use its default user model.

Ok, so create a new user model in `models.py`.

``` python
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField()
```

In this code we've inherited from `AbstractUser` and added a new field named `age` to store user age.

But unfortunately django has no idea about our custom user model, and we need to notify and make django aware of our new model. So all we need is doing some changed in `settings.py`:

```
# settings.py

AUTH_USER_MODEL = 'accounts.CustomUser'
```

At this point, we are quite sure that django will use our `CustomUser` model instead of its own `User` model.

## Docker

### Dockerfile

### docker-compose

> docker-compose up

> docker-compose down
