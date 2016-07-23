__author__ = 'WelserJr'

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import Email


class EmailForm(Form):
    email = StringField(
        "Email",
        validators=[
            Email(message="Ingrese Email")
        ]
    )
