from fbchat import Client
# from coinphucmap import configPhuc
from fbchat.models import *
def autsendfb():
    client = Client('ledanghongphuc@gmail.com', 'PhucMap')
    print("Own id: {}".format(client.uid))
    print('Ket noi auto thanh cong')
    noiDUng = input('BAN CAN GUI TIN NHAN GI >>> :')
    client.send(Message(text=str(noiDUng)), thread_id=client.uid, thread_type=ThreadType.USER)
    client.logout()
while True:
    autsendfb()
    pass
