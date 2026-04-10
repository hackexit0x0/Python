## Django Installation
### Install Django
```py
# Install Django
pip install django

# Create a new Django project
django-admin startproject my_project

# Go inside project folder
cd my_project

# (Optional but recommended) Create app
python manage.py startapp mysite

# Run initial migrations (create default database tables)
# Migration = process of updating database schema
python manage.py migrate

# Create migrations for your app models
python manage.py makemigrations

# Run development server (default port 8000)
python manage.py runserver

# Run server on custom port
python manage.py runserver 8080

# Open in browser
http://127.0.0.1:8000/

# Create superuser (admin login)
python manage.py createsuperuser

# Example:
# Username: admin
# Email: admin@gmail.com
# Password: 123 (not recommended, weak password)
# Django will warn but you can bypass (y/N)

# Access admin panel
http://127.0.0.1:8000/admin/
```
## Django Structure
```py
### Manually created directories
mkdir templates   # Store HTML files (web pages / UI templates)
mkdir static      # Store static assets like CSS, JS, fonts, images
mkdir media       # Store uploaded files (images, videos, user files)

### Config (add in settings.py)

# Tell Django where template files are located IF RENDERING
 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
       #  'DIRS': [], OLD
        'DIRS': [BASE_DIR / 'templates'], # New Config
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Static files URL (used in browser)
STATIC_URL = 'static/'

# Static files folder path
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files URL
MEDIA_URL = '/media/'

# Media folder path
MEDIA_ROOT = BASE_DIR / 'media'
```
### settings.py
```py
from pathlib import Path

# Project base folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key (keep private)
SECRET_KEY = 'your-secret-key'

# Debug mode (True = development)
DEBUG = True

# Allowed domains
ALLOWED_HOSTS = []

# Installed apps (add your app here)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    'mysite',  # your app
]

# Main URL file
ROOT_URLCONF = 'mysite.urls'

# Database (default SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Language & time zone
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

# Static files (CSS, JS)
STATIC_URL = 'static/'
```
### urls.py (route)
```py
# Example URL slugs (how users access pages in browser)
# http://mysite.com/          -> Home page
# http://mysite.com/blogs     -> Blog page
# http://mysite.com/about-us  -> About page

# Import Django admin panel
from django.contrib import admin   

# Import 'path' to define URL routes
from django.urls import path

# Import views file from 'mysite' app/project
from mysite import views

# List of URL patterns (routes)
urlpatterns = [
    # Admin panel route (custom URL instead of default 'admin/')
    path('admin-cpl/', admin.site.urls),
    # Route for blog page
    # When user visits http://mysite.com/blog/
    # It will call the 'blog' function from views.py
    path('blog/', views.blog),
      # access blog page
    path('blog/',views.blog),
    # about
    path('about/',views.about),
    # contact
    path('contact/',views.contact)
]
```
### views.py (manual create mysite/views.py)
```py
# Import HttpResponse class from Django to send text response
from django.http import HttpResponse
# Web html page rendering
# home page & render index.html
def home(request):
    return render(request, 'index.html')

# create functions
def blog(request):
    return render(request, 'blog.html')

# contact-us
def contact(request):
    return render(request, 'contact.html')

# aboutus
def about(request):
    return render(request, "about-us.html")


```