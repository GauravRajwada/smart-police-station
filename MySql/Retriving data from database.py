import mysql.connector as db

mydb=db.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='adhaar'
)
print(mydb)
mycursor=mydb.cursor()

mycursor.execute("SHOW TABLES")
for i in mycursor:
    print(i)

mycursor.execute("SELECT * FROM adhaar1")

result=mycursor.fetchall()
for i in result:
    print(i)

#Retrive data from specific adhaar number
mycursor.execute("SELECT * FROM adhaar1 WHERE Adhaar_no=1")
result=mycursor.fetchone()
print(result)