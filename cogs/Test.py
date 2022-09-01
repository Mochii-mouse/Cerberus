import discord
from discord.ext import commands


class test(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join_date(self, member: discord.Member):
        difference = member.joined_at - datetime.now
        print(difference.days)


def setup(client):
    client.add_cog(test(client))
