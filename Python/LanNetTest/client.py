# -*- coding:utf-8 -*-
import socket
import sys
from ctypes import c_char

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from multiprocessing import Process, Queue, Value

import time
import ts

def speed_test(q, val):
    HOST = '192.168.31.210'#'127.0.0.1'
    PORT = 1234
    speed = int(0)
    SendData = (c_char * 8192*8)()
    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    num = int(0)
    t = time.time()
    stop = t
    while True:
        client.send(SendData)
        num = num + 1
        if time.time() - t >=1:
            t = time.time()
            if q.value == 0:
                q.value = num
            num = 0
        if val.value == 1 :
            break

    client.close()
        #print(client.recv(1024).decode('utf-8'))

class wid(QtWidgets.QWidget):
    def  __init__(self):
        super().__init__()
        self.ui = ts.Ui_st()
        self.ui.setupUi(self)
        self.flag = False
        self.speed = Value('I' , 0)
        self.val = Value('I' , 0)
        self.s = 0
        self.pro = Process(target=speed_test, args=(self.speed,self.val,))
        self.timer = 0
        

    @pyqtSlot()
    def on_pushButton_clicked(self):
        if self.flag == False:
            #speed_test(self.speed,self.val)
            print('Child process will start.')
            self.ui.pushButton.setText('关闭')
            self.pro.start()
            self.timer = self.startTimer(100)
            self.flag = True
        else:
            self.flag == False
            print('Child process will stop.')
            self.val.value = 1
            time.sleep(1)
            self.pro.close()
            self.ui.pushButton.setText('启动')
            self.killTimer(self.timer)


    def timerEvent(self,event):
        temp = self.speed.value
        self.speed.value = 0
        if temp != 0:
           self.s = temp*8*8/1024
        self.ui.label.setText('{:.2f}Mb/s'.format(self.s))
        #self.timer = self.startTimer(100)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wid = wid()
    wid.show()
    sys.exit(app.exec_())
