import smbclient

# Optional - specify the default credentials to use on the global config object
#smbclient.ClientConfig(username='serenissima\derema', password='tvlgalccllz3')

# Optional - register the credentials with a server (overrides ClientConfig for that server)


#smbclient.mkdir(r"\\172.31.1.103\c$\Temp\aa", username="serenissima\derema", password="tvlgalccllz3")

#with smbclient.open_file(r"\\server\share\directory\file.txt", mode="w") as fd:pip install smbprotocol
#    fd.write(u"file contents")


def smbCopy(suce,dest):
    try:
        smbclient.register_session("172.31.1.103", username="", password="")
        smbclient.copyfile(suce,dest)
    except Exception as e: 
        print(e)        
    
