import discord 
from discord.ext import commands
from discord.utils import get


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

#Natpo command 
@bot.command()
async def newColumn(ctx):
    import random



    ####Enemies List
    numEnem = random.randint(1,10)
    #print(numEnem)

    listEnem = ["Trudeau", 
        "Greta Thunberg", 
        "Joseph Stalin", 
        "China",
        "Antifa",
        "The Woke Mob",
        "The Woke Left",
        "George Soros",
        "The Deficit",
        "Homeless People",
        "BLM",
        "My Niece doing a Sociology Undergrad"]


    varEnem = listEnem[numEnem]
    #print(varEnem)

    ####Friends List
    numFren = random.randint(1,10)
    #print(numFren)

    listFren = ["Ayn Rand", 
        "Elon Musk", 
        "Bill Gates", 
        "The Wolf of Wall Street",
        "Some Speculative Real Estate Investor",
        "A Mining Executive Named Kyle",
        "David Frum",
        "Gad Saad",
        "Jordan Peterson's Corpse",
        "My Racist Uncle",
        "The Macdonald Laurier Institute"]


    varFren = listFren[numFren]
    #print(varFren)

    ####Bad things they like List
    numBad = random.randint(0,7)
    #print(numBad)

    listBad = ["Free Market",       
            "Capitalism",
            "Statues of Assholes",
            "Billionaires",
            "NATO",
            "bombing campaigns in countries that aren't predominantly white",
            "Budget Cuts",
            "Tax Breaks for the Wealthy"]

    varBad = listBad[numBad]
    #print(varBad)

    ####Good things they don't like 
    numGood = random.randint(0,13)
    #print(numGood)

    listGood = ["Dental Care",
            "working class solidarity",
            "solar panels",
            "public transit",
            "Socialism",
            "Defunding the Police",
            "prison abolition",
            "Stopping Climate Change",
            "Fair Taxes",
            "the Welfare State",
            "not having wars",
            "anti-discrimination laws",
            "Trans rights",
            "consequences for being awful"]
    varGood = listGood[numGood]
    #print(varGood)

    #### Hacks that write for them
    numHack = random.randint(0,9)
    #print(numHack)

    listHack = ["Barbara Kay",
                "Rex Murphy",
                "Terry Glavin",
                "Lorne Gunter",
                "John Ivison",
                "Tristin Hopper",
                "Kelly Mcparland",
                "Jessie Kline",
                "Rupa Subramunya",
                "A very dead Christie Blatchford"
                ]
    varHack = listHack[numHack]
    #print(varHack)

    #### domestic activities pundits would find demeaning but shoe horn into arguments
    numDmst = random.randint(0,9)
    #print(numHack)

    listDmst = ["going to the gas station",
                "using a self-checkout lane",
                "washing the dishes",
                "mowing the lawn",
                "taking public transit",
                "gardening",
                "watering your grass",
                "fixing a boken fence",
                "cleaning the bathroom",
                "unclogging the drain"
                ]
    varDmst = listDmst[numDmst]
    #print(varHack)

    '''
    ADDING VARIABLES TO MAD LIB DICTIONARY
    '''
    madlibDict = {"Enemy": varEnem, "Friend":varFren, "Bad": varBad, "Good": varGood, "Hack": varHack, "Domestic": varDmst}

    '''

    FORMATTED HEADLINES 

    '''

    head1 = 'The unknown consequence of {data[Good]}? It opens the door for more communism from {data[Enemy]}. - By {data[Hack]}'.format(data=madlibDict) 
    head2 = 'How can we secure a future for {data[Bad]}? Simple, just ask {data[Friend]}. - By {data[Hack]}'.format(data=madlibDict) 
    head3 = '{data[Good]} is killing our precious {data[Bad]} and we need to stop it. - By {data[Hack]}'.format(data=madlibDict) 
    head4 = 'How {data[Friend]} is finally going to put an end to the {data[Good]} Agenda. - By {data[Hack]}'.format(data=madlibDict) 
    head5 = 'Think {data[Good]} has gone too far? So does {data[Friend]}. - By {data[Hack]}'.format(data=madlibDict) 
    head6 = 'What is {data[Good]} and what does it mean for your portfolio? - By {data[Hack]}'.format(data=madlibDict) 

    listHead = [head1, head2, head3, head4, head5,head6]
    numHead = random.randint(0,(len(listHead)-1))

    #print('list length: ', len(listHead))
    varNewColumn = listHead[numHead]
    await ctx.reply(varNewColumn)

@bot.command()
async def member(ctx):
    member_list = ''
    for member in ctx.message.server.members:
        member_list += member.name
    await ctx.reply(member_list)

bot.run('#')