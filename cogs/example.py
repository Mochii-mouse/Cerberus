import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '/')

class example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(ctx.bot.latency * 1000)}ms')

def setup (client):
    client.add_cog(example(client))