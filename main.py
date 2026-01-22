from microbit import *
import utime

uart.init(baudrate=115200, tx=pin16, rx=pin15)

def send(cmd, t=800):
    uart.write(cmd + "\r\n")
    sleep(t)

send("AT")
send('AT+CWJAP="abc","12345678"', 5000)

while True:
    temp = temperature()
    http_put(temp)
    utime.sleep(10)
