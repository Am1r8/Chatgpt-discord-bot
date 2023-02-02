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