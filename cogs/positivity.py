import discord
from discord.ext import commands, tasks


class positivity(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.dm_only()
    async def confess(self, ctx, *, message):
        channel = self.client.get_channel(1117497926541922345)
        sender = ctx.author
        confession = await channel.send(f'"{message}" sent by ||{sender}||')
        await confession.add_reaction('✅')
        await confession.add_reaction('❌')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = self.client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = self.client.get_user(payload.user_id)
        if payload.channel_id == 1117497926541922345:
            if str(payload.emoji) == '✅' and not user.bot:
                channel = self.client.get_channel(1117497819989819413)
                await channel.send(message.content.split(' sent by')[0].strip('"'))
                await message.delete()
            elif str(payload.emoji) == '❌' and not user.bot:
                print("Don't send")
                await message.delete()


async def setup(client):
    await client.add_cog(positivity(client))
