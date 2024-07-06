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