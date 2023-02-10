import discord
from discord.ext import commands
from discord import app_commands
from typing import Literal 

class VTSG(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(description="Check base and buffed stats of various components of the VTSG.")
    @app_commands.describe( attack="Attack to display information about.")
    async def vtsg(self, interaction: discord.Interaction, attack: Literal["main beam", "sun avatars", "spectres", "glaives", "blades", "homing missiles", "magical homing shots"]):
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

async def setup(bot):
    await bot.add_cog(VTSG(bot))