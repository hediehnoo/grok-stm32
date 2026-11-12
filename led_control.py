import serial
import time

# اگر از USB-TTL استفاده می‌کنی بگذار /dev/ttyUSB0
ser = serial.Serial('/dev/serial0', 115200, timeout=1)
time.sleep(2)  # صبر برای آماده شدن پورت

def send_command(cmd):
    ser.write((cmd + '\n').encode('utf-8'))
    print(f"ارسال شد: {cmd}")

print("دستورات: on / off / exit")

while True:
    cmd = input("دستور: ").strip().lower()
    
    if cmd == "on":
        send_command("LED_ON")
    elif cmd == "off":
        send_command("LED_OFF")
    elif cmd == "exit":
        break
    else:
        print("دستور نامعتبر")

ser.close()
print("پایان")
