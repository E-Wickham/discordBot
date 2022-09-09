import discord 
from discord.ext import commands
from discord.utils import get
from Variables import *

def GenerateColumn():
    import random


    ##Randomly Generate Variables from lists in Variables.py
    ####Enemies List
    numEnem = random.randint(1,10)
    varEnem = listEnem[numEnem]
    
    ####Friends List
    numFren = random.randint(1,10)
    varFren = listFren[numFren]

    ####Bad things they like List
    numBad = random.randint(0,7)
    varBad = listBad[numBad]

    ####Good things they don't like 
    numGood = random.randint(0,13)
    varGood = listGood[numGood]

    #### Hacks that write for them
    numHack = random.randint(0,9)
    varHack = listHack[numHack]

    #### domestic activities pundits would find demeaning but shoe horn into arguments
    numDmst = random.randint(0,9)
    varDmst = listDmst[numDmst]

    ####Add Generated Content to Dictionary
    madlibDict = {"Enemy": varEnem, "Friend":varFren, "Bad": varBad, "Good": varGood, "Hack": varHack, "Domestic": varDmst}

    ####Create formatted headlines
    head1 = 'The unknown consequence of {data[Good]}? It opens the door for more communism from {data[Enemy]}. - By {data[Hack]}'.format(data=madlibDict) 
    head2 = 'How can we secure a future for {data[Bad]}? Simple, just ask {data[Friend]}. - By {data[Hack]}'.format(data=madlibDict) 
    head3 = '{data[Good]} is killing our precious {data[Bad]} and we need to stop it. - By {data[Hack]}'.format(data=madlibDict) 
    head4 = 'How {data[Friend]} is finally going to put an end to the {data[Good]} Agenda. - By {data[Hack]}'.format(data=madlibDict) 
    head5 = 'Think {data[Good]} has gone too far? So does {data[Friend]}. - By {data[Hack]}'.format(data=madlibDict) 
    head6 = 'What is {data[Good]} and what does it mean for your portfolio? - By {data[Hack]}'.format(data=madlibDict) 

    ##Randomly select a headline
    listHead = [head1, head2, head3, head4, head5,head6]
    numHead = random.randint(0,(len(listHead)-1))

    ##Print the selected Headline
    varNewColumn = listHead[numHead]
    return varNewColumn