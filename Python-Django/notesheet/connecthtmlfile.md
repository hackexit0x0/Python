## 📘 Django Template Connection Notes
> Connect multiple HTML files in Django\
> Reuse same footer / navbar / header in all pages
> Save time + clean code
### 🔹 Method 1: {% include %}
> 👉 Used for small reusable parts\
> 📌 Example Use:\
> Footer\
> Navbar\
> Sidebar\

### 🧾 Step 1: Create Footer File
> 📄 templates/footer.html
```py
<footer style="background:black; color:white; padding:10px; text-align:center;">
    <p>© 2026 My Website</p>
</footer>
```

### 🧾 Step 2: Use in index.html
> 📄 templates/index.html
```py
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>

<h1>Welcome to Home Page</h1>

{% include 'footer.html' %}

</body>
</html>
```

## 🔹 Method 2: {% extends %}
> 👉 Used for full layout system (Best Practice)\
> 🧾 Step 1: Create Base Template\
> 📄 templates/base.html
```py
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>

<!-- Navbar -->
<h2>My Navbar</h2>

<!-- Main Content -->
{% block content %}
{% endblock %}

<!-- Footer -->
<footer style="background:black; color:white; color:white;">
    <p>© 2026 My Website</p>
</footer>

</body>
</html>
```

### 🧾 Step 2: Use in index.html
> 📄 templates/index.html
```py
{% extends 'base.html' %}

{% block title %}Home Page{% endblock %}

{% block content %}
<h1>Welcome to Home Page</h1>
<p>This is main content</p>
{% endblock %}
```