import discord
from discord.ext import commands
from discord import app_commands
from typing import Literal 
import info.cash as cash
import numpy as np

class Income(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description="Find out which round you need to start saving up at for a certain amount of money.")
    @app_commands.describe(money="The amount of money you need.", round="The round you need the money by.", difficulty="The difficulty you're playing at.")
    async def saveup(self, interaction: discord.Interaction, money: app_commands.Range[int, 1], round: app_commands.Range[int, 1, 140], 
                difficulty: Literal["easy/medium", "hard", "impoppable/chimps"] = "easy/medium"):              
        if difficulty == "easy/medium":
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

    @app_commands.command(description="Find out which round you'll get a certain amount of money by.")
    @app_commands.describe(money="The amount of money you need.", round="The current round.", difficulty="The difficulty you're playing at.")
    async def saveby(self, interaction: discord.Interaction, money: app_commands.Range[int, 1], round: app_commands.Range[int, 1, 140], 
                difficulty: Literal["easy/medium", "hard", "impoppable/chimps"] = "easy/medium"):
            if difficulty == "easy/medium":
                try:
                    cash_total = cash.medium[round] + money
                    medium_array = np.array(cash.medium)
                    mask = (medium_array >= cash_total)
                    final = np.flatnonzero(mask)[0]
                    save_embed = discord.Embed(color=0xffd04f, title="Result [`/saveby`]", description=f"If you start saving up at {round}, you will get {money} by **round {final}**.\n\nExpression:\n> *total = money obtained by the end of round + money needed*\n> *round = minimum round to the required amount*")
                    save_embed.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/2/23/Money_icon.png/revision/latest?cb=20210727151424&path-prefix=bloons")
                    save_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                    save_embed.set_footer(text="ⓘ does not factor in external farming or any money you already have")
                    await interaction.response.send_message(embed=save_embed)
                except IndexError as e:
                    error_embed = discord.Embed(color=0x5865f2, title="Encountered Problem [`/saveby`]", description="Money parameter is not earned by round 140 or less. Please lower the value.")
                    error_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                    await interaction.response.send_message(embed=error_embed)
            elif difficulty == "hard":
                try:
                    cash_total = cash.hard[round] + money
                    hard_array = np.array(cash.hard)
                    mask = (hard_array >= cash_total)
                    final = np.flatnonzero(mask)[0]
                    save_embed = discord.Embed(color=0xffd04f, title="Result [`/saveby`]", description=f"If you start saving up at {round}, you will get {money} by **round {final}**.\n\nExpression:\n> *total = money obtained by the end of round + money needed*\n> *round = minimum round to the required amount*")
                    save_embed.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/2/23/Money_icon.png/revision/latest?cb=20210727151424&path-prefix=bloons")
                    save_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                    save_embed.set_footer(text="ⓘ does not factor in external farming or any money you already have")
                    await interaction.response.send_message(embed=save_embed)
                except IndexError as e:
                    error_embed = discord.Embed(color=0x5865f2, title="Encountered Problem [`/saveby`]", description="Money parameter is not earned by round 140 or less. Please lower the value.")
                    error_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                    await interaction.response.send_message(embed=error_embed)
            elif difficulty == "impoppable/chimps":
                try:
                    cash_total = cash.impoppable[round] + money
                    impoppable_array = np.array(cash.impoppable)
                    mask = (impoppable_array >= cash_total)
                    final = np.flatnonzero(mask)[0]
                    save_embed = discord.Embed(color=0xffd04f, title="Result [`/saveby`]", description=f"If you start saving up at {round}, you will get {money} by **round {final}**.\n\nExpression:\n> *total = money obtained by the end of round + money needed*\n> *round = minimum round to the required amount*")
                    save_embed.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/2/23/Money_icon.png/revision/latest?cb=20210727151424&path-prefix=bloons")
                    save_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                    save_embed.set_footer(text="ⓘ does not factor in external farming or any money you already have")
                    await interaction.response.send_message(embed=save_embed)
                except IndexError as e:
                    error_embed = discord.Embed(color=0x5865f2, title="Encountered Problem [`/saveby`]", description="Money parameter is not earned by round 140 or less. Please lower the value.")
                    error_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                    await interaction.response.send_message(embed=error_embed)


async def setup(bot):
    await bot.add_cog(Income(bot))
