from flask import Flask, jsonify, Response, render_template, request
import pandas as pd
import numpy as np
import sys
from Project_app.utils import MedicalInsurance

app = Flask(__name__)

################################################################
#######################-BASE API-###############################
################################################################

@app.route('/')
def hello_flask():
    print('Welcome to Project Mediacal Insurance Prediction')
    return render_template('index.html')

################################################################
#######################-PREDICTION API-#########################
################################################################

@app.route('/predict_charges',methods=['GET','POST'])
def get_insurance_charges():
    
    if request.method == 'POST':
    
        data = request.form
        
        age = eval(data['age'])
        sex = data['sex']
        bmi = eval(data['bmi'])
        children = eval(data['children'])
        smoker = data['smoker']
        region = data['region']
        
        med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
        charges = med_ins.get_predicted_charges()
        
        return render_template('index.html',prediction=charges)
    
    else:
        
        data = request.args
        
        age = eval(data['age'])
        sex = data['sex']
        bmi = eval(data['bmi'])
        children = eval(data['children'])
        smoker = data['smoker']
        region = data['region']
        
        med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
        charges = med_ins.get_predicted_charges()
        
        return render_template('index.html',prediction=charges)
        

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5005,debug=True)

