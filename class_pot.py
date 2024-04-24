from machine import PWM, Pin
import utime
import network
from umqtt.simple import MQTTClient
import secrets

potentiometer = machine.ADC(26)


led_red = PWM(Pin(10))
led_green = PWM(Pin(11))
led_blue = PWM(Pin(14))

led_red.freq(1000)
led_green.freq(1000)
led_blue.freq(1000)

# Connect to the internet
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.wifi_ssid, secrets.wifi_password)
while wlan.isconnected() == False:
    print("Waiting for connection...")
    utime.sleep(1)
print("Connected to John's hotspot")

# Initialise MQTTClient and connect to MQTT server
mqtt_client = MQTTClient(client_id = secrets.MQTT_CLIENT_ID, server = secrets.MQTT_HOST, user = secrets.MQTT_USERNAME, password = secrets.MQTT_PASSWORD)

mqtt_client.connect()

def turn_led_off():
    while True:
        led_red.duty_u16(0)
        led_green.duty_u16(0)
        led_blue.duty_u16(0)
    
#def light_led_based_on_pot(value):
    

#turn_led_off()

while True:
    result = potentiometer.read_u16()
    if result < 300:
        result = 0
    value = 65535 - result
    
    print(value)
    mqtt_client.publish(secrets.MQTT_TOPIC, str(result))
    led_red.duty_u16(value)
    led_green.duty_u16(value)
    led_blue.duty_u16(value)
    #light_led_based_on_pot(pot_value)
    utime.sleep(5)