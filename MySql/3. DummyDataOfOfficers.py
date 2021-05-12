import mysql.connector as db

mydb=db.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='police_station'
)
print(mydb)

mycursor=mydb.cursor()

#Creating officers database
mycursor.execute("CREATE TABLE officers (Name VARCHAR(150),DOB VARCHAR(100),ID INTEGER(20),Gender VARCHAR(10),Address VARCHAR(255),Email VARCHAR(25),Mobile VARCHAR(15),No_of_cases INTEGER(20),PRIMARY KEY (ID))")
mycursor.execute("SHOW TABLES")
for i in mycursor:
    print(i)


sql_formula='INSERT INTO officers (Name,DOB,ID,Gender,Address,Email,Mobile,No_of_cases) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
person=[('Alex',"01/02/2001",1,"Male","Jaunpur","sinyash2000@gmail.com","8808988674",1),
        ('BOB',"02/02/2001",2,"Male","Rampur","sinyash2000@gmail.com","8808988674",0),
        ('David',"03/02/2001",3,"Male","Greater Noida","sinyash2000@gmail.com","8808988674",5),
        ('Zera',"03/02/2001",4,"Female","Noida","sinyash2000@gmail.com","8808988674",3)]
mycursor.executemany(sql_formula,person)
mydb.commit()