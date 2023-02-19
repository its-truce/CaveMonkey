import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime

class HelpDropdown(discord.ui.Select):
    def __init__(self, bot):
        self.bot = bot
        options = [
            discord.SelectOption(label="Information", description="Displays general information about the bot.", default=True),
            discord.SelectOption(label="Stats", description="Displays stats about the bot.")
        ]
        super().__init__(min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        if self.values[0] == "Information":
            info_embed = discord.Embed(color=0x5865f2, title="Information [`/info`]")
            info_embed.set_thumbnail(url="https://media.discordapp.net/attachments/1074597800735690853/1074598467906830387/pfp.png?width=580&height=580")
            info_embed.set_image(url="https://media.discordapp.net/attachments/1074597800735690853/1074598065601773578/PicsArt_02-12-01.png")
            info_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            info_embed.add_field(name="Developer", value="╰ [truce#7887](https://discord.com/users/626333424965386240)")
            info_embed.add_field(name="Source", value="╰ [please star the repo!](https://github.com/its-truce/CaveMonkey)", inline=False)
            info_embed.add_field(name="Description", value="Cave Monkey is a bot made to help you step up your BTD6 gameplay. If you find any of the information incorrect "
            "or want to suggest commands, you can DM me.", inline=False)
            info_embed.add_field(name="Commands", value="This bot uses slash commands. You can bring up the entire list of commands by typing `/` and clicking on the bot's pfp.", 
                inline=False)
            self.options[1].default = False
            self.options[0].default = True
            await interaction.edit_original_response(embed=info_embed, view=self.view)
        if self.values[0] == "Stats":
            stats_embed = discord.Embed(color=0x5865f2, title="Stats [`/info`]")
            stats_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            package_info = """
```ansi
[0;36mOS: Windows 11
Python: 3.10.0 (default, Feb 14 2023) [GCC 6.3.0]
Library: discord.py
Library Version: 2.1.0[0m
```"""
            stats_embed.add_field(name="Package Info", value=package_info, inline=False)
            latency = f"""
```ansi
[0;31mBot Latency: {round(self.bot.latency * 1000)} ms[0m
```"""
            stats_embed.add_field(name="Latency", value=latency, inline=False)
            delta_uptime = datetime.utcnow() - self.bot.launch_time
            hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
            minutes, seconds = divmod(remainder, 60)
            days, hours = divmod(hours, 24)
            uptime = f"""
```ansi
[0;33mBot Uptime: {days}d, {hours}h, {minutes}m, {seconds}s[0m
```"""
            stats_embed.add_field(name="Uptime", value=uptime, inline=False)
            presence = f"""
```ansi
[0;34mUsers: {len(self.bot.users)}
Guilds: {len(self.bot.guilds)}[0m
```"""
            stats_embed.add_field(name="Presence", value=presence, inline=False)
            host = """
```ansi
[0;35mCPU: Intel i5 10th Gen 
Total RAM: 8 GB
Disk: 1 TB HDD
GPU: Intel(R) UHD Graphics[0m
```"""
            stats_embed.add_field(name="Host Specs", value=host, inline=False)
            self.options[0].default = False
            self.options[1].default = True
            await interaction.edit_original_response(embed=stats_embed, view=self.view)            


class HelpView(discord.ui.View):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.add_item(HelpDropdown(self.bot))


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description="Shows information and stats about the bot.")
    async def info(self, interaction: discord.Interaction):
        info_embed = discord.Embed(color=0x5865f2, title="Information [`/info`]")
        info_embed.set_thumbnail(url="https://media.discordapp.net/attachments/1074597800735690853/1074598467906830387/pfp.png?width=580&height=580")
        info_embed.set_image(url="https://media.discordapp.net/attachments/1074597800735690853/1074598065601773578/PicsArt_02-12-01.png")
        info_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
        info_embed.add_field(name="Developer", value="╰ [truce#7887](https://discord.com/users/626333424965386240)")
        info_embed.add_field(name="Source", value="╰ [please star the repo!](https://github.com/its-truce/CaveMonkey)", inline=False)
        info_embed.add_field(name="Description", value="Cave Monkey is a bot made to help you step up your BTD6 gameplay. If you find any of the information incorrect "
        "or want to suggest commands, you can DM me.", inline=False)
        info_embed.add_field(name="Commands", value="This bot uses slash commands. You can bring up the entire list of commands by typing `/` and clicking on the bot's pfp.", 
            inline=False)
        view = HelpView(self.bot)
        await interaction.response.send_message(embed=info_embed, view=view)

    @app_commands.command(description="Sends the invite link for the bot.")
    async def invite(self, interaction: discord.Interaction):
        invite_embed = discord.Embed(color=0x5865f2, title="Invite [`/invite`]", description="[Click here to add me to your server!](https://discord.com/api/oauth2/authorize?client_id=1069569059257077840&permissions=517543938112&scope=bot)")
        invite_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
        await interaction.response.send_message(embed=invite_embed)
        
    @app_commands.command(description="Sends the source of the bot.")
    async def source(self, interaction: discord.Interaction):
        await interaction.response.send_message("https://github.com/its-truce/CaveMonkey")

async def setup(bot):
    await bot.add_cog(Help(bot))