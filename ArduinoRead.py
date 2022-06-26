import serial
import time
import tkinter

tk = tkinter.Tk()
tk.title("Arduino")
tk.geometry("300x300")

py_serial = serial.Serial(
    
    # Window
    port='COM3',
    
    # 보드 레이트 (통신 속도)
    baudrate=9600,
)
while True:
    print(py_serial.readline())