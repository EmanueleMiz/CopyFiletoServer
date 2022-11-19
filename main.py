#import shutil, filecmp, urllib
#from my_query import *
from smb.SMBHandler import SMBHandler
from smb.SMBConnection import SMBConnection
#from read_file import *
#from write_file import *
#from ts import *
#from my_smb import *
#from smb_test import *
from smb import smb_structs
smb_structs.SUPPORT_SMB2 = True

PHAT = "aprova.txt"
#
#p = "011"
my_name = ''


conn = SMBConnection(my_name, '', 'a','a','a')
conn.connect('172.31.1.103', port=445, timeout=60)
#file2transfer = open(filename,"r")
#conn.storeFile('\\',path + filename, file2transfer, timeout=30 )



f = input("Su che farm vuoi copiare i file : ")
inprotel = input("Dove si trova il Protel.ini da copiare : ")
outprotel = input("Dove deve essere posizionato : ")






tslist = getTs(f)

host1 ="\\"+"\\172.31.1.103"+inprotel

bar = "\\"
bar2 = "\\"

for t in tslist : 
    p = bar + bar + "" + t.ip +"\\"+ outprotel
    print(p)
    smbCopy(p,host1)


#with opener.open('smb://172.31.1.115/Public/protel.ini') as file:
#    for line_number, line in enumerate (file, start=1):
#        if word in line:
#            print(f"Word '{word}' found on line {line_number}")
#            print(line)
#            i = i + 1
        
#    if i == 0 :
#        print("Il site non corrisponde")

#surce = './temp/1/test.txt'

#dest = './temp/2'

#shutil.copy2(surce,dest)