import databse as db
from New_Case import English

"""UserId="BOB123"
Password="1234"
db.userid(UserId,Password)"""

user=[('Alex123',"1234"),('BOB123',"1234"),('Zera123',"1234")]
English.welcome()
print("Please enter your USERID: ")
user=input()
print("Please enter your Password: ")
password=input()

while 1:
#    if (user,password) in user:
        print("Login Successfully")
        sr=input("Please enter the FIR sr_no: ")
        mes = db.fir(sr)
        message = ""
        for i in mes.keys():
            if i=="Profile":
                break
            message += str(i) + ": " + str(mes[i]) + "\n\n\n"
        print(message)
        update=input("Please give the update")
        db.fir_update(update,sr)
        mes = db.fir(sr)
        message = ""
        for i in mes.keys():
            if i=="Profile":
                break
            message += str(i) + ": " + str(mes[i]) + "\n\n\n"
        print("FIR Register Successfully updated.\nThank you")
        #print(message)
        break
#    else:
#        print("Invalid Input")

