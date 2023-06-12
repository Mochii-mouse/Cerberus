from distutils import extension
import discord
import json
import random
import os
from discord.ext import commands, tasks
from itertools import cycle
import argparse
from dotenv import load_dotenv
load_dotenv()

token = os.getenv('token')
parser = argparse.ArgumentParser()
parser.add_argument('--mode', default='development',
                    choices=['development', 'production'])

args = parser.parse_args()
mode = args.mode

if mode == 'production':
    prefix = '.'
else:
    prefix = '!'
client = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
status = cycle(['Your mum', 'with C-3PO', 'OwO'])


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used.')


@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready')
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            print('Loading' + filename + ' (cog)...')
            await client.load_extension(f'cogs.{filename[:-3]}')


@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def load(ctx, extension):
    await client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    await client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(ctx, extension):
    await client.unload_extension(f'cogs.{extension}')
    await client.load_extension(f'cogs.{extension}')


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Don\'t count on it.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command(aliases=['pee'])
async def Pee(ctx, member: discord.Member):
    await ctx.send(f'Cerberus pees on {member.mention}')
    await ctx.message.delete()


client.run(token)
