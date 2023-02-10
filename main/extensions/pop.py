import discord
from discord.ext import commands
from discord import app_commands
from typing import Literal 
import info.pops as pops

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


class PopBloon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description="Check which towers can pop certain balloons.")
    @app_commands.describe(bloon="Type of bloon.")
    async def pop(self, interaction: discord.Interaction, bloon: Literal["camo", "lead", "purple", "general"]):
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

async def setup(bot):
    await bot.add_cog(PopBloon(bot))