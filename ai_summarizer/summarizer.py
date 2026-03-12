from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPEN_AI_API_KEY")
)

# read text
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

prompt = f"Summarize the following text:\n\n{text}"

response = client.chat.completions.create(
    model="openrouter/auto",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

summary = response.choices[0].message.content

print("\nSummary:\n")
print(summary)

with open("summary.txt", "w", encoding="utf-8") as f:
    f.write(summary)