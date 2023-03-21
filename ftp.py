import pysftp
import os
import dotenv
import pandas as pd

dotenv.load_dotenv()

sftp_host = os.getenv('hostname_sftp')
sftp_user = os.getenv('username_sftp')
sftp_password = os.getenv('password_sftp')
sftp_port = int(os.getenv('port_sftp'))

#cnopts = pysftp.CnOpts(knownhosts='known_hosts')
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

def load_file_from_ftp(dir, filenames):
    found_files = []

    with pysftp.Connection(sftp_host, username=sftp_user, password=sftp_password, port=sftp_port, cnopts=cnopts) as sftp:
        #transport = paramiko.Transport((sftp_host, sftp_port))
        #sftp = paramiko.SFTPClient.from_transport(transport)
        print('Connected to SFTP server')

        # Navigate to the remote folder
        #sftp.chdir(dir)
        #print('Changed remote directory to ftp')

        # Get the list of files in the folder
        folders = sftp.listdir()
        print(folders)

        #for file in files:
            #if file in filenames:
                #found_files.append(sftp.open(file))
        file = sftp.open(dir + filenames[0])
        df_file = pd.read_excel(file)
        found_files.append(df_file)
        # Filter the list to only XLS files
        # xls_files = [file for file in remote_files if file.endswith('.xls')]
        
    # Close the SFTP connection
    sftp.close()
    print("Disconnected from SFTP server")

    return found_files
    #return sftp.open(xls_files[0])
 