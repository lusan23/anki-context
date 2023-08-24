"""
Interact with gpt to generate and ask it to generate
x examples.
"""

"""
PSEUDO CODE
PREP PROMP
SEND TO GPT
GET THE ANSWER 
FORMAT THE STRING 
PREPARE THE EXERCISES TO BE OUTPUTED
OUTPUT THE EXERCISES

"""
import openai
import json

api_keyy = "YOUR_API_HERE"

with open("my_apikey.json") as f:
    api_keyy = json.load(f)

openai.api_key = api_keyy

chat_completion = openai.ChatCompletion.create(
                                model='gpt-3.5-turbo',
                                messages=[
                                    {
                                        'role':'user',
                                        'content': 'hello world'
                                    }
                                ] )

print(chat_completion.choices[0].message.content)
