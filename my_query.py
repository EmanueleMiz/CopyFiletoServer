import sqlite3

def connect():
    con = sqlite3.connect("ts_info.db")
    return(con)



#db = connect()
#cur = db.cursor()
#cur.execute("CREATE TABLE TEMP_(Hostname, IP, Farm)") #Create Table

#cur.execute(""" INSERT INTO IDC_TS VALUES ('TS13', '10.29.1.23', '2008'),('TS14', '10.29.1.24', '2008') """)

#db.commit()

#db.close()

def farm(f):
    db = connect()
    cur = db.cursor()
    q = "SELECT * FROM IDC_TS WHERE farm = '" +f+ "'"
    try:
        res = cur.execute(q)
    except Exception as e:
        print(e)
    data = res.fetchall()
    db.close()
    return(data)


def ints(hostname,ip,farm):
    db = connect()
    cur = db.cursor()
    q = " INSERT INTO IDC_TS VALUES ('"+hostname+"', '"+ip+"', '"+farm+"')"
    try:
        res = cur.execute(q)
        db.commit()
    except Exception as e:
        print(e)
    db.close