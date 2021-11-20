import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix = '+', intents=intents)
intents.members = True

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")
  


@bot.command()
async def all(ctx):
    embed = discord.Embed(
        title="все команды",
        description="пусто | экономика - +economy модерация - +moder",
    )
    await ctx.send(embed=embed)

@bot.command()
async def economy(ctx):
    embed = discord.Embed(
        title="экономика",
        description="пусто | экономика - +economy модерация - +moder",
    )
    await ctx.send(embed=embed)

@bot.command()
async def moder(ctx):
    embed = discord.Embed(
        title="модерация",
        description="пусто | экономика - +economy модерация - +moder",
    )
    await ctx.send(embed=embed)

@bot.command()
async def prefix(ctx):
    await ctx.send("префикс `+`")


bot.run("ODg2Njc1MjE4NDE5MDU2NjYw.YT5CpQ.gfx0_SOLZf4jBqONygpMXdamapA")