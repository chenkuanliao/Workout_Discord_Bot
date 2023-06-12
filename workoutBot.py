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
        global workout

        print(f"message found: {message.content} from {message.author} in {message.channel}")

        # if the bot it mentioned for workout
        if client.user in message.mentions:
            if "workout" in message.content.lower() or "wo" in message.content.lower():
                state = True
                index = 0
                workout = None
                print("bot is being mentioned for workout")

                await message.channel.send("Time to workout! What are you doing today?\n- pull\n- push\n- leg\n- shoulder\n")

            else:
                print("bot is being mentioned but not for workout")

                await message.channel.send("You should go workout, that's the only thing I can help you.")
        
        # once session starts
        elif message.author.id != client.user.id and state:
            # endding the seesion
            if "!end" in message.content.lower():
                state = False
                index = 0
                await message.channel.send("this session has been ended")

            # starting session
            elif "pull" == message.content.lower():
                index = 1
                workout = BotFunction.get_workout("pull")
                string = BotFunction.get_summary(workout)
                await message.channel.send(string)
                await message.channel.send("type 'next' or 'n' to start workout")


            elif "push" ==  message.content.lower():
                index = 1
                workout = BotFunction.get_workout("push")
                string = BotFunction.get_summary(workout)
                await message.channel.send(string)
                await message.channel.send("type 'next' or 'n' to start workout")

            elif "leg" ==  message.content.lower():
                index = 1
                workout = BotFunction.get_workout("leg")
                string = BotFunction.get_summary(workout)
                await message.channel.send(string)
                await message.channel.send("type 'next' or 'n' to start workout")

            elif "shoulder" == message.content.lower():
                index = 1
                workout = BotFunction.get_workout("shoulder")
                string = BotFunction.get_summary(workout)
                await message.channel.send(string)
                await message.channel.send("type 'next' or 'n' to start workout")

            elif "next" == message.content.lower()or "n" == message.content.lower():
                if workout == None:
                    await message.channel.send("No workout has been selected yet")
                elif len(workout)-1 < index:
                    index = 0
                    state = False
                    await message.channel.send("You're done with your workout! Nice!")

                else:
                    string = BotFunction.get_current_workout(workout, index)
                    await message.channel.send(string)
                    index = index + 1


client = Bot(intents=intents)
client.run(token)
