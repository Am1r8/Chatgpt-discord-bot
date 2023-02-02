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
    response_dict = response.get('choice')
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0].get['text']
    return prompt_response