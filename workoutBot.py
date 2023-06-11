import os
import discord
from dotenv import load_dotenv
from workoutFunction import BotFunction
from workoutFunction import WorkoutData


load_dotenv()

token = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

state = None
index = 0

class Bot(discord.Client):
    async def on_ready(self):
        print("logged on")
    
    async def on_message(self, message):
        global state
        global index

        print(f"message found: {message.content} from {message.author} in {message.channel}")

        # if the bot it mentioned for workout
        if client.user in message.mentions:
            if "workout".lower() in message.content or "wo".lower() in message.content:
                state = True
                index = 0
                print("bot is being mentioned for workout")

                await message.channel.send("Time to workout! What are you doing today?\n- pull\n- push\n- leg\n- shoulder\n")

            else:
                print("bot is being mentioned but not for workout")

                await message.channel.send("You should go workout, that's the only thing I can help you.")
        
        # once session starts
        elif message.author.id != client.user.id and state:
            # endding the seesion
            if "!end".lower() in message.content:
                state = False
                index = 0

            # starting session
            elif "pull".lower() in message.content:
                index = index + 1
                BotFunction.start_workout()
                await message.channel.send(index)
                


            elif "push".lower() in message.content:
                index = index + 1

            elif "leg".lower() in message.content:
                index = index + 1

            elif "shoulder".lower() in message.content:
                index = index + 1


client = Bot(intents=intents)
client.run(token)
