from flask import Flask, render_template,redirect,flash,url_for
from form import Prediction     # imports the Prediction class from the module form
from joblib import load 

app = Flask(__name__)


app.config['SECRET_KEY'] = 'a8c8a89d2426e119344e329c4968d867'  # to protect you app

@app.route('/', methods=['GET','POST'])      #this function routes to the desired page ( this routes to the home page )
def home():
    form = Prediction()   # this assigns a variable calleda forms to the class Prediction
    result = ''
    if form.validate_on_submit():# this handles the form
        data =[form.bedrooms.data,form.bathrooms.data,form.sqft_living.data,form.sqft_lot.data, form.floors.data,
         form.sqft_above.data,form.sqft_lot15.data,form.yr_built.data,form.condition.data,form.zipcode.data]                 # fetch the data
        model = load('model.joblib')   # loading the model
        result = model.predict([data])  # 
        result = result.str.strip('[]')
        flash('The price is $ '+ result)
        return redirect(url_for('home'))
    return render_template('home.html')   # this parses the data to the home form

# @app.route('/')
# def home():
#     return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

