from django.shortcuts import render
from django.http import HttpResponse

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
