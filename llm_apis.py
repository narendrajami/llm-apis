from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

#api call
answer = client.responses.create(
    model="gpt-4.1",
    input="what is the value of pi?"
)

#extracts just the text
print(answer.output_text)

#multi-turn conversations
result1 = client.responses.create(
    model="gpt-4.1",
    input=[
        {"role":"user", "content": "My name is Jami"},
        {"role":"assistant", "content": "Nice to meet you, Jami"},
        {"role":"user", "content":"what is my name?"}
    ]
)

print(result1.output_text)

#system prompt, temperature , max_tokens

result2 = client.responses.create(
    model="gpt-4.1",
    instructions="you are a helpful assistant who makes jokes",
    input="what is sum of 1 and 3?",
    temperature=0.5,
    max_output_tokens=100
)

print(result2.output_text)
print(f"input tokens: {result2.usage.input_tokens}")
print(f"output tokens: {result2.usage.output_tokens}")
print(f"total tokens: {result2.usage.total_tokens}")

stream = client.responses.create(
    model="gpt-4.1",
    instructions="You are a helpful assistant",
    input="Tell me a short story you know",
    stream=True
)

for event in stream:
    if hasattr(event,'delta'):
        print(event.delta, end="", flush=True)