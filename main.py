import discord
import discord.ext
import os
from keep_alive import keep_alive
from threading import Thread
with open('.token' , 'r') as token:
    tok = token.read()
client = discord.Client()

dev_id = 765739254164357121

prefix = 't!'

@client.event 
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event #epic
async def on_message(message):

    with open('messages.log.txt' , 'a') as log:
        __msg = str(f"{message.author} : {message.content} ({message.channel} [{message.channel.id}])\n")
        log.write(__msg)
    msg = str(message.content)
    if msg.startswith(prefix):
        command = msg.replace(prefix , '')
        if command.casefold() == ' dev':
            if message.author.id != dev_id:
                await message.reply(f'<@!{message.author.id}> my developer is <@!{dev_id}>')
            else:
                await message.reply('Hey! You are my developer. Hi dad!')
        
        if command.casefold() == ' cat' or command.casefold() == ' nyan':

            await message.channel.send(file=discord.File('./Nyan Cat.mp4'))
            await message.reply('Rainbow Kitty go brrrr!!!')
        
        
# keep_alive()
client.run(tok)