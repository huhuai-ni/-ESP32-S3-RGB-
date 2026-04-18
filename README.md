# -ESP32-S3-RGB-
个基于 ESP32-S3、MicroPython 和 HiveMQ Cloud 的物联网全栈项目。它不仅实现了从硬件驱动、Wi-Fi 联网到云端 MQTT 远程控制的完整链路，还包含了 安全思维注入 实验
🧰 硬件清单
名称	型号/规格	数量
ESP32-S3 开发板	板载 CH343 芯片 (或 CH340)	1
可寻址 RGB LED	板载 (NeoPixel / WS2812)	1
Micro USB 数据线	确保可传输数据




 快速开始
1. 烧录 MicroPython 固件
下载 ESP32_GENERIC_S3-20260406-v1.28.0.bin（或访问 官网 获取最新版）。

使用 esptool 或 乐鑫 Flash Download Tool 烧录，地址设为 0x0。

烧录前请擦除整个 Flash。

2. 上传代码与依赖库
使用 Thonny IDE 连接 ESP32-S3，将以下文件保存到 MicroPython 设备：

文件	位置	说明
boot.py	根目录	Wi-Fi 连接配置（替换你的 SSID 和密码）
main.py	根目录	主程序（替换 MQTT 凭证）
umqtt/simple.py	/lib/umqtt/	MQTT 基础库
umqtt/robust.py	/lib/umqtt/	带自动重连的 MQTT 库
3. 配置 HiveMQ Cloud
注册 HiveMQ Cloud 免费 Serverless 集群。

创建 Access Credential（用户名/密码）。

将 main.py 中的 MQTT_BROKER、MQTT_USER、MQTT_PWD 替换为你的信息。

4. 运行与测试
重启 ESP32，观察板载 RGB LED 依次闪烁红、绿、蓝（表示 MQTT 连接成功）。

打开 web/index.html（需替换其中的 MQTT 凭证），点击按钮即可远程控制灯光颜色。

查看 Thonny Shell 输出，确认收到指令。
