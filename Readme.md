Getting Started

To play around with your own Django template custom tags and filters, you’re going to need a Django project. You’ll build dinosoar, a small website with all sorts of dinosaur info. Although the name implies that you’ll only include flying dinos, that’s just for marketing spin. All your favorite heavyweights will be there as well.
If you’ve never set up a Django project before or if you need a refresher, you may want to read Get Started With Django Part 1: Build a Portfolio App first.
Django is a third-party library, so it should be installed in a virtual environment. If you’re new to virtual environments, check out Python Virtual Environments: A Primer. Create and activate a new virtual environment for yourself and then run the following commands:

```
 $ python -m pip install django==3.2.5
 $ django-admin startproject dinosoar
 $ cd dinosoar
 $ python manage.py startapp dinofacts .
 $ python manage.py migrate
```

Setting Up a Django Project

You need to make some changes to your project’s settings to make Django aware of your newly created app and to configure your templates. Edit dinosoar/dinosoar/settings.py and add dinofacts to the INSTALLED_APPS list:

```
# dinosoar/dinosoar/settings.py

INSTALLED_APPS = [

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "dinofacts",
]

```
Within the same file, you’ll need to update the DIR value in the TEMPLATES attribute. This tells Django where to look for your template files:

```
# dinosoar/dinosoar/settings.py

TEMPLATES = [

    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },

```