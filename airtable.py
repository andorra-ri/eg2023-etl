import os
import requests
import json
import dotenv

# Load env vars:
dotenv.load_dotenv()
airtable_api_url = os.getenv('airtable_api_url')
airtable_api_key = os.getenv('airtable_api_key')

def save_lists_to_airtable(records):
    '''
    Description: Updates records in Airtable from dictionaries, parsed as json file
    Arguments:
        - 'records'(list): list of dictionaries with the records to be updated
    '''
    # Define the headers for the request
    headers = {
        "Authorization": f"Bearer {airtable_api_key}",
        "Content-Type": "application/json"
    }

    response = requests.patch(airtable_api_url + '/lists', headers=headers, data=json.dumps({'records': records}))
    if response.status_code == 200:
        print("Records updated successfully")
    else:
        print("\033[91m Error updating record: " + json.dumps(response.json()) + '\033[0m')

def save_results_to_airtable(records):
    '''
    Description: Updates records in Airtable from dictionaries, parsed as json file
    Arguments:
        - 'records'(list): list of dictionaries with the records to be updated
    '''
    headers = {
        "Authorization": f"Bearer {airtable_api_key}",
        "Content-Type": "application/json"
    }

    print("To save: " + json.dumps({'records': records}))
    response = requests.patch(airtable_api_url + '/results', headers=headers, data=json.dumps({'records': records}))
    if response.status_code == 200:
        print("Record updated successfully")
    else:
        print("\033[91m Error updating record: " + json.dumps(response.json()) + '\033[0m')