from fbchat import Client
from fbchat.models import *
import codecs
import random
import time
from twilio.rest import Client
import requests
def autsendfb():
    client = Client('0941946655', '')
    print("Own id: {}".format(client.uid))
    print('Ket noi auto thanh cong')
    noiDUng = tumoi()
    client.send(Message(text='30 PHUT 1 TU MOI 😻 {}'.format(noiDUng)), thread_id=100000838467269, thread_type=ThreadType.USER)
    client.send(Message(text='Mình có nhận viết website dạo ai cần LH <3'), thread_id=100000838467269,thread_type=ThreadType.USER)

    client.logout()
def tumoi():
    with codecs.open("test.txt", "r", encoding='utf8') as f:
        list2 = []
        for item in f:
            number = 0
            while number < 1000:
                list2.append(item + str(number))
                number += 1
        return random.choice(list2)
# while True:
#     autsendfb()
#     time.sleep(2000)
#     pass



# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACe61d2fc75196206a584e69a52e260683'
auth_token = 'afca2dca05afdc7882823ddb85861e9b'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="window, /ˈwɪn.dəʊ/, (n.) cửa sổ;",
                     from_='+12512379485',
                     to='+84939091768'
                 )

print(message.sid)
