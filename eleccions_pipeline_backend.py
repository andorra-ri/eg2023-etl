'''
Description: Script to download files from a remote SFTP folder, read them as dataframes, to parse them finally as json files.
    Finally a patch request to airtable is done to update records into airtable.
'''

# Import dependencies
from ftp import load_file_from_ftp
from ftp_paramiko import load_file_from_sftp
from llistes_nacionals_parroquials import create_lists, blanks_nulls_count
from airtable import save_to_airtable, save_to_airtable_2

# Define script parameters:
remote_path = '/rtva/'
files = ['Escrutini_Parroquial.xls', 'Detall_Escrutini_Parroquial.xls'] 

files = load_file_from_sftp(remote_path, files)
df = files[0]
df_2 = files[1]
lists = create_lists(df)
other_votes = blanks_nulls_count(df_2)

batch_size = 9
length_lists = len(lists)
for i in range(length_lists):
    batch = lists[i:i+batch_size]
    save_to_airtable(batch)

save_to_airtable_2(other_votes)
