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
On = tkinter.Button(tk, text="ON", width=15, height=5, command=lambda: py_serial.write(b'1'))
On.pack()
Off = tkinter.Button(tk, text="OFF", width=15, height=5, command=lambda: py_serial.write(b'0'))
Off.pack()
tk.mainloop()