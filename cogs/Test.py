import discord
from discord.ext import commands
import datetime


class test(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join_date(self, ctx, member: discord.Member):
        difference = datetime.datetime.now() - member.joined_at
        await ctx.send(member.joined_at)
        await ctx.send(f'{difference.days} days ago')

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


def setup(client):
    client.add_cog(test(client))
