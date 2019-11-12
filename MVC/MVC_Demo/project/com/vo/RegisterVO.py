from wtforms import *


class RegisterVO:
    id = IntegerField
    firstname = StringField
    lastname = StringField
    username=StringField
	password=StringField