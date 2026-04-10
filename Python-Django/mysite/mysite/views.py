# manual import lib
from django.http import HttpResponse
# https render
from django.shortcuts import render


# home page & render index.html
def home(request):
    return render(request, 'index.html')

# create functions
def blog(request):
    return render(request, 'blog.html')

# contact-us
def contact(request):
    return render(request,'contact.html')

# aboutus
def about(request):
    return render(request, "about-us.html")

# register
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Save Data
        RegisterUser.objects.create(
            username=username,
            email=email,
            password=password
        )

        return redirect('register')  # reload page after submit

    return render(request, "register.html")

# login
def login(request):
    return render(request, "login.html")
