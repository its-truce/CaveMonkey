# Imports
import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime
import config

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content= True
        intents.members = True
        intents.presences = True
        activity = discord.Game(name="Bloons TD 6")
        super().__init__(command_prefix=commands.when_mentioned_or(config.prefix), intents=intents, activity=activity, status=discord.Status.idle, owner_id = config.owner_id)

    async def setup_hook(self):
        for ext in config.initial_extensions:
            try:
                await self.load_extension(ext)
            except Exception as e:
                print(f"Failed to load extension {ext}.\nException:\n{e}")

# Initializing the bot
bot = Bot()
bot.launch_time = datetime.utcnow()

# Running
if __name__ == "__main__":
    bot.run(config.token)
