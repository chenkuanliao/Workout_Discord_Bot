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

        # if the bot it mentioned for workout
        if client.user in message.mentions:
            if "workout".lower() in message.content or "wo".lower() in message.content:
                print("bot is being mentioned for workout")

                await message.channel.send("Time to workout! What are you doing today?\n- pull\n- push\n- leg\n- shoulder\n")

            else:
                print("bot is being mentioned but not for workout")

                await message.channel.send("You should go workout, that's the only thing I can help you.")



client = Bot(intents=intents)
client.run(token)
