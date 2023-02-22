# Imports
import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime
from config import TOKEN

# Setup
initial_extensions = ("extensions.vtsg", "extensions.pop", "extensions.income", "extensions.player", "extensions.help")

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
bot.launch_time = datetime.utcnow()

# Functionality
@commands.is_owner()
@bot.command()
async def sync(ctx):
    await bot.tree.sync()
    embed = discord.Embed(color=0x5865f2, title="Sync [`-sync`]", description="Cave Monkey app commands have been synced successfully.")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1074597800735690853/1074597847242117170/PicsArt_02-12-01.png")
    await ctx.send(embed=embed)

@commands.is_owner()
@bot.command()
async def reload(ctx, extarg: str = None):
    if extarg is not None:
        try:
            await bot.reload_extension(f"extensions.{extarg}")
            embed = discord.Embed(color=0x5865f2, title="Reload [`-reload`]", description=f"Reloaded the `{extarg}` extension successfully!")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/1074597800735690853/1074597847242117170/PicsArt_02-12-01.png")
            await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(color=0x585f2, title="Encountered Problem [`-reload`]", description=f"```py\n{e}\n```")
            await ctx.send(embed=embed)
    else:
        try:
            for ext in initial_extensions:
                await bot.reload_extension(ext)
            embed = discord.Embed(color=0x5865f2, title="Reload [`-reload`]", description="Cave Monkey extensions have been reloaded successfully.")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/1074597800735690853/1074597847242117170/PicsArt_02-12-01.png")
            await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(color=0x585f2, title="Encountered Problem [`-reload`]", description=f"```py\n{e}\n```")
            embed.set_footer(text=f"ⓘ {ext} could not be loaded.")
            await ctx.send(embed=embed)

# Running
bot.run(TOKEN)
