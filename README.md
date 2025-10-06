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

## 🚀 Local Setup (Flask)
1. Create MySQL DB: `medvault`
2. Copy `.env.example` → `.env` and set:
   `DATABASE_URL=mysql+pymysql://root:@127.0.0.1/medvault`
3. `python -m venv .venv`  
   Windows: `.venv\Scripts\activate`  
   macOS/Linux: `source .venv/bin/activate`
4. `pip install -r requirements.txt`
5. `flask --app app run --debug` → open http://127.0.0.1:5000/


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
