from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("XAI_API_KEY")
print("کلید پیدا شد؟", "بله" if api_key else "خیر")
print("طول کلید:", len(api_key) if api_key else 0)

client = OpenAI(
    api_key=api_key,
    base_url="https://api.x.ai/v1"
)

print("\nدر حال ارسال درخواست...")

try:
    response = client.responses.create(
        model="grok-4.7",
        input="سلام، خودت را معرفی کن"
    )
    print("\n✅ پاسخ گروک:")
    print(response.output_text)

except Exception as e:
    print("\n❌ خطای کامل:")
    print(type(e).__name__)
    print(e)
    if hasattr(e, 'response') and e.response is not None:
        print("وضعیت:", e.response.status_code)
        try:
            print("متن پاسخ سرور:", e.response.text)
        except:
            pass
