from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import URL, DataRequired

class InputForm(FlaskForm):
    url_input = StringField("URL", validators=[URL(), DataRequired()])
    submit = SubmitField("Shorten")