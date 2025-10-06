from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Patient
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route("/")
    def home():
        return redirect(url_for("patients_list"))

    @app.route("/patients")
    def patients_list():
        q = request.args.get("q", "").strip()
        query = Patient.query
        if q:
            like = f"%{q}%"
            query = query.filter((Patient.first_name.ilike(like)) | (Patient.last_name.ilike(like)) | (Patient.email.ilike(like)))
        patients = query.order_by(Patient.created_at.desc()).all()
        return render_template("patients_list.html", patients=patients, q=q)

    @app.route("/patients/new")
    def patients_new():
        return render_template("patient_form.html", patient=None)

    @app.route("/patients/<int:pid>/edit")
    def patients_edit(pid):
        patient = Patient.query.get_or_404(pid)
        return render_template("patient_form.html", patient=patient)

    @app.route("/patients/save", methods=["POST"])
    def patients_save():
        pid = request.form.get("id")
        first = request.form.get("first_name", "").strip()
        last = request.form.get("last_name", "").strip()
        dob = request.form.get("date_of_birth") or None
        phone = request.form.get("phone", "").strip()
        email = request.form.get("email", "").strip()

        if not first or not last:
            flash("First name and Last name are required.", "error")
            return redirect(request.referrer or url_for("patients_list"))

        if pid:
            patient = Patient.query.get_or_404(int(pid))
            patient.first_name = first
            patient.last_name = last
            patient.date_of_birth = datetime.strptime(dob, "%Y-%m-%d").date() if dob else None
            patient.phone = phone
            patient.email = email
        else:
            patient = Patient(
                first_name=first,
                last_name=last,
                date_of_birth=datetime.strptime(dob, "%Y-%m-%d").date() if dob else None,
                phone=phone,
                email=email
            )
            db.session.add(patient)

        db.session.commit()
        flash("Saved successfully.", "ok")
        return redirect(url_for("patients_list"))

    @app.route("/patients/<int:pid>/delete", methods=["POST"])
    def patients_delete(pid):
        patient = Patient.query.get_or_404(pid)
        db.session.delete(patient)
        db.session.commit()
        flash("Deleted.", "ok")
        return redirect(url_for("patients_list"))

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
