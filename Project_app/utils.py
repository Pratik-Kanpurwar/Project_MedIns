import pickle
import os
print(os.getcwd())
import json
import pandas as pd
import numpy as np
import traceback
import sys
import config
import warnings
warnings.filterwarnings('ignore')

class MedicalInsurance():
    def __init__(self,age,sex,bmi,children,smoker,region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = 'region_'+region
        
    def load_model(self):
        try:
            # print("loading model")

            with open(config.MODEL_FILE_PATH,'rb') as f:
                self.model = pickle.load(f)
                
            # print("model loaded")
            print(config.JSON_FILE_PATH)
                
            with open(config.JSON_FILE_PATH,'r') as f:
                self.project_data = json.load(f)
                
            # print('dict loaded')
            
        except:
            print(sys.exc_info())
                
            
    def get_predicted_charges(self):
        try:
        
            self.load_model()
            
            test_array = np.zeros(len(self.project_data['columns']))

            index = self.project_data['columns'].index(self.region)
            
            test_array[0] = self.age
            test_array[1] = self.project_data['sex'][self.sex]
            test_array[2] = self.bmi
            test_array[3] = self.children
            test_array[4] = self.project_data['smoker'][self.smoker]
            test_array[index] = 1
            
            prediction = self.model.predict([test_array])
            charges = np.round(prediction[0],2)
            
            # return f"predicted charges are {charges}"
            return charges
            
        except:
            print(traceback.print_exc())
        
                
if __name__ == "__main__":             
    age = eval(input("give an age: "))
    sex = 'male'
    bmi = 27.9
    children = 2
    smoker = 'yes'
    region = 'northeast'

    med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
    print(med_ins.get_predicted_charges())
        