import json
import requests
url='http://127.0.0.1:8000/heartdisease_prediction'

input_data_for_model= {

    'age':22,
    'sex':1,
    'cp':0,
    'trestbps':100,
    'chol':131,    
    'fbs':83.7,
    'restecg':1,
    'thalach':191,
    'exang':0,
    'oldpeak':1.5,
    'slope':0,
    'ca':0,
    'thal':2,
}
input_json=json.dumps(input_data_for_model)
response=requests.post(url, data=input_json)
print(response.text)