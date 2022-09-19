import discord
from discord.ext import commands, tasks
import datetime
import random
import asyncio


class events(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.channel_purge.start()
        self.monster_hunt.start()

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

    @tasks.loop(minutes=1)
    async def monster_hunt(self):
        channel = self.client.get_channel(1021369583560572948)
        Message = await channel.fetch_message(channel.last_message_id)
        Monsters = ['Witch', 'Ghost', 'Zombie', 'Black cat']
        if (datetime.datetime.now(datetime.timezone.utc) - Message.created_at).total_seconds() < (60*10):
            if Message.author.bot:
                return
            elif (random.randint(1, 10)) == 8:
                await channel.send(f'A {random.choice(Monsters)} has appeared!')

                def check(m):
                    return m.content == 'Catch' and m.channel == channel

                await self.client.wait_for('message', timeout=10.0, check=check)
                await channel.send(f'Caught!')


async def setup(client):
    await client.add_cog(events(client))
