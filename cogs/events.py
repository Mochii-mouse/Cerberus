import discord
from discord.ext import commands


class events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if 'Clark' in message.content:
            await message.channel.send('Clark is a cutie pie!')

    # @commands.Cog.listener()
    # async def on_message(self, message):
    #    if message.author.bot:
    #        return
    #    if '' in message.content:
    #        await message.channel.send('Clark is a cutie pie!')


def setup(client):
    client.add_cog(events(client))
