from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
   return render(request, "index.html")

# testing env
def test(request):
    assetList = [
        {
            'id': 1,
            'asset_name': 'Laptop',
            'model': 'Dell i5',
            'serial_no': 'SN12345',
            'po_no': 'PO001',
            'status': 'Available',
            'device_status': 'In Warranty',
            'price': 50000,
            'discount': 10
        },
        {
            'id': 2,
            'asset_name': 'Desktop',
            'model': 'HP i7',
            'serial_no': 'SN67890',
            'po_no': 'PO002',
            'status': 'Used',
            'device_status': 'Out Warranty',
            'price': 40000,
            'discount': 5
        },
        {
            'id': 3,
            'asset_name': 'Printer',
            'model': 'Canon X',
            'serial_no': 'SN99999',
            'po_no': 'PO003',
            'status': 'Faulty',
            'device_status': 'Out Warranty',
            'price': 15000,
            'discount': 2
        }
    ]
    return render(request, 'test.html', {'assetList': assetList})


# 🟢 Registration View
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create user
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

        User.objects.create_user(username=username, email=email, password=password)

        return redirect('login')  # after register go to login

    return render(request, 'register.html')


# 🔵 Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # create session
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

 # 🔴 Logout Function
# 🔒 Protect Home Page
@login_required(login_url='login')  # if not login → redirect to login page
def home(request):
    return render(request, 'home.html')

# 🟡 Home Page
def home(request):
    return render(request, 'home.html')