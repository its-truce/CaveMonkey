import discord
from discord.ext import commands
from discord import app_commands
from colorthief import ColorThief
from io import BytesIO
import sys
from urllib.request import urlopen
import info.nkapi as nkapi
import aiohttp
import random
from sqlitedict import SqliteDict

saved_ids = SqliteDict("./saved_ids.sqlite")

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
                jsonr["body"]["heroesPlaced"]["Quincy"], jsonr["body"]["heroesPlaced"]["Sauda"], jsonr["body"]["heroesPlaced"]["StrikerJones"], 
                jsonr["body"]["heroesPlaced"]["Ezili"], jsonr["body"]["heroesPlaced"]["CaptainChurchill"]]
            most_used_hero = herolist.index(max(herolist))
            most_used_hero = nkapi.herofy(most_used_hero)
            highest_round = str(jsonr["body"]["highestRound"])
            achievements = str(jsonr["body"]["achievements"])
            followers = str(jsonr["body"]["followers"])
            avatar = jsonr["body"]["avatarURL"]
            player_embed = discord.Embed(color=self.color, title=f"{uname} [`/player info`]")
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
            bloons_embed = discord.Embed(color=self.color, title=f"{uname} [`/player info`]")
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
            medals_embed = discord.Embed(color=self.color, title=f"{uname} [`/player info`]")
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
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ctx_menu = app_commands.ContextMenu(name="View BTD6 Profile", callback=self.info)
        self.bot.tree.add_command(self.ctx_menu)

    player_group = app_commands.Group(name="player", description="Group for viewing information about a player.")

    @player_group.command(description="Check information about a player using their ID.")
    @app_commands.describe(id = "The player ID.")
    async def info(self, interaction: discord.Interaction, id: str = None):
        await interaction.response.defer()
        if id is not None:
            URL = "https://data.ninjakiwi.com"
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{URL}/btd6/users/{id}") as r:
                    jsonr = await r.json()
            if jsonr["error"] == "Invalid user ID":
                error_embed = discord.Embed(color=0x5865f2, title="Encountered Problem [`/player info`]", description="ID parameter was invalid. Please use the "
                "`/player tutorial` command to get your ID.")
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
                    jsonr["body"]["heroesPlaced"]["Quincy"], jsonr["body"]["heroesPlaced"]["Sauda"], jsonr["body"]["heroesPlaced"]["StrikerJones"], 
                    jsonr["body"]["heroesPlaced"]["Ezili"], jsonr["body"]["heroesPlaced"]["CaptainChurchill"]]
                most_used_hero = herolist.index(max(herolist))
                most_used_hero = nkapi.herofy(most_used_hero)
                highest_round = str(jsonr["body"]["highestRound"])
                achievements = str(jsonr["body"]["achievements"])
                followers = str(jsonr["body"]["followers"])
                avatar = jsonr["body"]["avatarURL"]
                f = BytesIO(urlopen(avatar).read())
                dominant = ColorThief(f).get_color(quality=1) 
                player_embed = discord.Embed(color=discord.Color.from_rgb(r=dominant[0], g=dominant[1], b=dominant[2]), title=f"{uname} [`/player info`]")
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
        elif interaction.user.id not in saved_ids:
            error_embed = discord.Embed(color=0x5865f2, title="Encountered Problem [`/player info`]", description="You don't have an ID saved. You can save one with `/player save`.")
            error_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            await interaction.followup.send(embed=error_embed)
        else:
            URL = "https://data.ninjakiwi.com"
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{URL}/btd6/users/{saved_ids[interaction.user.id]}") as r:
                    jsonr = await r.json()
            if jsonr["error"] == "Invalid user ID":
                error_embed = discord.Embed(color=0x5865f2, title="Encountered Problem [`/player save`]", description="ID parameter was invalid. Please use the "
                "`/player tutorial` command to get your ID.")
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
                    jsonr["body"]["heroesPlaced"]["Quincy"], jsonr["body"]["heroesPlaced"]["Sauda"], jsonr["body"]["heroesPlaced"]["StrikerJones"], 
                    jsonr["body"]["heroesPlaced"]["Ezili"], jsonr["body"]["heroesPlaced"]["CaptainChurchill"]]
                most_used_hero = herolist.index(max(herolist))
                most_used_hero = nkapi.herofy(most_used_hero)
                highest_round = str(jsonr["body"]["highestRound"])
                achievements = str(jsonr["body"]["achievements"])
                followers = str(jsonr["body"]["followers"])
                avatar = jsonr["body"]["avatarURL"]
                f = BytesIO(urlopen(avatar).read())
                dominant = ColorThief(f).get_color(quality=1) 
                player_embed = discord.Embed(color=discord.Color.from_rgb(r=dominant[0], g=dominant[1], b=dominant[2]), title=f"{uname} [`/player info`]")
                player_embed.set_thumbnail(url=avatar)
                player_embed.add_field(name="Rank", value=f"<:rank:1072789620883984414> {rank}", inline=False)
                player_embed.add_field(name="Veteran Rank", value=f"<:veteran:1072789996047704144> {veteran}", inline=False)
                player_embed.add_field(name="Most Experienced Monkey", value=most_experienced, inline=False)
                player_embed.add_field(name="Most Used Hero", value=most_used_hero, inline=False)
                player_embed.add_field(name="Highest Round", value=f"<:red:1072864121088909322> {highest_round}", inline=False)
                player_embed.add_field(name="Followers", value=f"<:dartface:1072900168275468318> {followers}", inline=False)
                player_embed.add_field(name="Achievements", value=f"<:achievements:1073259163653787728> {achievements}", inline=False)
                view = PlayerView(color=discord.Color.from_rgb(r=dominant[0], g=dominant[1], b=dominant[2]), id=saved_ids[interaction.user.id])
                player_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                await interaction.followup.send(embed=player_embed, view=view)            


    @player_group.command(description="Fetches your player ID from a challenge ID.")
    @app_commands.describe(code = "The challenge code.")
    async def fetch(self, interaction: discord.Interaction, code: str):
        await interaction.response.defer()
        URL = "https://data.ninjakiwi.com"
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{URL}/btd6/challenges/challenge/{id}") as r:
                jsonr = await r.json()
        if jsonr["error"] == "No challenge with that ID exists":
            error_embed = discord.Embed(color=0x5865f2, title="Encountered Problem [`/player fetch`]", description="Code parameter was invalid. Use `player tutorial` to get a tutorial on how to get a challenge ID.")
            error_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            error_embed.set_footer(text="ⓘ ninja kiwi API might be having issues if your code is valid.")
            await interaction.followup.send(embed=error_embed)
        else:
            uid = jsonr["body"]["creator"]
            uid = uid.replace("https://data.ninjakiwi.com/btd6/users/", "")
            fetch_embed = discord.Embed(color=0x5865f2, title="Player ID [`/player fetch`]")
            fetch_embed.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/8/86/CreateChallengeIcon.png/revision/latest?cb=20200601042401&path-prefix=bloons")
            fetch_embed.add_field(name="Challenge ID", value=id, inline=False)
            fetch_embed.add_field(name="Player ID", value=uid, inline=False)
            fetch_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            await interaction.followup.send(embed=fetch_embed)

    @player_group.command(description="Sends a tutorial on how to get your player ID.")
    async def tutorial(self, interaction: discord.Interaction):
        tutorial_embed = discord.Embed(color=0x5865f2, title="Finding Your Player ID [`/tutorial player`]")
        tutorial_embed.set_thumbnail(url="https://static.wikia.nocookie.net/b__/images/9/9d/EnterCodeIcon.png/revision/latest?cb=20200706034206&path-prefix=bloons")
        tutorial_embed.set_image(url="https://static.wikia.nocookie.net/b__/images/d/d0/ChallengeBrowserExample.png/revision/latest/scale-to-width-down/1000?cb=20210107085929&path-prefix=bloons")
        tutorial_embed.add_field(name="Step 1", value="Click on the events monkey (the one with an exclamation mark over it) on the main menu of the game.", inline=False)
        tutorial_embed.add_field(name="Step 2", value="Scroll all the way down and open the challenge browser.", inline=False)
        tutorial_embed.add_field(name="Step 3", value="Click on the yellow CREATE button.", inline=False)
        tutorial_embed.add_field(name="Step 4", value="Modify the challenge as you wish and beat it. After this, submit the challenge.", inline=False)
        tutorial_embed.add_field(name="Step 5", value="You'll get a code that looks something like ZMDSRCO. Copy it and enter it into the `/player fetch` command to get your player ID.", inline=False)
        await interaction.response.send_message(embed=tutorial_embed)
        
    @player_group.command(description="Saves your player ID so you can view your profile by using /player info.")
    @app_commands.describe(id = "The player ID.")
    async def save(self, interaction: discord.Interaction, id: str):
        await interaction.response.defer()
        URL = "https://data.ninjakiwi.com"
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{URL}/btd6/users/{id}") as r:
                jsonr = await r.json()
        if jsonr["error"] == "Invalid user ID":
            error_embed = discord.Embed(color=0x5865f2, title="Encountered Problem [`/player save`]", description="ID parameter was invalid. Please use the "
            "`/player tutorial` command to get your ID.")
            error_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            await interaction.followup.send(embed=error_embed)
        elif interaction.user.id in saved_ids:
            error_embed = discord.Embed(color=0x5865f2, title="Encountered Problem [`/player save`]", description="You already have a saved ID. You can delete it by using `/player delete`.")
            error_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            await interaction.followup.send(embed=error_embed)
        else:
            saved_ids[interaction.user.id] = id
            saved_ids.commit()
            save_embed = discord.Embed(color=0x5865f2, title="ID Saved [`/player save`]", description="Your ID has been saved. You can now use `/player info` to check "
            "your BTD6 profile.")
            save_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            await interaction.followup.send(embed=save_embed)

    @player_group.command(description="Deletes your saved player ID.")
    async def delete(self, interaction: discord.Interaction):
        if interaction.user.id not in saved_ids:
            error_embed = discord.Embed(color=0x5865f2, title="Encountered Problem [`/player delete`]", description="You don't have an ID saved. You can save one with `/player save`.")
            error_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            await interaction.response.send_message(embed=error_embed)
        else:
            del saved_ids[interaction.user.id]
            saved_ids.commit()
            save_embed = discord.Embed(color=0x5865f2, title="ID Deleted [`/player delete`]", description="Your ID has been deleted. You can now use `/player save` to "
            "save a new one.")
            save_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            await interaction.response.send_message(embed=save_embed)       

    async def info(self, interaction: discord.Interaction, member: discord.Member):
        await interaction.response.defer()
        if member.id not in saved_ids:
            error_embed = discord.Embed(color=0x5865f2, title="Encountered Problem [`Player Info`]", description=f"{member.display_name} does not have a saved ID! IDs can be "
            "saved using `/player save`.")
            error_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
            await interaction.followup.send(embed=error_embed)
        else:
            URL = "https://data.ninjakiwi.com"
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{URL}/btd6/users/{saved_ids[interaction.user.id]}") as r:
                    jsonr = await r.json()
            if jsonr["error"] == "Invalid user ID":
                error_embed = discord.Embed(color=0x5865f2, title="Encountered Problem [`Player Info`]", description="ID parameter was invalid. Please use the "
                "`/player tutorial` command to get your ID.")
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
                    jsonr["body"]["heroesPlaced"]["Quincy"], jsonr["body"]["heroesPlaced"]["Sauda"], jsonr["body"]["heroesPlaced"]["StrikerJones"], 
                    jsonr["body"]["heroesPlaced"]["Ezili"], jsonr["body"]["heroesPlaced"]["CaptainChurchill"]]
                most_used_hero = herolist.index(max(herolist))
                most_used_hero = nkapi.herofy(most_used_hero)
                highest_round = str(jsonr["body"]["highestRound"])
                achievements = str(jsonr["body"]["achievements"])
                followers = str(jsonr["body"]["followers"])
                avatar = jsonr["body"]["avatarURL"]
                f = BytesIO(urlopen(avatar).read())
                dominant = ColorThief(f).get_color(quality=1) 
                player_embed = discord.Embed(color=discord.Color.from_rgb(r=dominant[0], g=dominant[1], b=dominant[2]), title=f"{uname} [`Player Info`]")
                player_embed.set_thumbnail(url=avatar)
                player_embed.add_field(name="Rank", value=f"<:rank:1072789620883984414> {rank}", inline=False)
                player_embed.add_field(name="Veteran Rank", value=f"<:veteran:1072789996047704144> {veteran}", inline=False)
                player_embed.add_field(name="Most Experienced Monkey", value=most_experienced, inline=False)
                player_embed.add_field(name="Most Used Hero", value=most_used_hero, inline=False)
                player_embed.add_field(name="Highest Round", value=f"<:red:1072864121088909322> {highest_round}", inline=False)
                player_embed.add_field(name="Followers", value=f"<:dartface:1072900168275468318> {followers}", inline=False)
                player_embed.add_field(name="Achievements", value=f"<:achievements:1073259163653787728> {achievements}", inline=False)
                view = PlayerView(color=discord.Color.from_rgb(r=dominant[0], g=dominant[1], b=dominant[2]), id=saved_ids[interaction.user.id])
                player_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
                await interaction.followup.send(embed=player_embed, view=view)

    async def cog_unload(self):
        self.bot.tree.remove_command(self.info, type=self.info.type)


async def setup(bot: commands.Bot):
    await bot.add_cog(PlayerInfo(bot))
