import discord
import os
from openai import chatgpt_response

discord_token = ""

class Myclient(discord.Client):
    async def on_ready(self):
        print("Bot is ready")