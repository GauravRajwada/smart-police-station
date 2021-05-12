import mysql.connector as db
#import face_verify as f
import base64
#import io
#import PIL.Image
#import cv2
mydb1=db.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='adhaar'
)
mycursor1=mydb1.cursor()

mydb=db.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='police_station'
)
mycursor=mydb.cursor()

def adhaar(index):
        #index=1
        query = "SELECT * FROM adhaar WHERE Adhaar_no={}".format(index)
        mycursor1.execute(query)
        result = mycursor1.fetchone()
        n=mycursor1.column_names

        return {i: j for i, j in zip(n, result[0:7])}


def load_file(text):
    with open(text, 'rb') as f:
        photo = f.read()

    encodestring = base64.b64encode(photo)
    return encodestring


def fir_register(detail):
#    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in detail.keys())
#    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in detail.values())
#    sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('FIR_Register', columns, values)
#    mycursor.execute(sql)
#    mydb.commit()
    l = []
    for i in detail.keys():
        l.append(detail[i])
    k = (l)
    l = []
    l.append(k)

    sql = 'INSERT INTO fir_register (DOB,Adhaar_No,Gender,Address,Email,Mobile,Profile,Date_of_incident,Place_pf_incident,Description,Victim_Name,Investigating_officer) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    mycursor.executemany(sql, l)
    mydb.commit()


def min_case_off():
    query="""select * from officers where No_of_cases=(select min(No_of_cases) from officers)"""
    mycursor.execute(query)
    value = mycursor.fetchone()
    key = mycursor.column_names
    result=""
    for i in range(len(key)):
        if key[i] not in ['DOB','Address','Email','No_of_cases']:
            result+=str(key[i])+"-"+str(value[i])+" "


    return result

def fir_update(update,sr):
    sr=str(sr)
    cur=mydb.cursor()
    a='\'{}\''.format(update)
    cur.execute("select Updates from fir_register where Sr_no={}".format(sr))
    if cur.fetchone()==(None,):
        """UPDATE fir_register SET Description= {} WHERE Sr_no = {}"""
        query="UPDATE fir_register SET Updates= {} WHERE Sr_no = {}".format(a, sr)
        cur.execute(query)
        mydb.commit()
    else:
        query = """update fir_register set Updates=CONCAT(Updates, {}) where Sr_no = {};""".format(a, sr)
        mycursor.execute(query)
        mydb.commit()

def fir(sr):
    query = "SELECT * FROM fir_register WHERE Sr_no={}".format(sr)
    mycursor.execute(query)
    result = mycursor.fetchone()
    n = mycursor.column_names
    return {i: j for i, j in zip(n, result)}

def userid(UserId,Password):
    #UserId="BOB123"
    #Password="1234"
    try:
        query = "SELECT User,Password FROM userid"
        mycursor.execute(query)
        result = mycursor.fetchall()
        if (UserId,Password) in result:
            return "Login Successfully"
        else:
            return "Invalid Input"
    except :
        return "Some Problen"
        """return "Invalid UserId or Password"""

def recent_case():
    query = """select Sr_no from fir_register where Sr_no=(select max(Sr_no) from fir_register)"""
    mycursor.execute(query)
    value = mycursor.fetchone()
    return value[0]


