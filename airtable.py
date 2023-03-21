import os
import requests
import json
import dotenv

dotenv.load_dotenv()

airtable_api_url = os.getenv('airtable_api_url')
airtable_api_key = os.getenv('airtable_api_key')

def save_to_airtable(records):
    # Define the headers for the request
    headers = {
        "Authorization": f"Bearer {airtable_api_key}",
        "Content-Type": "application/json"
    }

    print(airtable_api_key, ' ', airtable_api_url)
    response = requests.patch(airtable_api_url + '/lists', headers=headers, data=json.dumps({ 'records': records}))
    if response.status_code == 200:
        print("Record updated successfully")
    else:
        print("Error updating record: " + json.dumps(response.json()))
