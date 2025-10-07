from machine import Pin
import time

led = Pin(20, Pin.OUT)
button = Pin(22, Pin.IN, Pin.PULL_DOWN)

led_state = 0

while True:
    if button.value():           # button pressed
        led_state = int(not led_state)   # toggle LED state
        led.value(led_state)
        time.sleep(0.3)   # debounce delay
