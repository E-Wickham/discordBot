import discord
from discord import app_commands
from discord.ext import commands
from discord.utils import get
from NewColumn import *

##Subclassing out the client to allow for use of a variable to 
##Track if commands have been synced to Discord
##and avoid spamming Discord servers

MY_GUILD = discord.Object(id='BST GUILD ID')
AUTOROLE = "New Friend"

class BotClient(discord.Client):
    def __init__(self):
        ##Define Intents, might change once I have dev potal access to bot
        super().__init__(intents=discord.Intents.default()) 
        ##Define variable to track if commands are synced to Discord
        synced = False
        ##Define the Command tree for the client
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        await self.wait_until_ready()
        ##check if commands have been synced, sync if they havent, ignore otherwise.
        ##on_ready() can be called more than once, so we used synced variable to avoid spam
        if not self.synced:
            await tree.sync(guild=discord.Object(MY_GUILD))
            self.synced = True
        print("Bot Running")


##Initialize Bot
client = BotClient()

@client.event
async def on_member_join(member):
    role = get(member.guild.roles, name=AUTOROLE)
    await member.add_roles(role)
    print(f'{member} was given {role} role.')

@client.tree.command()
async def hello(ctx: discord.Interaction):
    await ctx.response.send_message(f'Hello, {ctx.user.mention}')

@client.tree.command()
async def worstcolumnist(ctx: discord.Interaction):
    await ctx.response.send_message("The winner of The BST Institute's Worst Columnist in Canada Contest (2021) is Rex Murphy. He stinks!")

#Live on Twitch Command 
@client.tree.command()
async def live(ctx: discord.Interaction):
    await ctx.response.send_message("@everyone WE ARE LIVE ON TWITCH: https://twitch.tv/bigshinytakes")
    await ctx.message.delete()

#new episode command 
@client.tree.command()
async def newep(ctx: discord.Interaction):
    await ctx.response.send_message("@everyone New episode from the good folks at the Big Shiny Takes Institute: https://bigshinytakes.com/newepisode.php")
    await ctx.message.delete()

#new role command 
@client.tree.command()
async def accept(ctx: discord.Interaction):
    user = ctx.user
    role = discord.utils.get(user.guild.roles, name="New Friend")
    await user.add_roles(role)
    await ctx.response.send_message(f"Welcome to the channel {user}")

#fb 
@client.tree.command()
async def fightback(ctx: discord.Interaction):
    await ctx.response.send_message("(we're so sorry fightback!)")

#new oppo command 
@client.tree.command()
async def opday(ctx: discord.Interaction):
    await ctx.response.send_message("(haha jk it's opposite day)")

#new mojo command 
@client.tree.command()
async def mojo(ctx: discord.Interaction):
    user = ctx.user
    await ctx.response.send_message(f"Mojo levels are good, vibes as well. I'll be monitoring the situation. Thanks for asking {user}")

##New NatPo Article Headline
@client.tree.command()
async def newColumn(ctx: discord.Interaction):
    newHead = GenerateColumn()
    await ctx.response.send_message(newHead)

@client.tree.command()
async def member(ctx: discord.Interaction):
    member_list = ''
    for member in ctx.message.server.members:
        member_list += member.name
    await ctx.response.send_message(member_list)






