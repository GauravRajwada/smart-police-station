import mysql.connector as db
import base64
import io
import PIL.Image


mydb=db.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='adhaar'
)
print(mydb)

mycursor=mydb.cursor()

"""*************Creating table and inserting details of adhaar that have all details of adhaar card***********"""

#Function to load image
def load_file(text):
    with open(text, 'rb') as f:
        photo = f.read()

    encodestring = base64.b64encode(photo)
    return encodestring

#
mycursor.execute("CREATE TABLE adhaar (Name VARCHAR(150),DOB VARCHAR(100),Adhaar_no INTEGER(20),Gender VARCHAR(10),Address VARCHAR(255),Email VARCHAR(25),Mobile VARCHAR(15),PRIMARY KEY (Adhaar_no),Profile LONGBLOB)")
mycursor.execute("SHOW TABLES")
for i in mycursor:
    print(i)


sql_formula='INSERT INTO adhaar (Name,DOB,Adhaar_No,Gender,Address,Email,Mobile,Profile) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
person=[('Gaurav Singh',"01/02/2001",1,"Male","Jaunpur","sinyash2000@gmail.com","8808988674",load_file("Image/gaurav.jpg")),
        ('Fahad Khan',"02/02/2001",2,"Male","Rampur","sinyash2000@gmail.com","8808988674",load_file("Image/fahad.jpg")),
        ('Sneha Singh',"25/12/2005",3,"Female","Lucknow","sinyash2000@gmail.com","8808988674",load_file("Image/sneha.jpeg")),
        ('Pooja Singh',"15/08/1985",4,"Female","New Delhi","sinyash2000@gmail.com","8808988674",load_file("Image/pooja.jpg")),
        ('Tanu Singh',"03/06/2003",5,"Female","Varanasi","sinyash2000@gmail.com","8808988674",load_file("Image/tanu.jpeg")),]
mycursor.executemany(sql_formula,person)

mydb.commit()



"""Check weather data is inserted properly or not"""
sql1="select * from adhaar"
mycursor.execute(sql1)
data = mycursor.fetchall()
data1=base64.b64decode(data[0][7])
file=io.BytesIO(data1)
img=PIL.Image.open(file)
img.show()
db.close()


