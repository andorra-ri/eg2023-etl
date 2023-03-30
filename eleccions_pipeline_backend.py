'''
Description: Script to download files from a remote SFTP folder, read them as dataframes, to parse them finally as json files.
    Finally a patch request to airtable is done to update records into airtable.
'''

# Import dependencies
from ftp import load_file_from_ftp
from ftp_paramiko import load_file_from_sftp
from llistes_nacionals_parroquials import create_lists, blanks_nulls_count
from airtable import save_lists_to_airtable, save_results_to_airtable

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

for i in range(0, len(lists), batch_size):
    batch = lists[i:i+batch_size]
    print('Indexes: ' + str(i) + ':' + str(i+batch_size))
    save_lists_to_airtable(batch)

save_results_to_airtable(other_votes)