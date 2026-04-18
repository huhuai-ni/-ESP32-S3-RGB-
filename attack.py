import paho.mqtt.client as mqtt

broker = "db660b7df5154b248d9321f0ffc54009.s1.eu.hivemq.cloud"
port = 8883
username = ""
password = ""
topic = "home/rgb"

client = mqtt.Client()
client.username_pw_set(username, password)
client.tls_set()
client.connect(broker, port)
client.publish(topic, "off")
client.disconnect()
print("重放攻击完成：已发送 'off' 指令")
