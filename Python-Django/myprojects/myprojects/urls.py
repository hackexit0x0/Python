from django.contrib import admin
from django.urls import path
# import lib form myapp
from myapp.views import *

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # index
    path('', home, name="Home"),

    path("test/", test, name="test"),

    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('home/', home, name='home'),
]
    