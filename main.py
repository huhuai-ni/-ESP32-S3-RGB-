import time
import ssl
from machine import Pin, reset
import neopixel
from umqtt.robust import MQTTClient

# ========== 配置 ==========
MQTT_BROKER = 'db660b7df5154b248d9321f0ffc54009.s1.eu.hivemq.cloud'
MQTT_PORT = 8883
MQTT_USER = ''
MQTT_PWD = ''
MQTT_TOPIC = b'home/rgb'
CLIENT_ID = 'esp32s3_rgb'
LED_PIN = 48
# ==========================

np = neopixel.NeoPixel(Pin(LED_PIN), 1)

def startup_blink():
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    for color in colors:
        np[0] = color
        np.write()
        time.sleep(0.3)
        np[0] = (0, 0, 0)
        np.write()
        time.sleep(0.2)

def on_message(topic, msg):
    print('收到指令:', msg)
    msg_str = msg.decode().lower()
    if msg_str == 'red':
        np[0] = (255, 0, 0)
        np.write()
    elif msg_str == 'green':
        np[0] = (0, 255, 0)
        np.write()
    elif msg_str == 'blue':
        np[0] = (0, 0, 255)
        np.write()
    elif msg_str == 'off':
        np[0] = (0, 0, 0)
        np.write()

def connect_mqtt():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.verify_mode = ssl.CERT_NONE
    client = MQTTClient(CLIENT_ID, MQTT_BROKER, port=MQTT_PORT,
                        user=MQTT_USER, password=MQTT_PWD,
                        keepalive=60, ssl=context)
    client.set_callback(on_message)
    client.connect()
    client.subscribe(MQTT_TOPIC)
    print('已连接到 HiveMQ Cloud！')
    print('已订阅主题:', MQTT_TOPIC.decode())
    return client

print('正在连接 HiveMQ Cloud...')
client = connect_mqtt()
startup_blink()

last_ping_time = time.time()
PING_INTERVAL = 60

while True:
    try:
        client.check_msg()
        now = time.time()
        if now - last_ping_time > PING_INTERVAL:
            try:
                client.publish(b'home/heartbeat', b'ping')
                print('[心跳] 已发送')
            except Exception as e:
                print('[心跳] 发送失败:', e)
                print('连接已死，5秒后重启...')
                time.sleep(5)
                reset()
            last_ping_time = now
        time.sleep(0.1)
    except OSError as e:
        print('OSError:', e)
        time.sleep(5)
        reset()
    except Exception as e:
        print('Exception:', e)
        time.sleep(5)
        reset()
