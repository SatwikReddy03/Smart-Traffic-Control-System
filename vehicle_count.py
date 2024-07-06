
import requests

url = r"https://ebb4f894-0fef-4b6c-8287-760a13b68146-00-1z3eo89k4pkjp.pike.replit.dev/predict"
data = {"data": [['5:45:00 PM', 27, 'Saturday', 147, 12, 5, 4, 168]]}  # Example input data

response = requests.post(url, json=data)
print(response)
prediction = response.json()["prediction"]
print(prediction)
category_values = {
    'low': 3,
    'normal': 6,
    'high': 10,
    'heavy':15
    }
print(category_values[prediction[0][0]])
