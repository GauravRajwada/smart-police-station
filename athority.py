
from win10toast import ToastNotifier
import databse as db

def notify(sr):
    sr=12
    n = ToastNotifier()
    mess="Sr_no: {}".format(sr)
    n.show_toast("New Case", mess, duration = 10)

def show():
    sr=input("Enter the Sr_no of FIR: ")
    sr=1
    mes = db.fir(sr)
    message = ""
    for i in mes.keys():
            message += str(i) + ": " + str(mes[i]) + "\n\n\n"
    print(message)