from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "your_secret_key"  # For flashing messages

db = SQLAlchemy(app)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    return redirect(url_for('view_records'))

@app.route('/add', methods=['GET', 'POST'])
def add_record():
    if request.method == 'POST':
        name = request.form['name']
        date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
        status = request.form['status']

        new_record = Attendance(name=name, date=date, status=status)
        db.session.add(new_record)
        db.session.commit()
        flash("Attendance record added successfully!", "success")
        return redirect(url_for('view_records'))
    return render_template('add.html')

@app.route('/view', methods=['GET', 'POST'])
def view_records():
    records = Attendance.query.all()

    # Search functionality
    if request.method == 'POST':
        search_name = request.form['search_name']
        date_filter = request.form['date_filter']

        if search_name:
            records = Attendance.query.filter(Attendance.name.contains(search_name)).all()
        elif date_filter:
            filter_date = datetime.strptime(date_filter, '%Y-%m-%d').date()
            records = Attendance.query.filter_by(date=filter_date).all()

    return render_template('view.html', records=records)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_record(id):
    record = Attendance.query.get_or_404(id)
    if request.method == 'POST':
        record.name = request.form['name']
        record.date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
        record.status = request.form['status']
        db.session.commit()
        flash("Record updated successfully!", "success")
        return redirect(url_for('view_records'))
    return render_template('edit.html', record=record)

@app.route('/delete/<int:id>')
def delete_record(id):
    record = Attendance.query.get_or_404(id)
    db.session.delete(record)
    db.session.commit()
    flash("Record deleted successfully!", "success")
    return redirect(url_for('view_records'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
