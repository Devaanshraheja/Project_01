from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)