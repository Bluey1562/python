from microbit import *

# INIT UART
uart.init(baudrate=115200, tx=pin16, rx=pin15)

def send(cmd, delay_ms=800):
    uart.write(cmd + "\r\n")
    sleep(delay_ms)

# TEST ESP
send("AT")

# CONNECT WIFI
send('AT+CWJAP="abc","12345678"', 5000)

def http_put(value):
    send('AT+CIPSTART="TCP","xxx.firebaseio.com",80', 2000)

    payload = str(value)
    http = (
        "PUT /temp.json HTTP/1.1\r\n"
        "Host: xxx.firebaseio.com\r\n"
        "Content-Length: {}\r\n\r\n{}"
    ).format(len(payload), payload)

    send('AT+CIPSEND={}'.format(len(http)), 1000)
    uart.write(http)
    sleep(2000)

while True:
    temp = temperature()
    http_put(temp)
    sleep(10000)
