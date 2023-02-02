import openai
import os

openai_api = ""


def chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=100,
    )