import cv2
import face_recognition
import mysql.connector as db
import base64
import os

mydb=db.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='adhaar'
)
mycursor=mydb.cursor()
def adhaar(index):
        #index=1
        query = "SELECT * FROM adhaar WHERE Adhaar_no={}".format(index)
        mycursor.execute(query)
        result = mycursor.fetchone()
        n=mycursor.column_names

        return result[7]

def fingure(index):
    index=1
    data1=base64.b64decode(adhaar(index))
    with open("data.jpg", 'wb') as f:
        f.write(data1)


    img_data = face_recognition.load_image_file('data.jpg')
    os.remove("data.jpg")

    img_data = cv2.cvtColor(img_data,cv2.COLOR_BGR2RGB)
    imgtest = face_recognition.load_image_file('verification/gaurav.jpg')
    imgtest = cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)

    # faceLoc = face_recognition.face_locations(img_data)[0]
    encodeElon = face_recognition.face_encodings(img_data)[0]

    # faceLocTest = face_recognition.face_locations(imgtest)[0]
    encodetest = face_recognition.face_encodings(imgtest)[0]

    results = face_recognition.compare_faces([encodeElon],encodetest)
    # faceDis = face_recognition.face_distance([encodeElon],encodetest)

    if results[0]==True:
        return True
    else:
        return False

# print(fingure(1))
