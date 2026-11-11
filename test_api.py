from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

response = client.chat.completions.create(
    model="grok-4.7",
    messages=[{"role": "user", "content": "سلام، خودت را معرفی کن"}]
)

print(response.choices[0].message.content)
