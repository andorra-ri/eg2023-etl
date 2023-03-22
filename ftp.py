import pysftp
import os
import dotenv
import pandas as pd

# Load env vars:
dotenv.load_dotenv()
sftp_host = os.getenv('hostname_sftp')
sftp_user = os.getenv('username_sftp')
sftp_password = os.getenv('password_sftp')
sftp_port = int(os.getenv('port_sftp'))

# Disable HostKeys for sftp connection:
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None


def load_file_from_ftp(dir, filenames):
    '''
    Connects to SFTP remote server, and downloads one or more xls files and reads them as dataframes
    Arguments:
        - 'dir'(string): path of the directory where the files are stored
        - 'filenames'(list): list of string, containing the name of the files to download
    Returns: 
        - 'found_files'(list): list of pandas dataframes
    Raises:
        Any exception raised by pysftp or pandas.read_excel() methods

    '''
    found_files = []
    with pysftp.Connection(sftp_host, username=sftp_user, password=sftp_password, port=sftp_port, cnopts=cnopts) as sftp:
        print('Connected to SFTP server')
        # Get the list of files in the folder
        folders = sftp.listdir()
        print(folders)

        for xls_file in filenames:
            file = sftp.open(dir + xls_file)
            df_file = pd.read_excel(file)
            found_files.append(df_file)
        
    # Close the SFTP connection
    sftp.close()
    print("Disconnected from SFTP server")

    return found_files 