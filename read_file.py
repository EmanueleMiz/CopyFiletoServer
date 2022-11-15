import urllib
from smb.SMBHandler import SMBHandler

def controllo_file(p):
    opener = urllib.request.build_opener(SMBHandler)
    fh = opener.open('smb://172.31.1.115/Public/protel.ini')
    data = fh.read()
    fh.close()
    file = str(data)

    f = file.find("protel"+p)
    if f > 1 :
        result = "Il Site Corrisponde"
    else:
        result = "Phat Seleziona in maniera errata (Il site non corrisponde)"
    return result


