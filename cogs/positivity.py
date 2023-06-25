import discord
from discord.ext import commands, tasks


class positivity(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.dm_only()
    async def compliment(self, ctx, *, message):
        channel = self.client.get_channel(1117925509045690388)
        sender = ctx.author
        confession = await channel.send(f'"{message}" sent by ||{sender}||')
        await confession.add_reaction('✅')
        await confession.add_reaction('❌')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = self.client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = self.client.get_user(payload.user_id)
        if payload.channel_id == 1117925509045690388:
            if str(payload.emoji) == '✅' and not user.bot:
                channel = self.client.get_channel(1035026935773925406)
                dec1 = '✧༺♥༻∞　　∞༺♥༻✧\n'
                dec2 = '\n.・。.・゜✭・.・✫・゜・。.'
                await channel.send(dec1 + message.content.split(' sent by')[0].strip('"') + dec2)
                await message.delete()
            elif str(payload.emoji) == '❌' and not user.bot:
                print("Don't send")
                await message.delete()

    @commands.command()
    @commands.dm_only()
    async def grievance(self, ctx, *, message):
        channel = self.client.get_channel(1117925509045690388)
        sender = ctx.author
        grievance = await channel.send(f'### Grievance \n "{message}"\n from ||{sender}||')


async def setup(client):
    await client.add_cog(positivity(client))
