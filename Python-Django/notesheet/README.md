```py
# Install Django
pip install django

# Check Django version
django-admin --version

# Create a new Django project
django-admin startproject my_project

# Go inside project folder
cd my_project

# (Optional but recommended) Create app
python manage.py startapp mysite

# Run initial migrations (create default database tables)
python manage.py migrate

# Create migrations for your app models
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Run development server (default port 8000)
python manage.py runserver

# Run server on custom port
python manage.py runserver 8080

# Run server on custom IP + port (LAN access)
python manage.py runserver 0.0.0.0:8000

# Open in browser
http://127.0.0.1:8000/

# Create superuser (admin login)
python manage.py createsuperuser

# Access admin panel
http://127.0.0.1:8000/admin/
```
## Django Structure
```py
### Manually created directories
mkdir templates   # Store HTML files
mkdir static      # CSS, JS, images
mkdir media       # Upload files

# Optional extra folders (Best Practice)
mkdir static/css
mkdir static/js
mkdir static/images


myproject/
│
├── my_project/
│   ├── settings.py
│   ├── urls.py
│
├── myapp/
│   ├── views.py
│   ├── models.py
│
├── templates/
│   ├── index.html
│   ├── blog.html
│   ├── about-us.html
│   ├── contact.html
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│
├── media/
├── manage.py
```

## Static & Media Config
```py
# Static files URL
STATIC_URL = 'static/'

# Static files folder path
STATICFILES_DIRS = [BASE_DIR / 'static']

# Collect static (for production)
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files URL
MEDIA_URL = '/media/'

# Media folder path
MEDIA_ROOT = BASE_DIR / 'media'
```

## settings.py
```py
# Import Path (IMPORTANT)
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# Templates config
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Removed 'DIRS': [],
        'DIRS': [BASE_DIR / 'templates'],  # updated
        'APP_DIRS': True,
    },
]

## Debug mode (Development only)
DEBUG = True

# Allow all hosts (Dev only)
ALLOWED_HOSTS = ['*']

# ------------------------------------------
## Connect Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # custom apps
    'mysite',
]

## Optional App variable method
EXTERNAL_APPS = [
    'mysite'
]
INSTALLED_APPS = INSTALLED_APPS + EXTERNAL_APPS
# ------------------------------------------

## Database (Default SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

## Time & Language
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'

## Static files config
STATIC_URL = '/static/'
```
## urls.py (route)
```py
from django.contrib import admin
from django.urls import path
# import libs
from myapp.views import *

urlpatterns = [
    # Access AdminPanle
    path('admin/', admin.site.urls),
    # Access IndexPages
    path('', home, name="Home"),
]
```

## views.py (mysite/views.py)
```py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
   return render(request, "index.html")
```
