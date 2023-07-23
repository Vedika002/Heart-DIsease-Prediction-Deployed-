from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app=FastAPI()

class model_input(BaseModel):
    age:int
    sex:int
    cp:int
    trestbps:int
    chol:int    
    fbs:int
    restecg:int
    thalach:int
    exang:int
    oldpeak:int
    slope:int
    ca:int
    thal:int

# loading the saved model
heart_model=pickle.load(open('model.pkl','rb'))
@app.post('/heartdisease_prediction') #when someone has to give values to our api
def heartdis_pred(input_parameters:model_input):
    input_data=input_parameters.json()
    input_dictionary = json.loads(input_data)
    age=input_dictionary['age']
    sex=input_dictionary['sex']
    cp=input_dictionary['cp']
    trestbps=input_dictionary['trestbps']
    chol=input_dictionary['chol']
    fbs=input_dictionary['fbs']
    restecg=input_dictionary['restecg']
    thalach=input_dictionary['thalach']
    exang=input_dictionary['exang']
    oldpeak=input_dictionary['oldpeak']
    slope=input_dictionary['slope']
    ca=input_dictionary['ca']
    thal=input_dictionary['thal']

    input_list=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
    prediction=heart_model.predict([input_list])
    if prediction[0]==0:
        return 'The person does not have heart disease'
    else:
        return 'person has a heart disease'
    
