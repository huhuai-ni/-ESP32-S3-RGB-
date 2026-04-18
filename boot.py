import network
import time

ssid = 'WiFi名字'
password = '密码'

print(f"正在连接WiFi: {ssid}")
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(ssid, password)

while not sta.isconnected():
    time.sleep(0.5)

print('网络连接成功！')
print('IP地址:', sta.ifconfig()[0])
