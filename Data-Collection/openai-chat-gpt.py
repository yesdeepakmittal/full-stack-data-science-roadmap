# https://www.codingthesmartway.com/how-to-use-chatgpt-with-python/

import openai

my_token = ""
openai.api_key = my_token

model_engine = "text-davinci-003"

'''Please generate some conversational text between a girl and a boy'''
prompt = "synset in NLP"

completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=2048,#1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)