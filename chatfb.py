from coinphucmap import configPhuc
from fbchat import Client
from fbchat.models import *
# khai bao dang nhap
def msg():
    Clients = Client(configPhuc.faceBook, configPhuc.passFace)
    print('Id fb cua ban la {}'.format(Clients.uid))
    print('KET NOI THANH CONG')
    noiDung = input("VUI LONG NHAP NOI DUNG MUON NHAN > :")
    Clients.send(Message(text=noiDung), thread_id=100028593181497, thread_type=ThreadType.USER)
    Clients.logout()
    print('DANG THOAT FB')
while True:
    msg()
    pass
