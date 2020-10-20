## Runs in Linux via: python kultTarotBot.py
## Requires Python > 3.4
## Bot needs to be given message read and send permissions on the Discord server.
## Need to install the discord.py API wrapper (e.g., via: pip install discord.py)
##
## Discord Bot Token needs to be in a file called "tokenFile.txt" which sits in the same
## dircetory as this file.

import random
import discord

## Ascertain mode: dev or production
m = open('modeFile.txt', "r")
MODE = m.readline().rstrip()
m.close()

## Read in Discord bot token from file
if MODE=="prod":
    tokenFile = 'prodToken.txt'
elif MODE=="dev":
    tokenFile = 'devToken.txt'

f = open(tokenFile, "r")
TOKEN = f.readline().rstrip()
f.close()

## Define cards
names = ["Anthropos", "Demiurge", "Astaroth", "Kether - Hierarchy",
         "Chokmah - Submission", "Binah - Community", "Chesed - Safety",
         "Geburah - Law", "Tiphareth - Allure", "Netzach - Victory",
         "Hod - Honor", "Yesod - Avarice", "Malkuth - Awakening",
         "Thaumiel - Power", "Chagidiel - Abuse", "Sathariel - Exclusion",
         "Gamichicoth - Fear", "Golab - Torment", "Togarini - Compulsion",
         "Hareb-Serap - Conflict", "Samael - Vengeance", "Gamaliel - Lust",
         "Nahemoth - Discord", "One of Skulls - Metropolis",
      	 "Two of Skulls - Forgetfulness", "Three of Skulls - Remnants",
      	 "Four of Skulls - Spirit", "Five of Skulls - Transition",
      	 "Six of Skulls - Flesh", "Seven of Skulls - Weapon",
      	 "Eight of Skulls - Suffering", "Nine of Skulls - Inferno",
      	 "One of Roses - Gaia", "Two of Roses - Birth",
      	 "Three of Roses - Survival", "Four of Roses - Growth",
      	 "Five of Roses - Predator", "Six of Roses - Swarm",
      	 "Seven of Roses - Prey", "Eight of Roses - Obsession",
      	 "Nine of Roses - Love", "One of Hourglasses - Achlys",
      	 "Two of Hourglasses - Future", "Three of Hourglasses - Past",
      	 "Four of Hourglasses - Space", "Five of Hourglasses - Borderland",
      	 "Six of Hourglasses - Hidden", "Seven of Hourglasses - Labyrinth",
      	 "Eight of Hourglasses - Crossroad", "Nine of Hourglasses - Gate",
      	 "One of Crescents - Vortex", "Two of Crescents - Creation",
      	 "Three of Crescents - Undoing", "Four of Crescents - Transformation",
      	 "Five of Crescents - Connection", "Six of Crescents - Merging",
      	 "Seven of Crescents - Reflection", "Eight of Crescents - Repetition",
      	 "Nine of Crescents - Stillness", "One of Eyes - Elysium",
      	 "Two of Eyes - Imprisonment", "Three of Eyes - Faith",
      	 "Four of Eyes - Distractions", "Five of Eyes - Division",
      	 "Six of Eyes - Rebellion", "Seven of Eyes - Madness",
      	 "Eight of Eyes - Visions", "Nine of Eyes - Enlightenment"]

majorArcana = names[:23]
minorArcana = names[23:]

ind = ["# Individual", "Card 1: A core Characteristic of the individual.",
"Card 2: Something from the Past that shaped the individual.", "Card 3: An Ambition that drives the individual.", "Card 4: The individual’s greatest Weakness.", "Card 5: The individual’s greatest Strength."]

loc = ["# Location", "Card 1: The Type of location.", "Card 2: Something about the location’s Past.", "Card 3: An unexpected or quirky Trait.", "Card 4: A Weakness at the location, which might be exploited.", "Card 5: Something that makes the location Exceptional."]

cul = ["# Cult", "Card 1: What Power/Ambition Drives the cult?", "Card 2: An important thing about the cult’s History.", "Card 3: What does the cult wish to Accomplish?", "Card 4: What is the cult’s Weakness, such as enemies?", "Card 5: What is the cult’s unexpected Resource?"]

plo = ["# Plot", "Card 1: What is the Power behind the plot?", "Card 2: What Caused the plot?", "Card 3: What is the Next Move in the plot?", "Card 4: What power Opposes the plot?", "Card 5: What power Supports the plot?"]

cre = ["# Creature", "Card 1: From what background does the creature Originate?", "Card 2: From where can you find Information about the creature?", "Card 3: What Drives the creature?", "Card 4: What is the creature’s Weakness?", "Card 5: What is the creature’s Strength?"]

art = ["# Artifact", "Card 1: From where does the Artifact Originate?", "Card 2: Who else is Looking for It?", "Card 3: What are the Dangers in using it?", "Card 4: What is its Primary Power?", "Card 5: What is its Secondary Power?"]

cards = ''

## Get discord connection
client = discord.Client()

## Define an event so that Bot can read messages
@client.event
async def on_message(message):

    global names

    ## Respond if user sends "!tarot"
    if message.content.startswith('!tarot'):

        ## Split into into "!tarot" and number of cards to draw
        bits = message.content.split(" ")

        num = ''
        comment = ''
        sep = ' '
        nl='\n'

        # If no other arguments, default to drawing 5 cards
        if len(bits)==1:
            num = 5

        if len(bits)>1:
            if list(bits[1])[0]=="#":
                comment = sep.join(bits[1:])
                num = 5
            elif list(bits[1])[0]=="?":
                comment = ''
            elif bits[1] in ["ind", "loc", "cul", "plo", "cre", "art"]:
                num = 5
                if bits[1]=="ind":
                    tmp = ind
                elif bits[1]=="loc":
                    tmp = loc
                elif bits[1]=="cul":
                    tmp = cul
                elif bits[1]=="plo":
                    tmp = plo
                elif bits[1]=="cre":
                    tmp = cre
                elif bits[1]=="art":
                    tmp = art

            elif isinstance(int(list(bits[1])[0]),int):
                num = int(bits[1])
                if len(bits) > 2:
                    if bits[2] in ["major", "maj"]:
                        names = majorArcana
                    elif bits[2] in ["minor", "min"]:
                        names = minorArcana

        if len(bits)>2:
            if(list(bits[2])[0]=="#"):
                comment = sep.join(bits[2:])

        if len(bits)>3:
            if(list(bits[3])[0]=="#"):
                comment = sep.join(bits[3:])

        msg = '```md\n'
        if comment!='':
            msg += comment
            msg += '\n'

        if isinstance(num, int):
            ## Restrict/check the number of cards to be drawn
            if num>10:
                num = 10
                msg = '10 is the maximum number of cards.\n\n'

            if num<1:
                num = 1
                msg = 'You must draw at least 1 card.\n\n'

            ## Draw a randow sample (without replacement) from list of cards
            cards = random.sample(names, k=num)

            ## Loop through 1 to n, adding card number and descriptor to message each time
            ## Creates a single string, with newline characters separateing each card.
            for i in range(1, num+1):
                msg+='Card {0}: {1}\n'.format(i, cards[i-1])

        if len(bits) > 1 and list(bits[1])[0]=="?":
            msg = '```md\n'
            if bits[1] in ["?","help"]:
                msg += '# Usage:\n'
                msg += '!tarot ? - displays this message\n'
                msg += '!tarot - draws 5 cards\n'
                msg += '!tarot n - draws n cards (1-10)\n'
                msg += '!tarot n # comment - adds a comment to the output\n'
                msg += '!tarot n maj - draws n cards from the major arcana\n'
                msg += '!tarot n min - draws n cards from the minor arcana\n'
                msg += '!tarot ?xxx - lists card definitions for template xxx\n'
                msg += '!tarot xxx - makes a 5 card draw for template xxx\n'
                msg += '# Templates: individuals (ind), locations (loc), cults (cul), plots (plo), creatures (cre) or artifacts (art)\n'

            if bits[1]=="?ind":
                msg += nl.join(ind)

            elif bits[1]=="?loc":
                msg += nl.join(loc)

            elif bits[1]=="?cul":
                msg += nl.join(cul)

            elif bits[1]=="?plo":
                msg += nl.join(plo)

            elif bits[1]=="?cre":
                msg += nl.join(cre)

            elif bits[1]=="?art":
                msg += nl.join(art)

        if len(bits) > 1 and bits[1] in ["ind", "loc", "cul", "plo", "cre", "art"]:
            msg = '```md\n'
            msg += tmp[0]
            msg += ":"
            msg += comment[1:]
            msg += "\n"
            for i in range(0,5):
                msg += '{0}\n#       {1}\n'.format(tmp[i+1], cards[i])

        msg+='```'

        ## Send message to channel
        await message.channel.send(msg)

## Write login details locally (i.e., on linux box where bot code is running)
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Kult: !tarot ? for help"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

## Run Bot on Discord server
client.run(TOKEN)
