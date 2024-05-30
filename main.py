import time
import network_cred
import network
from machine import Pin, PWM
import random



# create wifi connection 
def connect_to_internet(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    #wlan.activate(True)
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
        print("Connected")
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

connect_to_internet(network_cred.SSID, network_cred.PASSWORD)

#Changing values for 3 led's randomly

while True:
    set_pwm_rgb(pwm_red, random.randint(0,100))
    set_pwm_rgb(pwm_green, random.randint(0,100))
    set_pwm_rgb(pwm_blue, random.randint(0,100))
    time.sleep(1)
    print("chaning values randomly")



