import argparse
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

def generate_code(prompt):
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=2000,
        temperature=0,
        system="You are an orchestration savant. You have the assistance of a human operator who can help you rearrange or optimize code. You only have access to the most recent python file that you create, it will be included with your prompt. Your first task is to build this system in a single file. Your response will be copied into a new file, it should be albe to create new subsequent files in an organized manner in this directory.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )

    return message.content[0].text

def main():
    parser = argparse.ArgumentParser(description="Generate Python code from a problem prompt using Claude")
    parser.add_argument("prompt", help="The problem prompt to generate code for")
    parser.add_argument("output_file", help="The file to write the generated code to")
    args = parser.parse_args()

    generated_code = generate_code("""The new file will be called file_1.py. Here is the current file that this prompt is in, initiator.py: import argparse
import anthropic
import os

def generate_code(prompt):
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=2000,
        temperature=0,
        system="You are an orchestration savant. You have the assistance of a human operator who can help you rearrange or optimize code. You only have access to the most recent python file that you create, it will be included with your prompt. Your first task is to build this system in a single file. Your response will be copied into a new file, it should be albe to create new subsequent files in an organized manner in this directory.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )

    return message.content.content[0].text

def main():
    parser = argparse.ArgumentParser(description="Generate Python code from a problem prompt using Claude")
    parser.add_argument("prompt", help="The problem prompt to generate code for")
    parser.add_argument("output_file", help="The file to write the generated code to")
    args = parser.parse_args()

    generated_code = generate_code("The new file will be called file_1.py. Here is the current file that this prompt is in, initiator.py: ")

    with open(args.output_file, "w") as f:
        f.write(generated_code)

if __name__ == "__main__":
    main()""")

    with open(args.output_file, "w") as f:
        print(generated_code)
        f.write(generated_code)

if __name__ == "__main__":
    main()
