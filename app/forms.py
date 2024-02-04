from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class CourseSelectionForm(FlaskForm):
    course = SelectField('Select Course', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Enroll')

class ClockInForm(FlaskForm):
    submit = SubmitField('Clock In')
