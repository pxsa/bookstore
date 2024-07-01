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
| python manage.py startapp `accounts` | create a new django app |

## start

First create a new django application by the following command:

`python3 manage.py start app accounts`

> [!IMPORTANT]
> Whenever you created a new app, you need to add it to the`settings.py` immediately.

There are two ways in order to add a new app to the project:

1. wrtie the name of the app

```
INSTALLED_APPS = [
    'django.contrib.admin',
    ...

    'accounts',
]
```

2. write the name of corresponding appConfig class

```
INSTALLED_APPS = [
    'django.contrib.admin',
    ...

    'accounts.app.AccountsConfig',
]
```


## Docker

### Dockerfile

### docker-compose

> docker-compose up

> docker-compose down
