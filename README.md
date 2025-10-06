# 🏥 MedVault – Smart Medical History & Prescription Tracker

**Type:** Academic Project  
**Role:** Lead Designer, Frontend Developer & Documentation Owner  
**Timeline:** May-July 2025  
**Tech Stack:** HTML • CSS • Python (Flask) • MySQL

---

## 🧩 Overview
MedVault is a responsive web-based interface designed to simplify how small clinics and patients organize medical histories and prescriptions. The project focuses on creating a clean, accessible, and intuitive digital record-keeping experience, turning traditional medical files into a modern, user-friendly dashboard.

---

## 🚀 Features
- Interactive homepage and navigation layout
- Patient record creation, editing, and deletion  
- Prescription tracking linked to each patient  
- Searchable database for easy access  
- Fully responsive and visually consistent design  
- Organized record sections for quick access
- Simple, modern UI with healthcare-inspired color palette
  
---

## ⚙️ Architecture / Design Snapshot
A three-layer architecture:
1. **HTML:** Defines the content and structure of the interface
2. **CSS:** Adds visual styling, layout responsiveness, and color schemes
3. **Backend:** MySQL database with tables for patients, prescriptions, and visits  

---

## 🚀 Local Setup (Flask)
1. Create MySQL DB: `medvault`
2. Copy `.env.example` → `.env` and set:
   `DATABASE_URL=mysql+pymysql://root:@127.0.0.1/medvault`
3. Create a virtual environment and activate it:
   - Windows: `python -m venv .venv` then `.venv\Scripts\activate`
   - macOS or Linux: `python -m venv .venv` then `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the app: `flask --app app run --debug`  
   Open http://127.0.0.1:5000/

---
## 🧠 What I Learned
- Database normalization and ER design  
- Writing reusable code and structured documentation
- Creating consistent color themes and typography
- Designing user-focused healthcare dashboards 
- Translating user needs into technical features  

---

## 🖼️ Screenshots
(Add screenshots once you have them — drag into `screenshots/` folder and commit again.)

---

## 📘 Case Study
Read the full reflection → [MedVault Case Study](../CaseStudies/MedVault_CaseStudy.md)
