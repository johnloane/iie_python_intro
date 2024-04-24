from machine import Pin, PWM
from time import sleep
import network
from umqtt.simple import MQTTClient
import secrets

led_red = PWM(Pin(10))
led_green = PWM(Pin(11))
led_blue = PWM(Pin(14))

led_red.freq(1000)
led_green.freq(1000)
led_blue.freq(1000)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.wifi_ssid, secrets.wifi_password)
while wlan.isconnected() == False:
    print("Waiting for connection...")
    utime.sleep(1)
print("Connected to John's hotspot")

# Initialise MQTTClient and connect to MQTT server
mqtt_client = MQTTClient(client_id = secrets.MQTT_CLIENT_ID, server = secrets.MQTT_HOST, user = secrets.MQTT_USERNAME, password = secrets.MQTT_PASSWORD)


while True:
    for duty in range(65025):
        led_red.duty_u16(duty)
        led_green.duty_u16(duty)
        led_blue.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025, 0, -1):
        led_red.duty_u16(duty)
        led_green.duty_u16(duty)
        led_blue.duty_u16(duty)
        sleep(0.0001)