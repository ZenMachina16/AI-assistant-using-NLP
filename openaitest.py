import openai
from config import apikey


openai.api_key=apikey="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"
# print(apikey)


response = openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt="write an essay on christmas",
  temperature=0.74,
  max_tokens=5000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


print(response["choices"][0]["text"])