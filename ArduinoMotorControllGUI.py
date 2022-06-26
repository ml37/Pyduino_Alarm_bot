from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import serial
import time
import tkinter

form_class = uic.loadUiType('Controller.ui')[0]
py_serial = serial.Serial(
    
    # Window
    port='COM3',
    
    # 보드 레이트 (통신 속도)
    baudrate=9600,
)
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Btn_0.clicked.connect(self.Btn_0_clicked)
        self.Btn_90.clicked.connect(self.Btn_90_clicked)
        self.Btn_180.clicked.connect(self.Btn_180_clicked)
        self.HS.sliderMoved.connect(self.HS_sliderMoved)

    def Btn_0_clicked(self):
        py_serial.write(b'a')
        print("0")
    def Btn_90_clicked(self):
        py_serial.write(b'b')
        print("90")
    def Btn_180_clicked(self):
        py_serial.write(b'c')
        print("180")
    def HS_sliderMoved(self):
        py_serial.write(bytes(self.HS.value()))
        print(self.HS.value())

app = QApplication(sys.argv)
screen = MyWindow()
screen.show()
sys.exit(app.exec_())