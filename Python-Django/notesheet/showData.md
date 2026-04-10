## Show Data in pages
### views.py 
```py
from django.shortcuts import render
from django.http import HttpResponse

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
```
# urls.py
```py
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
]

```
## html Page Code
```py
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Asset System</title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet">

<style>
body {
    background: linear-gradient(135deg,#0f172a,#1e293b);
    color:white;
}

/* Card */
.main-card {
    background:#1e293b;
    padding:20px;
    border-radius:15px;
    box-shadow:0 20px 40px rgba(0,0,0,0.5);
    animation:fadeIn 1s;
}

/* Table */
.table {
    background:#0f172a;
    color:white;
}

.table th {
    background:linear-gradient(45deg,#00f2fe,#4facfe);
    color:black;
}

.table tr:hover {
    transform:scale(1.02);
    transition:0.3s;
}

/* Buttons */
.btn-action:hover {
    transform:scale(1.2);
}

/* Animation */
@keyframes fadeIn {
    from {opacity:0; transform:translateY(30px);}
    to {opacity:1; transform:translateY(0);}
}
</style>

</head>
<body>

<div class="container mt-5">

<div class="main-card">

<h2 class="text-center mb-4">📊 Asset Management (Demo)</h2>

<table class="table table-bordered text-center align-middle">
<thead>
<tr>
<th>Name</th>
<th>Model</th>
<th>Serial</th>
<th>PO</th>
<th>Status</th>
<th>Device</th>
<th>Price</th>
<th>Discount</th>
<th>Action</th>
</tr>
</thead>

<tbody>
{% for asset in assetList %}
<tr>
<td>{{ asset.asset_name }}</td>
<td>{{ asset.model }}</td>
<td>{{ asset.serial_no }}</td>
<td>{{ asset.po_no }}</td>

<td>
<span class="badge bg-success">{{ asset.status }}</span>
</td>

<td>
<span class="badge bg-info">{{ asset.device_status }}</span>
</td>

<td>₹ {{ asset.price }}</td>
<td>{{ asset.discount }}%</td>

<td>
<button class="btn btn-info btn-sm btn-action">
<i class="fa fa-eye"></i>
</button>

<button class="btn btn-warning btn-sm btn-action">
<i class="fa fa-edit"></i>
</button>

<button class="btn btn-danger btn-sm btn-action">
<i class="fa fa-trash"></i>
</button>
</td>

</tr>
{% empty %}
<tr>
<td colspan="9">No Data Found</td>
</tr>
{% endfor %}
</tbody>

</table>

</div>
</div>

</body>
</html>
```