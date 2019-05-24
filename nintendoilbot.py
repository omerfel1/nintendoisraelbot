#מהמחשב של עומר


import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
prefix = "?"
TOKEN = 'NTY1NDMxOTIzNDA5NjgyNDUy.XK3BIA.qZr8gJMJ2nKQ3N96_cBy6OeWmZw'
Client = commands.Bot(command_prefix=prefix)
client = discord.Client()
players= {}
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    #ChannelURL
    if message.content.startswith('$update'):
        update = 'To the last update: https://www.youtube.com/watch?v=kqcIFZFQ3qQ '.format(message)

        await client.send_message(message.channel, update)
    #invite
    if message.content.startswith('$invite'):
        invite ="Invation : https://discord.gg/bB5BbRv".format(message)
        await client.send_message(message.channel,invite)
    #help
           
    if message.content.startswith('$help' or '$HELP'):
        
        msg= f""" <@&534073769594060823> <@&534073537552449547> {message.author.mention}   Needs your help """.format(message)
        
       
        await client.send_message(message.channel, msg)
    if message.content.startswith('$switch'):
        user = ctx.message.author
        role = discord.utils.get(user.server.roles, name="switch")
        await client.add_roles(user, role)
@client.event
async def on_member_join(member):
    channel = client.get_channel("534017949078388740")
    await client.send_message(channel, "Hello " + member.mention + " ! welcome to our server")

    
    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------') 

client.run(TOKEN)
