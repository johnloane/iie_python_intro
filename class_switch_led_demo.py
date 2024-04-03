import machine
import utime

led_red = machine.Pin(10, machine.Pin.OUT)
led_green = machine.Pin(11, machine.Pin.OUT)
led_blue = machine.Pin(14, machine.Pin.OUT)

def change_colour(colour):
    if colour == "red":
        led_red.value(0)
        led_green.value(1)
        led_blue.value(1)
    elif colour == "green":
        led_red.value(1)
        led_green.value(0)
        led_blue.value(1)
    elif colour == "blue":
        led_red.value(1)
        led_green.value(1)
        led_blue.value(0)
    elif colour == "off":
        led_red.value(1)
        led_green.value(1)
        led_blue.value(1)
    
    


button_green = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if button_green.value() == 0:
        change_colour("red")
        utime.sleep(1)
        change_colour("green")
        utime.sleep(1)
        change_colour("blue")
        utime.sleep(1)
        change_colour("off")
        