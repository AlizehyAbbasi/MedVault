# 🏥 MedVault — Flask + MySQL Starter

Minimal Flask web app with **Patients CRUD** using **SQLAlchemy** (MySQL via `PyMySQL`) and plain HTML/CSS.
You can extend this with **Visits** and **Prescriptions** later.

## ✨ Features
- List patients
- Create / Edit patient
- Delete patient
- Simple templates + CSS (no JS framework)

## 🧰 Stack
- Python 3.9+
- Flask 3.x
- SQLAlchemy
- MySQL (via `PyMySQL`)

## 🚀 Quick Start
1. **Create DB in MySQL**
   - Create a database named `medvault` (e.g., via phpMyAdmin or MySQL CLI).
2. **Configure environment**
   - Copy `.env.example` to `.env` and set your DB URL, e.g.:
     ```
     FLASK_ENV=development
     DATABASE_URL=mysql+pymysql://root:@127.0.0.1/medvault
     ```
3. **Create virtualenv & install deps**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. **Run the app**
   ```bash
   flask --app app run --debug
   ```
   Visit http://127.0.0.1:5000/

## 📁 Structure
```
MedVault-Flask-Starter/
├── app.py
├── models.py
├── config.py
├── requirements.txt
├── .env.example
├── README.md
├── templates/
│   ├── base.html
│   ├── patients_list.html
│   └── patient_form.html
└── static/
    └── styles.css
```

## 🧱 Next Steps
- Add `Visits` and `Prescriptions` models + forms
- Add search + pagination on list
- Add auth (Flask-Login) if you need multi-user access
