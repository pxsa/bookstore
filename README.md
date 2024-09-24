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

But unfortunately django has no idea about our custom user model, and we need to notify and make django aware of our new model. So all we need to do is doing one tiny change in `settings.py`:

``` python
# settings.py
AUTH_USER_MODEL = 'accounts.CustomUser'
```

At this point, we are quite sure that django will use our `CustomUser` model instead of its own `User` model.

#### Custom User Form

As we have a new user model, we need to think about its consequences and make corresponding changes in order to have an appropriate signup form and extend them.

``` python
# forms.py

from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age', )

```
So whenever a user wanted to signup we can use our custom model.

> [!IMPORTANT]
> `Django` has no idea about this custom form, so we need to make it aware of our new form class.

``` python
# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
```

By registering the `CustomUserAdmin` then we're sure about the user creation form(`signup` form).

> [!NOTE]
> Now it's time to use `makemigrations` and then `migrate` our models.

If you're in your virtual env then:
> python3 manage.py makemigrations accounts

But if you're using docker then:
> sudo docker-compose exec web python3 manage.py makemigrations accounts

At this point you can creat a super user as well.

## Docker

### Dockerfile

### docker-compose

> docker-compose up

> docker-compose down
