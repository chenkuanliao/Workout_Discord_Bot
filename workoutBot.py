import os
import discord
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

class Bot(discord.Client):
    async def on_ready(self):
        print("logged on")
    
    async def on_message(self, message):
        print(f"message found: {message.content} from {message.author} in {message.channel}")

client = Bot(intents=intents)
client.run(token)
