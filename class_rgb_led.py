import machine
import utime

led_red = machine.Pin(10, machine.Pin.OUT)
led_green = machine.Pin(11, machine.Pin.OUT)
led_blue = machine.Pin(14, machine.Pin.OUT)

led_red.value(1)
led_green.value(1)
led_blue.value(1)

while True:
    print("Red")
    led_red.value(0)
    led_green.value(1)
    led_blue.value(1)
    utime.sleep(1)
    
    print("Green")
    led_red.value(1)
    led_green.value(0)
    led_blue.value(1)
    utime.sleep(1)
    
    print("Blue")
    led_red.value(1)
    led_green.value(1)
    led_blue.value(0)
    utime.sleep(1)
    
    print("Red and Green")
    led_red.value(0)
    led_green.value(0)
    led_blue.value(1)
    utime.sleep(1)
    
    print("Red and Blue")
    led_red.value(0)
    led_green.value(1)
    led_blue.value(0)
    utime.sleep(1)
    
    print("Green and Blue")
    led_red.value(1)
    led_green.value(0)
    led_blue.value(0)
    utime.sleep(1)
    
    print("White")
    led_red.value(0)
    led_green.value(0)
    led_blue.value(0)
    utime.sleep(1)
    
    print("End of loop, turning all off")
    led_red.value(1)
    led_green.value(1)
    led_blue.value(1)
    utime.sleep(1)