from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
app.config['SECRET_KEY'] = 'mysecretkey'

db = SQLAlchemy(app)

# Database Model for Attendance Log
class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"<Attendance {self.name} on {self.date}>"

# Create the database
with app.app_context():
    db.create_all()

# Form for submitting attendance
class AttendanceForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    status = StringField('Status (Present/Absent)', validators=[DataRequired()])
    submit = SubmitField('Submit Attendance')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = AttendanceForm()
    if form.validate_on_submit():
        new_attendance = Attendance(name=form.name.data, date=form.date.data, status=form.status.data)
        db.session.add(new_attendance)
        db.session.commit()
        return redirect(url_for('index'))

    records = Attendance.query.all()
    return render_template('index.html', form=form, records=records)

@app.route('/filter', methods=['GET', 'POST'])
def filter_records():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        filtered_records = Attendance.query.filter(Attendance.date >= start_date, Attendance.date <= end_date).all()
        return render_template('filter.html', records=filtered_records)

    return render_template('filter.html', records=[])

if __name__ == '__main__':
    app.run(debug=True)


