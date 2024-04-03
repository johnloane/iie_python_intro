import machine
import utime

button_red = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_green = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
light_green_led = machine.Pin(26, machine.Pin.OUT)

led_red = machine.Pin(10, machine.Pin.OUT)
led_green = machine.Pin(11, machine.Pin.OUT)
led_blue = machine.Pin(14, machine.Pin.OUT)

green_button_presscount = 0

while True:
    if button_red.value() == 1:
        print("Turning off")
        led_red.value(1)
        led_green.value(1)
        led_blue.value(1)
        green_button_presscount = 0
    if button_green.value() == 0:
        light_green_led.value(1)
        green_button_presscount += 1
        print("Green")
        if green_button_presscount % 2 != 0:
            led_red.value(1)
            led_green.value(0)
            led_blue.value(1)
        else:
            led_red.value(0)
            led_green.value(1)
            led_blue.value(1)
    #if button_red.value() == 1 and button_green.value() == 0:
        #led_red.value(1)
        #led_green.value(1)
        #led_blue.value(1)
    utime.sleep(0.25)
