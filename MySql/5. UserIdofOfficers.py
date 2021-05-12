import mysql.connector as db

mydb=db.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='police_station'
)
print(mydb)

mycursor=mydb.cursor()

#Creating table for officers id & password
mycursor.execute("CREATE TABLE UserId (User VARCHAR(255), Password VARCHAR(255))")


sql_formula='INSERT INTO UserId (User,Password) VALUES(%s,%s)'
person=[('Alex123','1234'),
        ('BOB123',"1234"),
        ('David123',"1234"),
        ('Zera123',"1234")]
mycursor.executemany(sql_formula,person)


mydb.commit()