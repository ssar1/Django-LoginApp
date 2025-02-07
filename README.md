# 🌟 Django Project Name

A Django-based web application for [describe purpose briefly]. 

![Django](https://img.shields.io/badge/Django-4.2-blue?style=flat&logo=django)  
![Python](https://img.shields.io/badge/Python-3.11-green?style=flat&logo=python)  
![Docker](https://img.shields.io/badge/Docker-20.10-blue?style=flat&logo=docker)

# Django Project - User Authentication

## 📌 Project Overview
This is a Django-based user authentication project that includes:
- User registration (Sign Up)
- User login & logout
- A home page with authentication checks
- Styled pages using CSS

## 🚀 Getting Started
Follow these steps to set up and run the project locally.

---

## 1️⃣ **Clone the Repository**
```sh
git clone <your-repo-url>
cd <your-project-folder>
```

---

## 2️⃣ **Set Up Virtual Environment**
Create and activate a virtual environment:

### 🔹 On macOS/Linux:
```sh
python3 -m venv myenv
source myenv/bin/activate
```

### 🔹 On Windows (CMD):
```sh
python -m venv myenv
myenv\Scripts\activate
```

---

## 3️⃣  🚀Run Database Migrations 
Ensure the database is updated:
```sh
python manage.py makemigrations
python manage.py migrate
```

---

## 4️⃣ **Create a Superuser (Optional for Admin Panel)**
```sh
python manage.py createsuperuser
```
Follow the prompts to set up an admin user.

---

## 5️⃣ **Run the Server Locally**
```sh
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## 6️⃣ **Checking SQLite Database**
By default, Django uses SQLite. Here’s how to check your database:

### 🔹 Open SQLite CLI
```sh
sqlite3 db.sqlite3
```

### 🔹 Show All Tables
```sql
.tables
```

### 🔹 Describe a Table
```sql
PRAGMA table_info(auth_user);
```

### 🔹 Query Data from `auth_user`
```sql
SELECT * FROM auth_user;
```

### 🔹 Exit SQLite
```sql
.exit
```

Alternatively, you can use **DB Browser for SQLite** to visually inspect the database.

---
---

## 🔹 **Available Routes**
| Route           | Description        |
|---------------|----------------|
| `/`           | Home Page |
| `/login/`     | User Login Page |
| `/signup/`    | User Signup Page |
| `/logout/`    | Logout Action |
| `/admin/`     | Django Admin Panel |

---

## 🎨 **Styling & Frontend**
- The CSS file is located at `app/static/app/style.css`.
- To modify styling, edit `style.css` and restart the server.

---

## 🛠 **Troubleshooting**
### ❌ Error: `ModuleNotFoundError: No module named 'app'`
**Solution:** Ensure the app is registered in `settings.py`:
```python
INSTALLED_APPS = [
    'app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### ❌ Error: `OperationalError: no such table: auth_user`
**Solution:** Run database migrations:
```sh
python manage.py migrate
```

### ❌ Error: Static files not loading
**Solution:** Ensure `{% load static %}` is included in your HTML files.

---

## 🚀  🚀 Run Database Migrations  🚀 🚀
 To add the age field to the CustomUser model, follow these migration steps:

- ✅  Modify the CustomUser model to include the age field
```sh
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)  # New field for age

```

- ✅Create migrations for the new field:
```sh
python manage.py makemigrations

```
✅ Apply the migrations to update the database:

```sh
python manage.py migrate
```

Let me know if you need any enhancements! 🚀

