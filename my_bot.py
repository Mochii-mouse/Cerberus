import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '/')
status = cycle(['Status 1', 'Status 2', 'Status 3'])

@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready.')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used.')

@client.event
async def on_member_join(ctx, member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain',
                'It is decidedly so',
                'Without a doubt',
                'Yes, definitely',
                'You may rely on it',
                'As I see it, yes',
                'Most likely',
                'Outlook good',
                'Yes',
                'Signs point to yes',
                'Reply hazy try again',
                'Ask again later',
                'Better not tell you now',
                'Cannot predict now',
                'Concentrate and ask again',
                "Don't count on it",
                'My reply is no',
                'My sources say no',
                'Outlook not so good',
                'Very doubtful']
    await ctx.send(f'Question: {question}\nAnswer:{random.choice(responses)}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an ammount of messages to delete.')

@client.command()
@commands.has_guild_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
@commands.has_guild_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.command()
@commands.has_guild_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users: 
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'unbanned {user.mention}')
            return

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

env = {}
with open('./.env') as f:
    for line in f.read().splitlines():
        values = line.split('=')
        key = values[0]
        value = "=".join(values[1:])
        env[key] = value

print(env)
token = env['discord_token']

client.run(token)
