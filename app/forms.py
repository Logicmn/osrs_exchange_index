from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

class SubmitForm(FlaskForm):
    input = StringField('Item search', validators=[InputRequired()])
