import discord
from discord.ext import commands
from discord import app_commands
from colorthief import ColorThief
from io import BytesIO
import sys
from urllib.request import urlopen
import info.nkapi as nkapi
import aiohttp

class PlayerDropdown(discord.ui.Select):
    def __init__(self, color, id):
        self.color = color
        self.id = id
        options = [
            discord.SelectOption(label="Main Info", description="Displays general information about the player."),
            discord.SelectOption(label="Bloons Popped", description="Displays information about bloons popped by the player"),
            discord.SelectOption(label="Medals Singleplayer", description="Displays the player's singleplayer medals.")
        ]
        super().__init__(placeholder="Choose what to display.",min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        URL = "https://data.ninjakiwi.com"
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{URL}/btd6/users/{self.id}") as r:
                jsonr = await r.json()
        if self.values[0] == "Main Info":
            uname = jsonr["body"]["displayName"]
            rank = str(jsonr["body"]["rank"])
            veteran = str(jsonr["body"]["veteranRank"])
            most_experienced = jsonr["body"]["mostExperiencedMonkey"]
            most_experienced = nkapi.emotify(most_experienced)
            highest_round = str(jsonr["body"]["highestRound"])
            achievements = str(jsonr["body"]["achievements"])
            followers = str(jsonr["body"]["followers"])
            avatar = jsonr["body"]["avatarURL"]
            player_embed = discord.Embed(color=self.color, title=f"{uname} [`/player`]")
            player_embed.set_thumbnail(url=avatar)
            player_embed.add_field(name="Rank", value=f"<:rank:1072789620883984414> {rank}", inline=False)
            player_embed.add_field(name="Veteran Rank", value=f"<:veteran:1072789996047704144> {veteran}", inline=False)
            player_embed.add_field(name="Most Experienced Monkey", value=most_experienced, inline=False)
            player_embed.add_field(name="Highest Round", value=f"<:red:1072864121088909322> {highest_round}", inline=False)
            player_embed.add_field(name="Followers", value=f"<:dartface:1072900168275468318> {followers}", inline=False)
            player_embed.add_field(name="Achievements", value=f"<:achievements:1073259163653787728> {achievements}", inline=False)
            player_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            await interaction.message.edit(embed=player_embed)
        if self.values[0] == "Bloons Popped":
            uname = jsonr["body"]["displayName"]
            avatar = jsonr["body"]["avatarURL"]
            bloon = str(jsonr["body"]["bloonsPopped"]["bloonsPopped"])
            camo = str(jsonr["body"]["bloonsPopped"]["camosPopped"])
            lead = str(jsonr["body"]["bloonsPopped"]["leadsPopped"])
            purple = str(jsonr["body"]["bloonsPopped"]["purplesPopped"])
            golden = str(jsonr["body"]["bloonsPopped"]["goldenBloonsPopped"])
            bad = str(jsonr["body"]["bloonsPopped"]["badsPopped"])
            zomg = str(jsonr["body"]["bloonsPopped"]["zomgsPopped"])
            bfb = str(jsonr["body"]["bloonsPopped"]["bfbsPopped"])
            moab = str(jsonr["body"]["bloonsPopped"]["moabsPopped"])
            bloons_embed = discord.Embed(color=self.color, title=f"{uname} [`/player`]")
            bloons_embed.set_thumbnail(url=avatar)
            bloons_embed.add_field(name="Bloons Popped", value=f"<:red:1072864121088909322> {bloon}", inline=False)
            bloons_embed.add_field(name="Camos Popped", value=f"<:camo:1073604591289114665> {camo}", inline=False)
            bloons_embed.add_field(name="Leads Popped", value=f"<:lead:1073604558036680835> {lead}", inline=False)
            bloons_embed.add_field(name="Purples Popped", value=f"<:purple:1073604467968184363> {purple}", inline=False)
            bloons_embed.add_field(name="Golden Bloons Popped", value=f"<:golden:1073604519994335294> {golden}", inline=False)
            bloons_embed.add_field(name="MOABs Popped", value=f"<:moab:1073604458359046214> {moab}", inline=False)
            bloons_embed.add_field(name="BFBs Popped", value=f"<:bfb:1073604497047298148> {bfb}", inline=False)
            bloons_embed.add_field(name="ZOMGs Popped", value=f"<:zomg:1073604448665993376> {zomg}", inline=False)
            bloons_embed.add_field(name="BADs Popped", value=f"<:bad:1073604438876487860> {bad}", inline=False)
            bloons_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            await interaction.message.edit(embed=bloons_embed)


class PlayerView(discord.ui.View):
    def __init__(self, color, id):
        super().__init__()
        self.color = color
        self.id = id
        self.add_item(PlayerDropdown(self.color, self.id))


class PlayerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description="Check information about a player using their ID.")
    @app_commands.describe(id = "The player ID.")
    async def player(self, interaction: discord.Interaction, id: str):
        await interaction.response.defer()
        URL = "https://data.ninjakiwi.com"
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{URL}/btd6/users/{id}") as r:
                jsonr = await r.json()
        if jsonr["error"] == "Invalid user ID":
            error_embed = discord.Embed(color=0x5865f2, title="Encountered Problem [`/player`]", description="ID parameter was invalid. Please reuse the command and set the `tutorial` parameter to True to get a tutorial on fetching IDs.")
            error_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            await interaction.followup.send(embed=error_embed)
        else:
            uname = jsonr["body"]["displayName"]
            rank = str(jsonr["body"]["rank"])
            veteran = str(jsonr["body"]["veteranRank"])
            most_experienced = jsonr["body"]["mostExperiencedMonkey"]
            most_experienced = nkapi.emotify(most_experienced)
            highest_round = str(jsonr["body"]["highestRound"])
            achievements = str(jsonr["body"]["achievements"])
            followers = str(jsonr["body"]["followers"])
            avatar = jsonr["body"]["avatarURL"]
            f = BytesIO(urlopen(avatar).read())
            dominant = ColorThief(f).get_color(quality=1) 
            player_embed = discord.Embed(color=discord.Color.from_rgb(r=dominant[0], g=dominant[1], b=dominant[2]), title=f"{uname} [`/player`]")
            player_embed.set_thumbnail(url=avatar)
            player_embed.add_field(name="Rank", value=f"<:rank:1072789620883984414> {rank}", inline=False)
            player_embed.add_field(name="Veteran Rank", value=f"<:veteran:1072789996047704144> {veteran}", inline=False)
            player_embed.add_field(name="Most Experienced Monkey", value=most_experienced, inline=False)
            player_embed.add_field(name="Highest Round", value=f"<:red:1072864121088909322> {highest_round}", inline=False)
            player_embed.add_field(name="Followers", value=f"<:dartface:1072900168275468318> {followers}", inline=False)
            player_embed.add_field(name="Achievements", value=f"<:achievements:1073259163653787728> {achievements}", inline=False)
            view = PlayerView(color=discord.Color.from_rgb(r=dominant[0], g=dominant[1], b=dominant[2]), id=id)
            player_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            await interaction.followup.send(embed=player_embed, view=view)

async def setup(bot):
    await bot.add_cog(PlayerInfo(bot))