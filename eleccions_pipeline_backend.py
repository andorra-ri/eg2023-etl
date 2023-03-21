# Import dependencies
import requests
import dotenv
import pandas as pd

from ftp import load_file_from_ftp
from llistes_nacionals_parroquials import create_lists
from airtable import save_to_airtable
#---------------------------------------------------------------------------------

# Import env vars:
dotenv.load_dotenv()

    #airtable related env vars:
# airtable_api_url = os.getenv('airtable_api_url')
# airtable_api_key = os.getenv('airtable_api_key')


#---------------------------------------------------------------------------------
files = load_file_from_ftp('/rtva/', ['Escrutini_Parroquial.xls'])
# file = './Escrutini_Parroquial.xls'
df = files[0]
lists = create_lists(df)

print(lists)

save_to_airtable(lists[:10])

#TESTING!!
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
    #In case we have a second file containing participation stats, we want to retrieve the blanks and nulls:
#bdf_blanks_nulls = pd.read_excel(sftp.open(remote_file_2))
#Appropiate treatment:

