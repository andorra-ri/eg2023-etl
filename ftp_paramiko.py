import paramiko
import os
import io
import base64
import dotenv
import pandas as pd

# Import env vars:
dotenv.load_dotenv()
sftp_host = os.getenv('hostname_sftp')
sftp_user = os.getenv('username_sftp')
sftp_password = os.getenv('password_sftp')
sftp_port = int(os.getenv('port_sftp'))
hostkey = os.getenv('key')


def load_file_from_sftp(dir, filenames):
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

    # Establish connection:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=sftp_host, username=sftp_user, password=sftp_password)        
    print('Connected to SFTP server')

    sftp = ssh.open_sftp()


    for xls_file in filenames:
        file = sftp.open(dir + xls_file)
        df_file = pd.read_excel(file)
        found_files.append(df_file)

    ssh.close()
    print("Disconnected from SFTP server")

    return found_files