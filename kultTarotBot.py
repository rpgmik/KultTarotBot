## Runs in Linux via: python kultTarotBot.py
## Requires Python > 3.4
## Bot needs to be given message read and send permissions on the Discord server.
## Need to install the discord.py API wrapper (e.g., via: pip install discord.py)
##
## Discord Bot Token needs to be in a file called "tokenFile.txt" which sits in the same
## dircetory as this file.

import random
import discord

## Read in Discord bot token from file: tokenFile.txt
f = open('devToken.txt', "r")
TOKEN = f.readline().rstrip()
f.close()

## Define cards
names = ["Anthropos", "Demiurge", "Astaroth", "Kether - Hiearchy",
         "Chokmah - Submission", "Binah - Community", "Chesed - Safety",
         "Geburah - Law", "Tiphareth - Allure", "Netzach - Victory",
         "Hod - Honor", "Yesod - Avarice", "Malkuth - Awakening",
         "Thaumiel - Power", "Chagidiel - Abuse", "Sathariel - Exclusion",
         "Gamichicoth - Fear", "Golab - Torment", "Togarini - Compulsion",
         "Hareb-Serap - Conflict", "Samael - Venegance", "Gamaliel - Lust",
         "Nahemoth - Discord", "One of Skulls - Metropolis",
      	 "Two of Skulls - Forgetfulness", "Three of Skulls - Remnants",
      	 "Four of Skulls - Spirit", "Five of Skulls - Transition",
      	 "Six of Skulls - Flesh", "Seven of Skulls - Weapon",
      	 "Eight of Skulls - Suffering", "Nine of Skulls - Inferno",
      	 "One of Roses - Gaia", "Two of Roses - Birth",
      	 "Three of Roses - Survival", "Four of Roses - Growth",
      	 "Five of Roses - Predator", "Six of Roses - Swarm",
      	 "Seven of Roses - Prey", "Eight of Roses - Obsession",
      	 "Nine of Roses - Love", "One of Hourglasses - Achylys",
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
      	 "Four of Eyes - Distractions", "Five of Eyes - Divison",
      	 "Six of Eyes - Rebellion", "Seven of Eyes - Madness",
      	 "Eight of Eyes - Visions", "Nine of Eyes - Enlightenment"]

## Get discord connection
client = discord.Client()

## Define an event so that Bot can read messages
@client.event
async def on_message(message):

    ## Respond if user sends "!tarot"
    if message.content.startswith('!tarot'):

        ## Split into into "!tarot" and number of cards to draw
        bits = message.content.split(" ")

        ## Use 5 cards if not defined, otherwise convert to integer
        num = 5
        comment = ''
        sep = ' '
        if len(bits)>1:
            if(list(bits[1])[0]!="#"):
                num = int(bits[1])
            elif(list(bits[1])[0]=="#"):
                comment = sep.join(bits[1:])
#            elif(list(bits[1])[0]=="!"):
#                comment  = " "
#                comment += bits[1:]

        if len(bits)>2:
            if(list(bits[2])[0]=="#"):
                comment = sep.join(bits[2:])
#            elif(list(bits[2])[0]=="!"):
#                comment  = " "
#                comment += bits[2:]

        msg = '```md\n'
        if comment!='':
            msg += comment
            msg += '\n'

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

        msg+='```'

        ## Send message to channel
        await message.channel.send(msg)

## Write login details locally (i.e., on linux box where bot code is running)
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Kult: !tarot or !tarot n"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

## Run Bot on Discord server
client.run(TOKEN)
