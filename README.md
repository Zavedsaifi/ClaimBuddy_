# ClaimBuddy – Patient Management System

This is a Django-based web application for managing basic patient information. It is developed as part of the assessment for the Associate Software Engineer role at ClaimBuddy Technologies.

---

## 🔧 Features

- Add, view, and manage patient records
- Uses Django models and views
- Integrated with the Stisla Admin Dashboard template
- Patient fields:
  - Full Name
  - Age
  - Gender
  - Insurance Provider
  - Policy Number

---

## 📁 Project Structure

patient_project/
├── pams/
│ ├── models.py
│ ├── views.py
│ └── templates/
│ └── pams/
│ └── patient_list.html
├── static/ # Contains Stisla CSS, JS
├── db.sqlite3
├── manage.py
└── README.md


---

## ▶ Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/Zavedsaifi/ClaimBuddy_.git
   cd ClaimBuddy

2. Create and activate a virtual environment:

    python -m venv venv
    venv\Scripts\activate

3. Install django:

    pip install django

4. Apply migrations:

    python manage.py migrate

5. Start the server:
    
    python manage.py runserver

Visit : http://127.0.0.1:8000/



