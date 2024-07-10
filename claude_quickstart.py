from dotenv import load_dotenv
import os

load_dotenv()

import anthropic

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=2000,
    temperature=0,
    system="You are an orchestration savant. Determine useful networked agent and orchestration patterns and describe them in concise detail for the given field or use case or problem statement.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "DRF + Vue software automation. We have a working template pattern. We want to automate the continuous creation of new APIs, frontend components, and database models based on distilled insignts from live user feedback."
                }
            ]
        }
    ]
)
print(message.content)
