from my_query import farm, ints

class Ts:
    def __init__(self, hostname, ip, farm):
        self.hostname = hostname
        self.ip = ip
        self.farm = farm

def getTs(nfarm):
    data = farm(nfarm)
    ts_list = []
    for t in data :
        temp = Ts('','','')
        temp.hostname = t[0]
        temp.ip = t[1]
        temp.farm = t[2]
        ts_list.append(temp)
    #print(ts_list)
    #print(ts_list[0].ip)
    return(ts_list)

l = getTs('test')

for i in l:
    print(i.ip)
#ints('test2','172.31.1.103','test')
