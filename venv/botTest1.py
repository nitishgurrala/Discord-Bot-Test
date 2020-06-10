import discord
from discord.ext import commands

from BBR_Reference import season

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$stats'):
        await message.channel.send("Please enter the player's name like so: '$name:BlueDressCapital'")

    if message.content.startswith('$name'):
        await message.channel.send('Getting player stats....')
        playerName = '{0.content}'.format(message)
        playerName = playerName[6:]
        name = playerName.split()
        print(name)
        testSeason = season(name[0], name[1], 1995)
        x = testSeason.getStats("per_game")
        await message.channel.send(x)
        #print(x)


client.run('NzE1MDI5NjE2NTU3MDMxNDU0.Xs7lfA.ONxAB4NRbn7Hk-RcQmfawgCepxQ')
