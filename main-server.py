
from machine import Pin, PWM
import socket
import math
import utime
import network
import time
import network_cred
 
ip = ""

# create wifi connection 
def connect_to_internet(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print("Waiting for connection")
        time.sleep(1)
    if wlan.status() != 3:
        raise RuntimeError("network connection failed")
    else:
        ip = wlan.ifconfig()[0]
        print('IP: ', ip)
        status = wlan.ifconfig()

def set_pwm_rgb(pwm_color, pwm_value):
    # pwm value is in percent, so we have to calculte a new value
    pwm_value = pwm_value + int(pwm_value *(65535 /100))
    pwm_color.duty_u16(pwm_value)
    return 

# define outputs (GPIO pin numbers, not physical pin numbers) and values
pwm_red = PWM(Pin(26))
pwm_red.freq(1000)   
pwm_green = PWM(Pin(27))
pwm_green.freq(1000) 
pwm_blue = PWM(Pin(28))
pwm_blue.freq(1000) 

 
def webpage(value):
    html = f"""
            <!DOCTYPE html>
            <html>
            <body>
            <form action="./red">
            <input type="submit" value="red " />
            </form>
            <form action="./green">
            <input type="submit" value="green" />
            </form>
            <form action="./blue">
            <input type="submit" value="blue" />
            </form>
            <form action="./off">
            <input type="submit" value="off" />
            </form>
            </body>
            </html>
            """
    return html
 
def serve(connection):
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        
        print(request)
        
        if request == '/off?':
            set_pwm_rgb(pwm_red, 0)
            set_pwm_rgb(pwm_green, 0)
            set_pwm_rgb(pwm_blue, 0)
        elif request == '/red?':
            set_pwm_rgb(pwm_red, 100)
            set_pwm_rgb(pwm_green, 0)
            set_pwm_rgb(pwm_blue, 0)
        elif request == '/green?':
            set_pwm_rgb(pwm_red, 0)
            set_pwm_rgb(pwm_green, 100)
            set_pwm_rgb(pwm_blue, 0)
        elif request == '/blue?':
            set_pwm_rgb(pwm_red, 0)
            set_pwm_rgb(pwm_green, 0)
            set_pwm_rgb(pwm_blue, 100)
    
        html=webpage(value)
        client.send(html)
        client.close()
 
def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    print(connection)
    return(connection)
 
connect_to_internet(network_cred.SSID, network_cred.PASSWORD)

try:
    if ip is not None:
        connection=open_socket(ip)
        serve(connection)
except KeyboardInterrupt:
    machine.reset()