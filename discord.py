import discord
import os
from openai import chatgpt_response

discord_token = ""

class Myclient(discord.Client):
    async def on_ready(self):
        print("Bot is ready")

    async def on_message(self, message):
        print(message.content)
        if message.author == self.user:
            return
        command, user_message = None, None

        for text in ['/ai', '/bot', '/chat', '/chatgpt']:
            if message.content.startswith(text):
                command = message.content.split(text)[0]
                user_message = message.content.replace(text, '')
                print(command, user_message)
        if command == '/ai' or command == '/bot' or command == '/chat' or command == '/chatgpt':
            bot_response = chatgpt_response(promt=user_message)
            await message.channel.send(bot_response)


intents = discord.Intents.default()
intents.message_content = True

client = Myclient(intents=intents)


if __name__ == '__main__':
    client.run(discord_token)