import mysql.connector as db

mydb=db.connect(
    host='localhost',
    user='root',
    passwd='1234',
)
print(mydb)

mycursor=mydb.cursor()

#Creating Main police station database
mycursor.execute("CREATE DATABASE Police_Station")

#Creating dummy Adhaar Database
mycursor.execute("CREATE DATABASE adhaar")
