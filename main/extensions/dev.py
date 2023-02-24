import discord
from discord.ext import commands
from datetime import datetime
import config

class DevView(discord.ui.View):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @discord.ui.button(label="Sync", style=discord.ButtonStyle.blurple)
    async def sync(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        if self.bot.owner_id == interaction.user.id:
            await self.bot.tree.sync()
            await interaction.followup.send(content="Bot tree has been synced.", ephemeral=True)
        else:
            await interaction.followup.send(content="This button is for the owner of the bot!", ephemeral=True)

    @discord.ui.button(label="Reload", style=discord.ButtonStyle.blurple)
    async def reload(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        if self.bot.owner_id == interaction.user.id:
            try:
                for ext in config.initial_extensions:
                    await self.bot.reload_extension(ext)
                await interaction.followup.send(content="Extensions have been reloaded.", ephemeral=True)
            except Exception as e:
                await interaction.followup.send(content=f"```py\n{e}\n```", ephemeral=True)
        else:
            await interaction.followup.send(content="This button is for the owner of the bot!", ephemeral=True)            


class DevTools(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command()
    async def sync(self, ctx: commands.Context):
        await self.bot.tree.sync()
        embed = discord.Embed(color=0x5865f2, title="Sync [`-sync`]", description="Cave Monkey app commands have been synced successfully.")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1074597800735690853/1074597847242117170/PicsArt_02-12-01.png")
        await ctx.send(embed=embed)

    @commands.is_owner()
    @commands.command()
    async def reload(self, ctx: commands.Context, extarg: str = None):
        if extarg is not None:
            try:
                await self.bot.reload_extension(f"extensions.{extarg}")
                embed = discord.Embed(color=0x5865f2, title="Reload [`-reload`]", description=f"Reloaded the `{extarg}` extension successfully!")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1074597800735690853/1074597847242117170/PicsArt_02-12-01.png")
                await ctx.send(embed=embed)
            except Exception as e:
                embed = discord.Embed(color=0x585f2, title="Encountered Problem [`-reload`]", description=f"```py\n{e}\n```")
                await ctx.send(embed=embed)
        else:
            try:
                for ext in config.initial_extensions:
                    await self.bot.reload_extension(ext)
                embed = discord.Embed(color=0x5865f2, title="Reload [`-reload`]", description="Cave Monkey extensions have been reloaded successfully.")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1074597800735690853/1074597847242117170/PicsArt_02-12-01.png")
                await ctx.send(embed=embed)
            except Exception as e:
                embed = discord.Embed(color=0x585f2, title="Encountered Problem [`-reload`]", description=f"```py\n{e}\n```")
                embed.set_footer(text=f"ⓘ {ext} could not be loaded.")
                await ctx.send(embed=embed)

    @commands.is_owner()
    @commands.command()
    async def dev(self, ctx: commands.Context):
        embed = discord.Embed(color=0x5865f2, title="Developer Menu [`/dev`]")
        latency = f"""
```ansi
[0;36mBot Latency: {round(self.bot.latency * 1000)} ms[0m
```"""
        embed.add_field(name="Latency", value=latency, inline=False)
        delta_uptime = datetime.utcnow() - self.bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        uptime = f"""
```ansi
[0;32mBot Uptime: {days}d, {hours}h, {minutes}m, {seconds}s[0m
```"""
        embed.add_field(name="Uptime", value=uptime, inline=False)
        info = f"""
```ansi
[0;33mOwner: {self.bot.get_user(config.owner_id).name}#{self.bot.get_user(config.owner_id).discriminator}
Prefix: {config.prefix}
Prefix Commands: {len(self.bot.commands)}
App Commands: {len(self.bot.tree.get_commands())}[0m
```"""
        embed.add_field(name="Info", value=info, inline=False)
        view = DevView(self.bot)
        await ctx.send(embed=embed, view=view)


async def setup(bot: commands.Bot):
    await bot.add_cog(DevTools(bot))
