from wtforms import Form, TextField, validators, BooleanField


class RegistrationForm(Form):
    name = TextField('Name:', [validators.Length(min=1, max=255), validators.required()])
    surname = TextField('Surname:', [validators.Length(min=1, max=255), validators.required()])
    email = TextField('Email:', [validators.email(), validators.Length(min=1, max=255), validators.required()])
    country = TextField('Country:', [validators.Length(min=1, max=255), validators.required()])
    city = TextField('City:', [validators.Length(min=1, max=255), validators.required()])
    refFriend = BooleanField('Friend')
    refGoogle = BooleanField('Google+')
    refFacebook = BooleanField('Facebook')
    refTwitter = BooleanField('Twitter')
    refSearch = BooleanField('Search Engine')
    refOther = BooleanField('Other')
    refOtherText = TextField('OtherText')