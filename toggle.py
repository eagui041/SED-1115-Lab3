from machine import Pin
import time

led1 = Pin(18, Pin.OUT)
sw1 = Pin(10, Pin.IN, Pin.PULL_DOWN)

#code to turn off led1 upon loading
led1.off()

led1_state = False  # initialize the LED state to off
debounce_delay = 80  # set the debounce delay to 100 milliseconds

while True:
    if sw1.value() == 1:
        led1_state = not led1_state  # toggle the LED state
        if led1_state: # if the LED state is True, turn on the LED
            led1.on()
        else:
            led1.off()
        time.sleep_ms(debounce_delay)  # add a debounce delay
        while sw1.value() == 1:
            pass  # wait for the button to be released
