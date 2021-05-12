import mysql.connector as db

mydb=db.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='police_station'
)
print(mydb)

mycursor=mydb.cursor()

#mycursor.execute("CREATE TABLE FIR_register (Name VARCHAR(150),DOB VARCHAR(100),ID INTEGER(20),Gender VARCHAR(10),Address VARCHAR(255),Email VARCHAR(25),Mobile VARCHAR(15),No_of_cases INTEGER(20),PRIMARY KEY (ID))")
mycursor.execute("""
CREATE TABLE fir_Register (Sr_no MEDIUMINT NOT NULL AUTO_INCREMENT,Victim_Name VARCHAR(255),DOB VARCHAR(255),Adhaar_no VARCHAR(255),Gender VARCHAR(255),Address VARCHAR(255),Email VARCHAR(255),Mobile VARCHAR(255),
Registered_date_time DATETIME DEFAULT CURRENT_TIMESTAMP,Date_of_incident VARCHAR(255),Place_pf_incident VARCHAR(255),Description VARCHAR(255),Investigating_officer VARCHAR(255),Updates VARCHAR(255),Last_Update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,Profile LONGBLOB,PRIMARY KEY (Sr_no))
""")

mycursor.execute("SHOW TABLES")
for i in mycursor:
    print(i)
mydb.commit()