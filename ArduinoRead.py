import serial
arduino = serial.Serial('com3', 9600)

while(True):
    a=arduino.readline()
    a = a[:-2].decode("utf-8")
    print(a)