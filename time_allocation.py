import math
import requests
def read_congestion_levels(filename):
    time_allocations = {}
    with open(filename, 'r') as file:
        for line in file:
            congestion_level, time_allocation = line.strip().split()
            time_allocations[congestion_level] = int(time_allocation)
    return time_allocations

def ml_time(l):
    url = r"https://ebb4f894-0fef-4b6c-8287-760a13b68146-00-1z3eo89k4pkjp.pike.replit.dev/predict"
    data = {"data": [l]}  

    response = requests.post(url, json=data)
    prediction = response.json()["prediction"]
    category_values = {
    'low': 3,
    'normal': 6,
    'high': 11,
    'heavy':15
    }
    return category_values[prediction[0][0]]



def allocate_time(congestion_level, score,instance):
    mlprediction_time=ml_time(instance)
    # Read congestion levels and their time allocations from file
    time_allocations = read_congestion_levels('congestion_levels.txt')
    congestion_level=congestion_level.split()[0]
    # Check if the provided congestion level is valid
    if congestion_level in time_allocations:
        time_allocation = time_allocations[congestion_level] * score
    else:
        print("Invalid congestion level provided.")
        return None

    return math.ceil(time_allocation+mlprediction_time)