import machine
import utime
import network
import secrets
from umqtt.simple import MQTTClient


motor = machine.PWM(machine.Pin(6))

motor.freq(8)


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.config(pm = 0xa11149)
wlan.connect(secrets.wifi_ssid, secrets.wifi_password)
while wlan.isconnected() == False:
    print("Waiting for connection...")
    utime.sleep(1)
print("Connected to wifi")
status = wlan.ifconfig()
print('ip = ' + status[0])

mqtt_client = MQTTClient(client_id=secrets.MQTT_CLIENT_ID, server=secrets.MQTT_HOST, user=secrets.MQTT_USERNAME, password=secrets.MQTT_PASSWORD)

def mqtt_subscription_callback(topic, message):
    print(f'Topic {topic} recieved message {message}')
    if message == b'on':
        print("Fan ON")
        motor.duty_u16(65535)
    elif message == b'off':
        print("Fan OFF")
        motor.duty_u16(0)
       
mqtt_client.set_callback(mqtt_subscription_callback)
mqtt_client.connect()

mqtt_client.subscribe(secrets.MQTT_RECIEVE_TOPIC)
print("Connected and subscribe")

try:
    while True:
        print(f'Waiting for messages on {secrets.MQTT_RECIEVE_TOPIC}')
        mqtt_client.wait_msg()
except Exception as e:
    print(f'Failed to wait for MQTT message: {e}')
finally:
    mqtt_client.disconnect()

#while True:
#    print("Turning motor on")
#    motor.duty_u16(65535)
#    utime.sleep(5)
#    
#    print("Turning motor off")
#    motor.duty_u16(0)
#    utime.sleep(5)