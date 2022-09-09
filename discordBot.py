import discord 
from discord.ext import commands
from discord.utils import get
from NewColumn import *

AUTOROLE = "New Friend"

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Bot running.")

#Autoassign original role
@bot.event
async def on_member_join(member):
    role = get(member.guild.roles, name=AUTOROLE)
    await member.add_roles(role)
    print(f"{member} was given {role} role.")

#Hello Command 
@bot.command()
async def hello(ctx):
    await ctx.reply('Hello!')

#Worst Column Command 
@bot.command()
async def worstcolumnist(ctx):
    await ctx.reply("The winner of The BST Institute's Worst Columnist in Canada Contest (2021) is Rex Murphy. He stinks!")

#Live on Twitch Command 
@bot.command()
async def live(ctx):
    await ctx.reply("@everyone WE ARE LIVE ON TWITCH: https://twitch.tv/bigshinytakes")
    await ctx.message.delete()

#new episode command 
@bot.command()
async def newep(ctx):
    await ctx.reply("@everyone New episode from the good folks at the Big Shiny Takes Institute: https://bigshinytakes.com/newepisode.php")
    await ctx.message.delete()

#new role command 
@bot.command()
async def accept(ctx):
    user = ctx.author
    role = discord.utils.get(user.guild.roles, name="New Friend")
    await user.add_roles(role)
    await ctx.reply(f"Welcome to the channel {user}")

#fb 
@bot.command()
async def fightback(ctx):
    await ctx.reply("(we're so sorry fightback!)")

#new oppo command 
@bot.command()
async def opday(ctx):
    await ctx.reply("(haha jk it's opposite day)")

#new mojo command 
@bot.command()
async def mojo(ctx):
    user = ctx.author
    await ctx.reply(f"Mojo levels are good, vibes as well. I'll be monitoring the situation. Thanks for asking {user}")

##New NatPo Article Headline
@bot.command()
async def newColumn(ctx):
    newHead = GenerateColumn()
    await ctx.reply(newHead)

@bot.command()
async def member(ctx):
    member_list = ''
    for member in ctx.message.server.members:
        member_list += member.name
    await ctx.reply(member_list)

bot.run('#')