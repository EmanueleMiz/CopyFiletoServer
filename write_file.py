import tempfile
from smb.SMBConnection import SMBConnection

def copia():
    connection = SMBConnection(username='admin',password='Serenissima1-',my_name='admin',remote_name='',domain='',use_ntlm_v2=True)
    connection.connect(ip='172.31.1.115')
    with open('./Prova.txt', 'rb', buffering=0) as file_obj:
    #file = open('./prova.txt', 'r')
        connection.storeFile('Public','admin/',file_obj)
    connection.close()

    return('yes')


