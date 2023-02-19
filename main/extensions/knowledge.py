import discord
from discord.ext import commands
from discord import app_commands
from typing import Literal
import info.mk as mk

class MonkeyKnowledge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(description="Check which Monkey Knowledge points affect a tower.")
    @app_commands.describe(tower="The tower to check MK points for.")
    async def mk(interaction: discord.Interaction, tower: Literal["dart monkey", "boomerang monkey", "bomb shooter", "tack shooter", "ice monkey", "glue gunner", "sniper monkey"]):
        if tower == "dart monkey":
            desc = mk.dart
            mk_embed = discord.Embed(color=0xAE5D22, title="Dart Monkey [`/mk`]", description=desc)
            mk_embed.set_thumbnail("https://static.wikia.nocookie.net/b__/images/b/b2/000-DartMonkey.png/revision/latest/scale-to-width-down/350?cb=20190522014750&path-prefix=bloons")
            mk_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            interaction.response.send_message(embed=mk_embed)
        if tower == "boomerang monkey":
            desc = mk.boomerang
            mk_embed = discord.Embed(color=0xFFD200, title="Boomerang Monkey [`/mk`]", description=desc)
            mk_embed.set_thumbnail("https://static.wikia.nocookie.net/b__/images/5/51/BTD6_Boomerang_Monkey.png/revision/latest/scale-to-width-down/350?cb=20180616145853&path-prefix=bloons")
            mk_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            interaction.response.send_message(embed=mk_embed)
        if tower == "bomb shooter":
            desc = mk.bomb
            mk_embed = discord.Embed(color=0x434564, title="Bomb Shooter [`/mk`]", description=desc)
            mk_embed.set_thumbnail("https://static.wikia.nocookie.net/b__/images/e/e1/Bomb_Shooter.png/revision/latest/scale-to-width-down/350?cb=20180616145810&path-prefix=bloons")
            mk_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            interaction.response.send_message(embed=mk_embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(MonkeyKnowledge(bot))