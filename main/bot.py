# Imports
import discord
from discord.ext import commands
from discord import app_commands
from typing import Literal
import numpy as np
import pops
import cash

# Setup
token = "YOUR TOKEN HERE"

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content= True
        intents.members = True
        intents.presences = True
        activity = discord.Game(name="Bloons TD6")
        super().__init__(command_prefix=commands.when_mentioned_or("^"), intents=intents, activity=activity, status=discord.Status.idle)

bot = Bot()

# Functionality
@bot.command()
async def sync(ctx):
    await bot.tree.sync()

class PopButtons(discord.ui.View):
    def __init__(self, bloon, page):
        super().__init__()
        self.bloon = bloon
        self.page = page

    @discord.ui.button(label="Next", style=discord.ButtonStyle.blurple)
    async def next(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.bloon == "camo":
            if self.page == 0:
                desc = pops.camo1
                next_page = discord.Embed(color=0x00c93c, title="Camo Bloons [`/pop`]", description=desc)
                next_page.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/3/3b/Camo_Bloon.png/revision/latest?cb=20130113080255&path-prefix=bloons")
                next_page.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                await interaction.response.edit_message(embed=next_page)
                self.page += 1
                self.previous.disabled = False
                await interaction.message.edit(view=self)

            elif self.page == 1:
                desc = pops.camo2
                next_page = discord.Embed(color=0x00c93c, title="Camo Bloons [`/pop`]", description=desc)
                next_page.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/3/3b/Camo_Bloon.png/revision/latest?cb=20130113080255&path-prefix=bloons")
                next_page.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                await interaction.response.edit_message(embed=next_page)
                self.page += 1
                button.disabled = True
                self.previous.disabled = False
                await interaction.message.edit(view=self)

        if self.bloon == "lead":
            if self.page == 0:
                desc = pops.lead1
                next_page = discord.Embed(color=0x706f6f, title="Lead Bloons [`/pop`]", description=desc)
                next_page.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/f/fd/BTD6Lead.png/revision/latest?cb=20190620031244&path-prefix=bloons")
                next_page.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                await interaction.response.edit_message(embed=next_page)
                self.page += 1
                self.previous.disabled = False
                await interaction.message.edit(view=self)

            elif self.page == 1:
                desc = pops.lead2
                next_page = discord.Embed(color=0x706f6f, title="Lead Bloons [`/pop`]", description=desc)
                next_page.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/f/fd/BTD6Lead.png/revision/latest?cb=20190620031244&path-prefix=bloons")
                next_page.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                await interaction.response.edit_message(embed=next_page)
                self.page += 1
                button.disabled = True
                self.previous.disabled = False
                await interaction.message.edit(view=self)

        if self.bloon == "purple":
            if self.page == 0:
                desc = pops.purple1
                next_page = discord.Embed(color=0x8940ff, title="Purple Bloons [`/pop`]", description=desc)
                next_page.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/b/bd/BTD6Purple.png/revision/latest?cb=20180809061728&path-prefix=bloons")
                next_page.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                await interaction.response.edit_message(embed=next_page)
                self.page += 1
                self.previous.disabled = False
                await interaction.message.edit(view=self)

            elif self.page == 1:
                desc = pops.purple2
                next_page = discord.Embed(color=0x8940ff, title="Purple Bloons [`/pop`]", description=desc)
                next_page.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/b/bd/BTD6Purple.png/revision/latest?cb=20180809061728&path-prefix=bloons")
                next_page.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                await interaction.response.edit_message(embed=next_page)
                self.page += 1
                button.disabled = True
                self.previous.disabled = False
                await interaction.message.edit(view=self)

    @discord.ui.button(label="Previous", style=discord.ButtonStyle.blurple, disabled=True)
    async def previous(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.bloon == "camo":
            if self.page == 1:
                desc = pops.camo0
                previous_page = discord.Embed(color=0x00c93c, title="Camo Bloons [`/pop`]", description=desc)
                previous_page.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/3/3b/Camo_Bloon.png/revision/latest?cb=20130113080255&path-prefix=bloons")
                previous_page.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                await interaction.response.edit_message(embed=previous_page)
                self.page -= 1
                button.disabled = True
                self.next.disabled = False
                await interaction.message.edit(view=self)

            elif self.page == 2:    
                desc = pops.camo1
                previous_page = discord.Embed(color=0x00c93c, title="Camo Bloons [`/pop`]", description=desc)
                previous_page.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/3/3b/Camo_Bloon.png/revision/latest?cb=20130113080255&path-prefix=bloons")
                previous_page.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                await interaction.response.edit_message(embed=previous_page)
                self.page -= 1
                self.next.disabled = False
                await interaction.message.edit(view=self)
        
        if self.bloon == "lead":
            if self.page == 1:
                desc = pops.lead0
                previous_page = discord.Embed(color=0x706f6f, title="Lead Bloons [`/pop`]", description=desc)
                previous_page.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/f/fd/BTD6Lead.png/revision/latest?cb=20190620031244&path-prefix=bloons")
                previous_page.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                await interaction.response.edit_message(embed=previous_page)
                self.page -= 1
                button.disabled = True
                self.next.disabled = False
                await interaction.message.edit(view=self)

            elif self.page == 2:    
                desc = pops.lead1
                previous_page = discord.Embed(color=0x706f6f, title="Lead Bloons [`/pop`]", description=desc)
                previous_page.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/f/fd/BTD6Lead.png/revision/latest?cb=20190620031244&path-prefix=bloons")
                previous_page.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                await interaction.response.edit_message(embed=previous_page)
                self.page -= 1
                self.next.disabled = False
                await interaction.message.edit(view=self)

        if self.bloon == "purple":
            if self.page == 1:
                desc = pops.purple0
                previous_page = discord.Embed(color=0x8940ff, title="Purple Bloons [`/pop`]", description=desc)
                previous_page.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/b/bd/BTD6Purple.png/revision/latest?cb=20180809061728&path-prefix=bloons")
                previous_page.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                await interaction.response.edit_message(embed=previous_page)
                self.page -= 1
                button.disabled = True
                self.next.disabled = False
                await interaction.message.edit(view=self)

            elif self.page == 2:    
                desc = pops.purple1
                previous_page = discord.Embed(color=0x8940ff, title="Purple Bloons [`/pop`]", description=desc)
                previous_page.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/b/bd/BTD6Purple.png/revision/latest?cb=20180809061728&path-prefix=bloons")
                previous_page.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                await interaction.response.edit_message(embed=previous_page)
                self.page -= 1
                self.next.disabled = False
                await interaction.message.edit(view=self)


@bot.tree.command(description="Check which towers can pop certain balloons.")
@app_commands.describe(bloon="Type of bloon.")
async def pop(interaction: discord.Interaction, bloon: Literal["camo", "lead", "purple", "general"]):
    if bloon == "camo":
        view = PopButtons("camo", 0)
        desc = pops.camo0
        pop_embed = discord.Embed(color=0x00c93c, title="Camo Bloons [`/pop`]", description=desc)
        pop_embed.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/3/3b/Camo_Bloon.png/revision/latest?cb=20130113080255&path-prefix=bloons")
        pop_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
        await interaction.response.send_message(embed=pop_embed, view=view)
        page = 0
    if bloon == "lead":
        view = PopButtons("lead", 0)
        desc = pops.lead0
        pop_embed = discord.Embed(color=0x706f6f, title="Lead Bloons [`/pop`]", description=desc)
        pop_embed.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/f/fd/BTD6Lead.png/revision/latest?cb=20190620031244&path-prefix=bloons")
        pop_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
        await interaction.response.send_message(embed=pop_embed, view=view)
    if bloon == "purple":
        view = PopButtons("purple", 0)
        desc = pops.purple0
        pop_embed = discord.Embed(color=0x8940ff, title="Purple Bloons [`/pop`]", description=desc)
        pop_embed.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/b/bd/BTD6Purple.png/revision/latest?cb=20180809061728&path-prefix=bloons")
        pop_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
        await interaction.response.send_message(embed=pop_embed, view=view)
    if bloon == "general":
        desc = pops.general
        member = interaction.guild.get_member(interaction.user.id)
        if member.mobile_status != discord.Status.offline:
            pop_embed = discord.Embed(color=0x2F3136)
            pop_embed.set_image(url="https://media.discordapp.net/attachments/1058750616500965438/1071426470255267941/image.png?width=601&height=580")
            pop_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            await interaction.response.send_message(embed=pop_embed)
        else:
            pop_embed = discord.Embed(color=0x2F3136, description=desc)
            pop_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            await interaction.response.send_message(embed=pop_embed)

@bot.tree.command(description="Find out which round you need to start saving up at for a certain amount of money.")
@app_commands.describe(money="The amount of money you need.", round="The round you need the money by.")
async def saveup(interaction: discord.Interaction, money: int, round: int):
    if round > 140:
        error_embed = discord.Embed(color=0x5865f2, title="Encountered Problem [`/saveup`]", description="Round parameter cannot exceed 140.")
        error_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
        await interaction.response.send_message(embed=error_embed)
    elif money > cash.medium[round - 1] - 650:
        error_embed = discord.Embed(color=0x5865f2, title="Encountered Problem [`/saveup`]", description="Money parameter cannot exceed maximum cash earned by round.")
        error_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
        await interaction.response.send_message(embed=error_embed)
    else:
        cash_total = cash.medium[round - 1] - 650
        req = cash_total - money
        medium_array = np.array(cash.medium)
        mask = (medium_array >= req)
        final = np.flatnonzero(mask)[0]
        save_embed = discord.Embed(color=0xffd04f, title="Result [`/saveup`]", description=f"To get {money} by round {round}, start saving up from **round {final}**.\n\nExpression:\n> *total = money obtained until round*\n> *required = total - money needed*\n> *round = minimum round to the required amount*")
        save_embed.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/2/23/Money_icon.png/revision/latest?cb=20210727151424&path-prefix=bloons")
        save_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
        save_embed.set_footer(text="ⓘ does not factor in external farming or any money you already have")
        await interaction.response.send_message(embed=save_embed)

@bot.tree.command(description="Check base and buffed stats of various components of the VTSG.")
@app_commands.describe(attack="Attack to display information about.")
async def vtsg(interaction: discord.Interaction, attack: Literal["main beam", "sun avatars", "spectres", "glaives", "blades", "homing missiles", "magical homing shots"]):
    if attack == "main beam":
        vtsg_embed = discord.Embed(color=0x3E3F7C, title="VTSG Main Beam [`/vtsg`]")
        vtsg_embed.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/0/00/555-SuperMonkey.png/revision/latest/scale-to-width-down/332?cb=20190522011421&path-prefix=bloons")
        vtsg_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
        vtsg_embed.add_field(name="Base Stats", value="> 50 damage | 0.06 attack cd | 833 base dps", inline=False)
        vtsg_embed.add_field(name="Buffed By", value="> AMD | P-Brew | OC | U-boost | Flagship | Jdrums\n> Blood Sacrifice | Homeland | Support Temple | Debuffs", inline=False)
        vtsg_embed.add_field(name="Buffed Damage", value="> 50 + 1 + 1 + 2 + 12 = 66", inline=False)
        vtsg_embed.add_field(name="Buffed Cooldown", value="> 0.06 * (0.85^3) * (0.81) * (0.36) * (0.5^2) = 0.002686", inline=False)
        vtsg_embed.add_field(name="Total Buffed DPS", value="> 66/0.002686 = 24570 ~ **24.6k**", inline=False)
        vtsg_embed.set_footer(text="ⓘ single target only; data from LordVex75")
        await interaction.response.send_message(embed=vtsg_embed)
    elif attack == "sun avatars":
        vtsg_embed = discord.Embed(color=0x3E3F7C, title="Vengeful Sun Avatars [`/vtsg`]")
        vtsg_embed.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/e/e7/555-SunAvatarTurret.png/revision/latest/scale-to-width-down/180?cb=20190522011449&path-prefix=bloons")
        vtsg_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
        vtsg_embed.add_field(name="Base Stats", value="> 29 damage | 0.03 attack cd | 3 projectiles | 6 savatars | 17400 base dps", inline=False)
        vtsg_embed.add_field(name="Buffed By", value="> Flagship | Jdrums\n> Blood Sacrifice | Homeland | Support Temple | Support VTSG | Debuffs", inline=False)
        vtsg_embed.add_field(name="Buffed Damage", value="> 29 + 2 + 2 + 12 = 45", inline=False)
        vtsg_embed.add_field(name="Buffed Cooldown", value="> 0.03 * (0.85^2) * (0.81^2) * (0.5^2) = 0.003555", inline=False)
        vtsg_embed.add_field(name="Total Buffed DPS", value="> 3 * 6 * 45/0.003555 = 227832.6 ~ **227.8k**", inline=False)
        vtsg_embed.set_footer(text="ⓘ single target only; data from LordVex75")
        await interaction.response.send_message(embed=vtsg_embed)
    elif attack == "spectres":
        vtsg_embed = discord.Embed(color=0x3E3F7C, title="Vengeful Spectres [`/vtsg`]")
        vtsg_embed.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/3/37/Vengeful_Spectre.png/revision/latest/scale-to-width-down/350?cb=20210719093633&path-prefix=bloons")
        vtsg_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
        vtsg_embed.add_field(name="Base Stats", value="> 30 dart damage | 20 bomb damage | 0.3 attack cd | 4 spectres | 667 base dps", inline=False)
        vtsg_embed.add_field(name="Buffed By", value="> OC | U-boost | Flagship | Jdrums\n> Blood Sacrifice | Homeland | Support Temple | Support VTSG | Debuffs", inline=False)
        vtsg_embed.add_field(name="Buffed Damage", value="> 30 + 2 + 2 + 12 = 46; 20 + 2 + 2 = 12 = 36; essentially 82", inline=False)
        vtsg_embed.add_field(name="Buffed Cooldown", value="> 0.3 * (0.85^2) * (0.81) * (0.36) * (0.5^2) = 0.0158", inline=False)
        vtsg_embed.add_field(name="Total Buffed DPS", value="> 4 * 82/0.0158 = 20759 ~ **20.8k**", inline=False)
        vtsg_embed.set_footer(text="ⓘ single target only; data from LordVex75")
        await interaction.response.send_message(embed=vtsg_embed)
    elif attack == "glaives":
        vtsg_embed = discord.Embed(color=0x3E3F7C, title="VTSG Glaives [`/vtsg`]")
        vtsg_embed.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/4/4d/GoldenGlaive555.png/revision/latest?cb=20200626011629&path-prefix=bloons")
        vtsg_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
        vtsg_embed.add_field(name="Base Stats", value="> 60 damage | 0.5 attack cd | 2 glaives | 240 base dps", inline=False)
        vtsg_embed.add_field(name="Buffed By", value="> AMD | P-Brew | OC | U-boost | Flagship | Jdrums\n> Blood Sacrifice | Homeland | Support Temple | Debuffs", inline=False)
        vtsg_embed.add_field(name="Buffed Damage", value="> 60 + 1 + 1 + 2 + 12 = 76", inline=False)
        vtsg_embed.add_field(name="Buffed Cooldown", value="> 0.5 * (0.85^3) * (0.81) * (0.36) * (0.5^2) = 0.02238", inline=False)
        vtsg_embed.add_field(name="Total Buffed DPS", value="> 2 * 76/0.02238 = 6790.3 ~ **6.8k**", inline=False)
        vtsg_embed.set_footer(text="ⓘ single target only; data from LordVex75")
        await interaction.response.send_message(embed=vtsg_embed)
    elif attack == "blades":
        vtsg_embed = discord.Embed(color=0x3E3F7C, title="VTSG Blades [`/vtsg`]")
        vtsg_embed.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/0/0c/GoldenBlade555.png/revision/latest?cb=20200626011628&path-prefix=bloons")
        vtsg_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
        vtsg_embed.add_field(name="Base Stats", value="> 50 damage | 1.5 attack cd | 16 blades | 533 base dps", inline=False)
        vtsg_embed.add_field(name="Buffed By", value="> AMD | P-Brew | OC | U-boost | Flagship | Jdrums\n> Blood Sacrifice | Homeland | Support Temple | Debuffs", inline=False)
        vtsg_embed.add_field(name="Buffed Damage", value="> 50 + 1 + 1 + 2 + 12 = 66", inline=False)
        vtsg_embed.add_field(name="Buffed Cooldown", value="> 1.5 * (0.85^3) * (0.81) * (0.36) * (0.5^2) = 0.06715", inline=False)
        vtsg_embed.add_field(name="Total Buffed DPS", value="> 16 * 66/0.06715 = 15726 ~ **15.7k** (~ 982 per blade)", inline=False)
        vtsg_embed.set_footer(text="ⓘ single target only; data from LordVex75")
        await interaction.response.send_message(embed=vtsg_embed)
    elif attack == "homing missiles":
        vtsg_embed = discord.Embed(color=0x3E3F7C, title="VTSG Homing Missiles [`/vtsg`]")
        vtsg_embed.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/c/cc/GoldenHomingMissile555.png/revision/latest?cb=20200626011630&path-prefix=bloons")
        vtsg_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
        vtsg_embed.add_field(name="Base Stats", value="> 150 damage (148 + 2 MOAB damage) | 1 attack cd | 2 missiles | 300 base dps", inline=False)
        vtsg_embed.add_field(name="Buffed By", value="> AMD | P-Brew | OC | U-boost | Flagship | Jdrums\n> Blood Sacrifice | Homeland | Support Temple | Debuffs", inline=False)
        vtsg_embed.add_field(name="Buffed Damage", value="> 150 + 1 + 1 + 2 + 12 = 166", inline=False)
        vtsg_embed.add_field(name="Buffed Cooldown", value="> 1 * (0.85^3) * (0.81) * (0.36) * (0.5^2) = 0.04477", inline=False)
        vtsg_embed.add_field(name="Total Buffed DPS", value="> 2 * 166/0.04477 = 7415.68 ~ **7.4k**", inline=False)
        vtsg_embed.set_footer(text="ⓘ single target only; data from LordVex75")
        await interaction.response.send_message(embed=vtsg_embed)
    elif attack == "magical homing shots":
        vtsg_embed = discord.Embed(color=0x3E3F7C, title="VTSG Magical Shots [`/vtsg`]")
        vtsg_embed.set_thumbnail(url="https://media.discordapp.net/attachments/936921170119381022/1072117994127364136/image.png")
        vtsg_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
        vtsg_embed.add_field(name="Base Stats", value="> 70 damage | 2 attack cd | 12 shots | 420 base dps", inline=False)
        vtsg_embed.add_field(name="Buffed By", value="> AMD | P-Brew | OC | U-boost | Flagship | Jdrums\n> Blood Sacrifice | Homeland | Support Temple | Debuffs", inline=False)
        vtsg_embed.add_field(name="Buffed Damage", value="> 70 + 1 + 1 + 2 + 12 = 86", inline=False)
        vtsg_embed.add_field(name="Buffed Cooldown", value="> 2 * (0.85^3) * (0.81) * (0.36) * (0.5^2) = 0.08954", inline=False)
        vtsg_embed.add_field(name="Total Buffed DPS", value="> 12 * 86/0.08954 = 11525 ~ **11.5k**", inline=False)
        vtsg_embed.set_footer(text="ⓘ single target only; data from LordVex75")
        await interaction.response.send_message(embed=vtsg_embed)

bot.run(token)
