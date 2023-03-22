'''
Description: Script to download files from a remote SFTP folder, read them as dataframes, to parse them finally as json files.
    Finally a patch request to airtable is done to update records into airtable.
'''

# Import dependencies
from ftp import load_file_from_ftp
from llistes_nacionals_parroquials import create_lists
from airtable import save_to_airtable

# Define script parameters:
remote_path = '/rtva/'
files = ['Escrutini_Parroquial.xls'] 

files = load_file_from_ftp(remote_path, files)
df = files[0]
lists = create_lists(df); print(lists)

save_to_airtable(lists[:10])
save_to_airtable(lists[11:21])
save_to_airtable(lists[22:26])
#TESTING!!
    #In case we have a second file containing participation stats, we want to retrieve the blanks and nulls:
#bdf_blanks_nulls = pd.read_excel(sftp.open(remote_file_2))
#Appropiate treatment:


#2. Reformat code: generalize second file + upload records and upload other pending records
#3. Push to CloudFunction and scheduler