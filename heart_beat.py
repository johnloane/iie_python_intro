import machine
import utime

pulse_sensor = machine.Pin(26, machine.Pin.IN)
bpm = 0
last_value = 0
start_time = utime.time()
while True:
    current_value = pulse_sensor.value()
    print(current_value)
    if current_value != last_value:
        bpm += 1
    last_value = current_value
    current_time = utime.time()
    if current_time - start_time >= 15:
        bpm = bpm * 4
        print(f"Beats {bpm}")
        start_time = current_time
        bpm = 0
    utime.sleep(0.5)

