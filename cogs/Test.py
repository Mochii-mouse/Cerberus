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
    async def spam_bot(self, message):


def setup(client):
    client.add_cog(test(client))