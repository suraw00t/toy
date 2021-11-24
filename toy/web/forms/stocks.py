from flask_wtf import FlaskForm
# from flask_wtf.recaptcha import validators
from wtforms import fields, validators

class ItemForm(FlaskForm):
    name = fields.StringField(
        validators=[validators.InputRequired()]
    )
    description = fields.StringField()
    weight = fields.FloatField(default = 0)

class ItemStatusForm(FlaskForm):
    buyer = fields.StringField(
        validators=[validators.InputRequired()]
    )
    seller = fields.StringField(
        validators=[validators.InputRequired()]
    )
    item = fields.StringField(
        validators=[validators.InputRequired()]
    )
    