import machine
import utime

button_red = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_green = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)

motor = machine.PWM(machine.Pin(6))

motor.freq(8)

while True:
    if button_green.value() == 0:
        print("Turning motor on")
        motor.duty_u16(65535)
        utime.sleep(5)
    if button_red.value() == 1:
        print("Turning motor off")
        motor.duty_u16(0)
        utime.sleep(5)