from fbchat import Client
from fbchat.models import *
import codecs
import random
import time

def autsendfb():
    client = Client('0941946655', 'PhucMap1803')
    print("Own id: {}".format(client.uid))
    print('Ket noi auto thanh cong')
    noiDUng = tumoi()
    client.send(Message(text='30 PHUT 1 TU MOI ?? {}'.format(noiDUng)), thread_id=100000838467269, thread_type=ThreadType.USER)

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
while True:
    autsendfb()
    time.sleep(2700)
    pass
