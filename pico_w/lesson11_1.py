#from machine import Pin

#red_led = Pin(15,mode=Pin.OUT)
#red_led.value(1)
#red_led.value(0)

from machine import Pin
import time

red_led = Pin(15,mode=Pin.OUT)
btn = Pin(14,mode=Pin.PULL_DOWN)

while True:
    if btn.value():
        red_led.value(1)
    else:
        red_led.value(0)