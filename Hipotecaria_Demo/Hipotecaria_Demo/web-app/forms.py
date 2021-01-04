from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import StringField, TextField, SubmitField, IntegerField,TextAreaField,RadioField,SelectField, DecimalField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import ValidationError

class PredictForm(FlaskForm):
   edad = IntegerField('Age:     ')
   estado_civil = StringField('Marital status:')
   ingreso_mensual = DecimalField('Monthly income:')
   anios_laboral = IntegerField('Years of work:')
   hijos = StringField('Children:  ')
   region = StringField('Region:  ')
   submit = SubmitField('PREDICT')
   abc = "" # this variable is used to send information back to the front page
