import discord
from discord.ext import commands

class welcome(commands.Cog):
    def __init__(self, client):
        self.client=client

    @commands.Cog.listener()
    async def on_ready(self):
        print("host: ON")

      
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(member)
        await member.send("хай")
        guild = self.bot.get_guild(901648944889733121)
        channel = discord.utils.get(member.guild.channels, id=901866676759461908)
        if guild:
            print("guild ok")
        else:
            print("guild not found")
        
        if channel is not None:
                await channel.send(f'Welcome to the {guild.name} Discord Server, {member.mention} !  :partying_face:')
        else:
            print("id channel wrong")

    @commands.command()
    async def status(self, ctx):
        embed = discord.Embed(
            title="Информация о хостинге",
            description=f"cogs `host.py` work | nodes online: 5 | bots online: 2 | nodes restarting: 0 п.с я на питоне бдфд говно",
)
        await ctx.send(embed=embed)

def setup(bot):
  client.add_cog(welcome(client))