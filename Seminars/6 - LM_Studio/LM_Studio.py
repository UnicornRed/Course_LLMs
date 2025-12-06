import os
from openai import OpenAI

# Point the client to LM‑Studio
client = OpenAI(
    api_key="lm-studio",                     # dummy key – not used by LM‑Studio
    base_url="http://127.0.0.1:1234/v1"      # <-- change if you set a custom port
)

resp = client.chat.completions.create(
    model="openai/gpt-oss-20b",                    # the model name you loaded in LM‑Studio
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user",   "content": "Что делает функция ord в Python?"}
    ],
    temperature=0.7,
)

print(resp.choices[0].message.content.strip())