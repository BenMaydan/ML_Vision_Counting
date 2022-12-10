from serial import *
import sys
import glob
import serial


if __name__ == '__main__':
    from serial.tools import list_ports
    port = list(list_ports.comports())
    for p in port:
        print(p.device)


    # configure the serial connections (the parameters differs on the device you are connecting to)
    ser = serial.Serial(
        port='/dev/cu.usbmodem13401',
        baudrate=115200,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.EIGHTBITS
    )

    while True:
        ser.write(bytearray([1,1,0,0,0,0,0,1]))
        # ser.flush()
