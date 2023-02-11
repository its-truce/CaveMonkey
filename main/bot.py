# Imports
import discord
from discord.ext import commands
from discord import app_commands

# Setup
token = "YOUR TOKEN HERE"
initial_extensions = ("extensions.vtsg", "extensions.pop", "extensions.income", "extensions.player")

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content= True
        intents.members = True
        intents.presences = True
        activity = discord.Game(name="Bloons TD 6")
        super().__init__(command_prefix=commands.when_mentioned_or("-"), intents=intents, activity=activity, status=discord.Status.idle, owner_id = 626333424965386240)

    async def setup_hook(self):
        for ext in initial_extensions:
            try:
                await self.load_extension(ext)
            except Exception as e:
                print(f"Failed to load extension {ext}.\nException:\n{e}")
bot = Bot()

# Functionality
@commands.is_owner()
@bot.command()
async def sync(ctx):
    await bot.tree.sync()
    embed = discord.Embed(color=0x5865f2, title="Sync [`-sync`]", description="Cave Monkey app commands have been synced successfully.")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1072801761775071252/1073502646666805248/pfp.png?width=580&height=580")
    await ctx.send(embed=embed)

@commands.is_owner()
@bot.command()
async def reload(ctx):
    try:
        for ext in initial_extensions:
            await bot.reload_extension(ext)
        embed = discord.Embed(color=0x5865f2, title="Reload [`-reload`]", description="Cave Monkey extensions have been reloaded successfully.")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1072801761775071252/1073502646666805248/pfp.png?width=580&height=580")
        await ctx.send(embed=embed)
    except Exception as e:
        print(f"Failed to reload extension {ext}.\nException:\n{e}")

# Running
bot.run(token)
