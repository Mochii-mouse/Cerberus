import discord
from discord.ext import commands, tasks
import datetime


class events(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.channel_purge.start()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        elif 'Clark' in message.content:
            await message.channel.send('Clark is a cutie pie!')
        elif (datetime.datetime.now(datetime.timezone.utc) - message.author.joined_at).days < 1:
            if 'nudes' in message.content.lower() or 'please ban' in message.content.lower():
                await message.author.ban()
                await message.channel.send(f'{message.author} has been banned')
        elif 'halloween' in message.content.lower():
            emoji = '\N{ghost}'
            await message.add_reaction(emoji)

    @tasks.loop(seconds=60)
    async def channel_purge(self):
        channel = self.client.get_channel(1015991023693991957)
        async for message in channel.history():
            if (datetime.datetime.now(datetime.timezone.utc) - message.created_at).days > 0:
                await message.delete()


async def setup(client):
    await client.add_cog(events(client))
