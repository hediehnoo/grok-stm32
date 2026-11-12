import os
import serial
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

# پورت سریال - اگر USB-TTL داری بگذار /dev/ttyUSB0
SERIAL_PORT = "/dev/serial0"
BAUD = 115200

try:
    ser = serial.Serial(SERIAL_PORT, BAUD, timeout=1)
    print("پورت سریال باز شد:", ser.name)
except:
    print("پورت سریال باز نشد - فقط API کار می‌کند")
    ser = None

def ask_grok(prompt):
    print("\nدرخواست:", prompt)
    response = client.chat.completions.create(
        model="grok-4.7",
        messages=[
            {"role": "system", "content": "پاسخ کوتاه و واضح بده."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=250
    )
    reply = response.choices[0].message.content.strip()
    print("پاسخ گروک:", reply)
    return reply

def send_to_stm32(text):
    if ser and ser.is_open:
        ser.write((text + "\n").encode("utf-8"))
        print("ارسال شد به STM32")
    else:
        print("سریال باز نیست")

# تست اولیه
reply = ask_grok("سلام، وضعیت را کوتاه بگو")
send_to_stm32(reply)

# حلقه اصلی
while True:
    try:
        msg = input("\nپیام تو (Enter برای خروج): ").strip()
        if not msg:
            break
        reply = ask_grok(msg)
        send_to_stm32(reply)
    except KeyboardInterrupt:
        break

if ser:
    ser.close()
