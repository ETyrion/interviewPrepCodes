import json
import requests

with open('sample_json.json') as file:
    emp_data = json.load(file)
    print(emp_data)
    total_employees = len(emp_data['emp_details'])
    #print(total_employees)
    for i in range(total_employees):
        first_name = emp_data['emp_details'][i]['first_name']
        print(first_name)
        if first_name == 'Noell':
            print(emp_data['emp_details'][i]['ip_address'])
