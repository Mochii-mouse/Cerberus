import discord
from discord.ext import commands
import datetime


class events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if 'Clark' in message.content:
            await message.channel.send('Clark is a cutie pie!')

    @commands.Cog.listener()
    async def on_message(self, message):
        if (datetime.datetime.now() - message.author.joined_at).days < 1:
            if 'nudes' in message.content.lower() or 'please ban' in message.content.lower():
                await message.author.ban()
                await message.channel.send(f'{message.author} has been banned')
            else:
                pass
        else:
            pass


async def setup(client):
    await client.add_cog(events(client))
