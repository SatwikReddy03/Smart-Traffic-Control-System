import random
import math
import datetime

def round_to_nearest_quarter_hour(dt):
    hour=dt.hour
    minute = dt.minute
    # Round the minutes to the nearest quarter hour
    if minute % 15 >= 7:
        minute += 15 - (minute % 15)
    else:
        minute -= minute % 15
    if minute==60:
        minute=0
        hour+=1
    return dt.replace(hour=hour,minute=minute, second=0, microsecond=0)

def get_time_date_day():
    # Get current date and time
    current_datetime = datetime.datetime.now()

    # Round the current time to the nearest quarter hour
    current_datetime = round_to_nearest_quarter_hour(current_datetime)

    # Extract time
    current_time = current_datetime.strftime("%I:%M:00 %p")  # 12-hour format with AM/PM

    # Extract date
    current_date = current_datetime.strftime("%d")  # Year-Month-Day format

    # Extract day
    current_day = current_datetime.strftime("%A")  # Full weekday name

    return current_time, current_date, current_day

import csv
def write_data_to_csv(data_list):
    # Write data to CSV file
    file_name = "traffic_data.csv"
    headers = ["Time", "Date", "Day of the week", "CarCount", "BikeCount", "BusCount", "TruckCount", "Total"]
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write headers
        writer.writerow(headers)
        
        # Write data rows
        writer.writerow(data_list)
    #print("CSV file created successfully.")

l=["12:00:00 AM",10,"Tuesday",31,0,4,4,39]
# Example data list
write_data_to_csv(l)

# Specify the headers


# Specify the file name


# Write data to CSV file
#write_data_to_csv(l, file_name)


def generate_vehicle_count(traffic_level,score):
    if "low" in traffic_level:
        return random.randint(10, 55)
    elif "medium" in traffic_level:
        return random.randint(55, 125)
    elif "high" in traffic_level:
        return random.randint(125, 235)




def divide_number_into_parts(number, ratios):
    # Calculate the sum of ratios
    total_ratio = sum(ratios)
    
    # Calculate the scaled values based on ratios
    scaled_values = [number * ratio / total_ratio for ratio in ratios]
    
    # Floor each scaled value
    floored_values = [math.floor(value) for value in scaled_values]
    
    return floored_values


def generate_instance(congestion_level, score):
    n=generate_vehicle_count(congestion_level,score)
    l=[12,2,4,1]
    a,b,c,d=divide_number_into_parts(n,l)
    b=int(b)
    d+=n-(a+b+c+d)
    e,f,g=get_time_date_day()
    return [e,f,g,a,b,c,d,n]

#print(generate_instance('low',0.75))