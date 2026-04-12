# 📘 Django Template Connection Notes

## 🔹 Topic: Connecting Templates in Django

Connect multiple HTML files and reuse common components like header, footer, and navbar.

---

## ✅ Benefits

* Reusable code
* Clean structure
* Saves development time
* Easy maintenance

---

# 🔹 Types of Template Connection

## 1️⃣ `{% include %}` Method

👉 Used for small reusable parts

### 📌 Common Use Cases

* Footer
* Navbar
* Sidebar

### 💡 Explanation

Includes one template inside another template.
Works like dynamic copy-paste.

---

### 🧾 Example

#### Step 1: Create Footer File

📄 `templates/footer.html`

```html
<footer style="background:black; color:white; padding:10px; text-align:center;">
    <p>© 2026 My Website</p>
</footer>
```

---

#### Step 2: Use in index.html

📄 `templates/index.html`

```html
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

---

# 2️⃣ `{% extends %}` Method (Best Practice)

👉 Used for full layout system

### 📌 Common Use Cases

* Full website layout
* Large projects
* Consistent UI design

### 💡 Explanation

* Create a base template (parent)
* Other templates inherit it (child)
* Use `{% block %}` to insert content

---

### 🧾 Example

#### Step 1: Create Base Template

📄 `templates/base.html`

```html
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
<footer style="background:black; color:white; padding:10px; text-align:center;">
    <p>© 2026 My Website</p>
</footer>

</body>
</html>
```

---

#### Step 2: Use in index.html

📄 `templates/index.html`

```html
{% extends 'base.html' %}

{% block title %}Home Page{% endblock %}

{% block content %}
<h1>Welcome to Home Page</h1>
<p>This is main content</p>
{% endblock %}
```

---

# 🔥 Quick Comparison

| Feature       | `{% include %}`  | `{% extends %}`          |
| ------------- | ---------------- | ------------------------ |
| Use Case      | Small components | Full layout              |
| Structure     | Simple include   | Parent-child system      |
| Reusability   | Limited          | High                     |
| Best Practice | Partial reuse    | Recommended for projects |

---

# 🚀 Best Practice Tips

* Use `{% include %}` for reusable parts like footer/navbar
* Use `{% extends %}` for scalable and maintainable projects
* Always keep templates inside `templates/` folder

---

# 📌 Summary

* `{% include %}` → small reusable components
* `{% extends %}` → full layout inheritance system

---

💡 This approach helps build clean, scalable Django applications.
