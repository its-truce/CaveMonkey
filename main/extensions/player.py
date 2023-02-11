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
            discord.SelectOption(label="Main Info", description="Displays general information about the player.", default=True),
            discord.SelectOption(label="Bloons Popped", description="Displays information about bloons popped by the player"),
            discord.SelectOption(label="Medals Singleplayer", description="Displays the player's singleplayer medals.")
        ]
        super().__init__(min_values=1, max_values=1, options=options)

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
            herolist = [jsonr["body"]["heroesPlaced"]["AdmiralBrickell"], jsonr["body"]["heroesPlaced"]["Adora"], jsonr["body"]["heroesPlaced"]["Benjamin"], 
                jsonr["body"]["heroesPlaced"]["Etienne"], jsonr["body"]["heroesPlaced"]["Geraldo"], jsonr["body"]["heroesPlaced"]["Gwendolin"], 
                jsonr["body"]["heroesPlaced"]["ObynGreenfoot"], jsonr["body"]["heroesPlaced"]["PatFusty"], jsonr["body"]["heroesPlaced"]["Psi"], 
                jsonr["body"]["heroesPlaced"]["Quincy"], jsonr["body"]["heroesPlaced"]["Sauda"], jsonr["body"]["heroesPlaced"]["StrikerJones"]]
            most_used_hero = herolist.index(max(herolist))
            most_used_hero = nkapi.herofy(most_used_hero)
            highest_round = str(jsonr["body"]["highestRound"])
            achievements = str(jsonr["body"]["achievements"])
            followers = str(jsonr["body"]["followers"])
            avatar = jsonr["body"]["avatarURL"]
            player_embed = discord.Embed(color=self.color, title=f"{uname} [`/player`]")
            player_embed.set_thumbnail(url=avatar)
            player_embed.add_field(name="Rank", value=f"<:rank:1072789620883984414> {rank}", inline=False)
            player_embed.add_field(name="Veteran Rank", value=f"<:veteran:1072789996047704144> {veteran}", inline=False)
            player_embed.add_field(name="Most Experienced Monkey", value=most_experienced, inline=False)
            player_embed.add_field(name="Most Used Hero", value=most_used_hero, inline=False)
            player_embed.add_field(name="Highest Round", value=f"<:red:1072864121088909322> {highest_round}", inline=False)
            player_embed.add_field(name="Followers", value=f"<:dartface:1072900168275468318> {followers}", inline=False)
            player_embed.add_field(name="Achievements", value=f"<:achievements:1073259163653787728> {achievements}", inline=False)
            player_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            self.options[1].default = False
            self.options[2].default = False
            self.options[0].default = True
            await interaction.edit_original_response(embed=player_embed, view=self.view)
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
            self.options[0].default = False
            self.options[2].default = False
            self.options[1].default = True
            await interaction.edit_original_response(embed=bloons_embed, view=self.view)
        if self.values[0] == "Medals Singleplayer":
            uname = jsonr["body"]["displayName"]
            avatar = jsonr["body"]["avatarURL"]
            easy = str(jsonr["body"]["_medalsSinglePlayer"]["Easy"])
            medium = str(jsonr["body"]["_medalsSinglePlayer"]["Medium"])
            hard = str(jsonr["body"]["_medalsSinglePlayer"]["Hard"])
            primary = str(jsonr["body"]["_medalsSinglePlayer"]["PrimaryOnly"])
            deflation = str(jsonr["body"]["_medalsSinglePlayer"]["Deflation"])
            military = str(jsonr["body"]["_medalsSinglePlayer"]["MilitaryOnly"])
            apopalypse = str(jsonr["body"]["_medalsSinglePlayer"]["Apopalypse"])
            reverse = str(jsonr["body"]["_medalsSinglePlayer"]["Reverse"])
            magic = str(jsonr["body"]["_medalsSinglePlayer"]["MagicOnly"])
            halfcash = str(jsonr["body"]["_medalsSinglePlayer"]["HalfCash"])
            doublehp = str(jsonr["body"]["_medalsSinglePlayer"]["DoubleMoabHealth"])
            abr = str(jsonr["body"]["_medalsSinglePlayer"]["AlternateBloonsRounds"])
            impoppable = str(jsonr["body"]["_medalsSinglePlayer"]["Impoppable"])
            chimpsblack = str(jsonr["body"]["_medalsSinglePlayer"]["CHIMPS-BLACK"])
            chimpsred = str(jsonr["body"]["_medalsSinglePlayer"]["Clicks"] - jsonr["body"]["_medalsSinglePlayer"]["CHIMPS-BLACK"])
            medals_embed = discord.Embed(color=self.color, title=f"{uname} [`/player`]")
            medals_embed.set_thumbnail(url=avatar)
            medals_embed.add_field(name="Easy", value=f"<:easy:1073876236507562024> {easy}", inline=False)
            medals_embed.add_field(name="Primary Only", value=f"<:primary:1073876277263614063> {primary}", inline=False)
            medals_embed.add_field(name="Deflation", value=f"<:deflation:1073876355307012106> {deflation}", inline=False)
            medals_embed.add_field(name="Medium", value=f"<:medium:1073876475578699816> {medium}", inline=False)
            medals_embed.add_field(name="Military Only", value=f"<:military:1073876516888399943> {military}", inline=False)
            medals_embed.add_field(name="Reverse", value=f"<:reverse:1073876573003993179> {reverse}", inline=False)
            medals_embed.add_field(name="Apopalypse", value=f"<:apopalypse:1073876616926724108> {apopalypse}", inline=False)
            medals_embed.add_field(name="Hard", value=f"<:hard:1073872742153199646> {hard}", inline=False)
            medals_embed.add_field(name="Magic Only", value=f"<:magic:1073872652114083961> {magic}", inline=False)
            medals_embed.add_field(name="Alternate Bloons Rounds", value=f"<:abr:1073872586955567114> {abr}", inline=False)
            medals_embed.add_field(name="Double HP MOABs", value=f"<:doublehp:1073872543150243931> {doublehp}", inline=False)
            medals_embed.add_field(name="Half Cash", value=f"<:halfcash:1073872491560308837> {halfcash}", inline=False)
            medals_embed.add_field(name="Impoppable", value=f"<:impoppable:1073876417349173248> {impoppable}", inline=False)
            medals_embed.add_field(name="Red Chimps", value=f"<:redchimps:1073872376766398544> {chimpsred}", inline=False)
            medals_embed.add_field(name="Black Chimps", value=f"<:blackchimps:1073872329916026930> {chimpsblack}", inline=False)
            medals_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            self.options[0].default = False
            self.options[1].default = False
            self.options[2].default = True
            await interaction.edit_original_response(embed=medals_embed, view=self.view)

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
            herolist = [jsonr["body"]["heroesPlaced"]["AdmiralBrickell"], jsonr["body"]["heroesPlaced"]["Adora"], jsonr["body"]["heroesPlaced"]["Benjamin"], 
                jsonr["body"]["heroesPlaced"]["Etienne"], jsonr["body"]["heroesPlaced"]["Geraldo"], jsonr["body"]["heroesPlaced"]["Gwendolin"], 
                jsonr["body"]["heroesPlaced"]["ObynGreenfoot"], jsonr["body"]["heroesPlaced"]["PatFusty"], jsonr["body"]["heroesPlaced"]["Psi"], 
                jsonr["body"]["heroesPlaced"]["Quincy"], jsonr["body"]["heroesPlaced"]["Sauda"], jsonr["body"]["heroesPlaced"]["StrikerJones"]]
            most_used_hero = herolist.index(max(herolist))
            most_used_hero = nkapi.herofy(most_used_hero)
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
            player_embed.add_field(name="Most Used Hero", value=most_used_hero, inline=False)
            player_embed.add_field(name="Highest Round", value=f"<:red:1072864121088909322> {highest_round}", inline=False)
            player_embed.add_field(name="Followers", value=f"<:dartface:1072900168275468318> {followers}", inline=False)
            player_embed.add_field(name="Achievements", value=f"<:achievements:1073259163653787728> {achievements}", inline=False)
            view = PlayerView(color=discord.Color.from_rgb(r=dominant[0], g=dominant[1], b=dominant[2]), id=id)
            player_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            await interaction.followup.send(embed=player_embed, view=view)

async def setup(bot):
    await bot.add_cog(PlayerInfo(bot))
