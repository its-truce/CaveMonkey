import discord
from discord.ext import commands
from discord import app_commands
from typing import Literal 
import info.cash as cash
import numpy as np

class SaveUp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description="Find out which round you need to start saving up at for a certain amount of money.")
    @app_commands.describe(money="The amount of money you need.", round="The round you need the money by.", difficulty="The difficulty you're playing at.")
    async def saveup(self, interaction: discord.Interaction, money: int, round: int, difficulty: Literal["easy/medium", "hard", "impoppable/chimps"] = "easy/medium"):
        if round > 140:
            error_embed = discord.Embed(color=0x5865f2, title="Encountered Problem [`/saveup`]", description="Round parameter cannot exceed 140.")
            error_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            await interaction.response.send_message(embed=error_embed)
        if round == 0:
            error_embed = discord.Embed(color=0x5865f2, title="Encountered Problem [`/saveup`]", description="Round parameter cannot be 0.")
            error_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            await interaction.response.send_message(embed=error_embed)
        if money == 0:
            error_embed = discord.Embed(color=0x5865f2, title="Encountered Problem [`/saveup`]", description="Money parameter cannot be 0.")
            error_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            await interaction.response.send_message(embed=error_embed)                
        elif difficulty == "easy/medium":
            if money > cash.medium[round - 1]:
                error_embed = discord.Embed(color=0x5865f2, title="Encountered Problem [`/saveup`]", description="Money parameter cannot exceed maximum cash earned by round.")
                error_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                await interaction.response.send_message(embed=error_embed)
            else:
                cash_total = cash.medium[round - 1]
                req = cash_total - money
                medium_array = np.array(cash.medium)
                mask = (medium_array >= req)
                final = np.flatnonzero(mask)[0]
                save_embed = discord.Embed(color=0xffd04f, title="Result [`/saveup`]", description=f"To get {money} by round {round}, start saving up from **round {final}**.\n\nExpression:\n> *total = money obtained until round*\n> *required = total - money needed*\n> *round = minimum round to the required amount*")
                save_embed.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/2/23/Money_icon.png/revision/latest?cb=20210727151424&path-prefix=bloons")
                save_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                save_embed.set_footer(text="ⓘ does not factor in external farming or any money you already have")
                await interaction.response.send_message(embed=save_embed)
        elif difficulty == "hard":
            if money > cash.hard[round - 1]:
                error_embed = discord.Embed(color=0x5865f2, title="Encountered Problem [`/saveup`]", description="Money parameter cannot exceed maximum cash earned by round.")
                error_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                await interaction.response.send_message(embed=error_embed)
            else:
                cash_total = cash.hard[round - 1]
                req = cash_total - money
                hard_array = np.array(cash.hard)
                mask = (hard_array >= req)
                final = np.flatnonzero(mask)[0]
                save_embed = discord.Embed(color=0xffd04f, title="Result [`/saveup`]", description=f"To get {money} by round {round}, start saving up from **round {final}**.\n\nExpression:\n> *total = money obtained until round*\n> *required = total - money needed*\n> *round = minimum round to the required amount*")
                save_embed.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/2/23/Money_icon.png/revision/latest?cb=20210727151424&path-prefix=bloons")
                save_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                save_embed.set_footer(text="ⓘ does not factor in external farming or any money you already have")
                await interaction.response.send_message(embed=save_embed)
        elif difficulty == "impoppable/chimps":
            if money > cash.impoppable[round - 1]:
                error_embed = discord.Embed(color=0x5865f2, title="Encountered Problem [`/saveup`]", description="Money parameter cannot exceed maximum cash earned by round.")
                error_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                await interaction.response.send_message(embed=error_embed)
            else:
                cash_total = cash.impoppable[round - 1]
                req = cash_total - money
                impoppable_array = np.array(cash.impoppable)
                mask = (impoppable_array >= req)
                final = np.flatnonzero(mask)[0]
                save_embed = discord.Embed(color=0xffd04f, title="Result [`/saveup`]", description=f"To get {money} by round {round}, start saving up from **round {final}**.\n\nExpression:\n> *total = money obtained until round*\n> *required = total - money needed*\n> *round = minimum round to the required amount*")
                save_embed.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/2/23/Money_icon.png/revision/latest?cb=20210727151424&path-prefix=bloons")
                save_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                save_embed.set_footer(text="ⓘ does not factor in external farming or any money you already have")
                await interaction.response.send_message(embed=save_embed)

async def setup(bot):
    await bot.add_cog(SaveUp(bot))