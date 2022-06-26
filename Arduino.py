import serial
import time
import tkinter

arduino = serial.Serial('com3', 9600)
time.sleep(1)

tk = tkinter.Tk()
tk.title("Arduino")

on = tkinter.Button(tk, text="ON", width=15, height=5, command=lambda: arduino.write(b'1'))
on.pack()
off = tkinter.Button(tk, text="OFF", width=15, height=5, command=lambda: arduino.write(b'0'))
off.pack()
tk.mainloop()