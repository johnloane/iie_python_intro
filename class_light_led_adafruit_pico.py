import machine
import utime
import network
from umqtt.simple import MQTTClient
import secrets
import _thread

button_red = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_green = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)

led_red = machine.Pin(10, machine.Pin.OUT)
led_green = machine.Pin(11, machine.Pin.OUT)
led_blue = machine.Pin(14, machine.Pin.OUT)

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

# Need a callback function to respond to messages
def mqtt_subscription_callback(topic, message):
    print(f'Topic {topic} recieved message {message}')
    if message == b'on':
        print("Light on")
        led_red.value(0)
        led_green.value(0)
        led_blue.value(0)
    elif message == b'off':
        print("Light off")
        led_red.value(1)
        led_green.value(1)
        led_blue.value(1)
        
        
def listen_for_button_press():
    while True:
        if button_red.value() == 1:
            print("Red")
            mqtt_client.publish(secrets.MQTT_TOPIC, "off")
            led_red.value(1)
            led_green.value(1)
            led_blue.value(1)
                
        if button_green.value() == 0:
            print("Green")
            mqtt_client.publish(secrets.MQTT_TOPIC, "on")
            led_red.value(0)
            led_green.value(0)
            led_blue.value(0)
            
        utime.sleep(0.25)
        
        
mqtt_client.set_callback(mqtt_subscription_callback)
mqtt_client.connect()

# Once connected subscribe to a topic
mqtt_client.subscribe(secrets.MQTT_TOPIC)

print("Waiting for messages")

_thread.start_new_thread(listen_for_button_press, ())

while True: 
    mqtt_client.wait_msg()    
    utime.sleep(0.25)
