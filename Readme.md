# Employee Management System

A sleek and efficient web-based Employee Management System built with Django. It enables organizations to manage employee records, track employment details, and maintain data in an organized and intuitive manner.

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Django](https://img.shields.io/badge/Django-4.x-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Project-Active-blue)

---

## ✨ Key Features

- 🔍 View and filter employee directory
- 🧾 Add, update, and delete employee records
- 📧 Manage personal and professional details (name, role, contact, email, etc.)
- 📅 Track date of joining and tenure in the company
- 📦 Uses modern UI with Bootstrap 5 & icons
- 🔐 CSRF-protected forms with built-in Django validation

---

## 🖥️ Tech Stack

- **Backend Framework**: Django (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Database**: SQLite (default, can be switched to PostgreSQL/MySQL)
- **Templating**: Django Templates

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/django-employee-manager.git
cd django-employee-manager
```
2. **Create a Virtual Environment:**

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate  # On Mac/Linux
```

3. **Install Dependencies:**

```bash
pip install django mysqlclient
```

4. **Run Migrations:**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Start the Development Server:**

```bash
python manage.py runserver
```
