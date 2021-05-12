from twilio.rest import Client
import databse as d

def send_message(sr=d.recent_case()):
 
    mes = d.fir(sr)
#    print(mes)    
    message = ""
    for i in mes.keys():
        if i=="Profile":
            break
        message += str(i) + ": " + str(mes[i]) + "\n\n"

    print(message)


    account_sid = 'AC52df8e1e86559d288247f858c410c64d' 
    auth_token = '725bdfc2e1616f209bd7c106c4f2a481' 
    client = Client(account_sid, auth_token) 
     
    message = client.messages.create( 
                                  from_='whatsapp:+14155238886',  
                                  body=message,      
                                  to='whatsapp:+918808988674' 
                              ) 
     
    print(message.sid)    
    
    
