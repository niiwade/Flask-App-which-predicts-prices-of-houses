from flask_wtf import FlaskForm   #the flaskform  is the class and the flask_wtf is the module
                                    # This is the base class
from wtforms import IntegerField,StringField,SubmitField, DecimalField
from wtforms.validators import DataRequired

class Prediction(FlaskForm):
    bedrooms = IntegerField('Number of Bedrooms', validators = [DataRequired()])
    bathrooms = IntegerField('Number of Bathrooms', validators = [DataRequired()])
    sqft_living = IntegerField('sqft_living', validators=[DataRequired()])
    sqft_lot = IntegerField('sqft_lot', validators=[DataRequired()])
    floors  = IntegerField('Floors', validators=[DataRequired()])
    sqft_above =  IntegerField('sqft_above', validators=[DataRequired()])
    sqft_lot15 = IntegerField('sqft_lot15', validators=[DataRequired()])
    yr_built =  IntegerField('yr_built',validators=[DataRequired()])
    condition = IntegerField('condition',  validators =[DataRequired()])
    zipcode = IntegerField('zipcode',validators= [DataRequired()])
    submit  = SubmitField('Predict')
