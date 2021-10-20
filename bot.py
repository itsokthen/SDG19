import config
import discord
from discord.ext import commands

# TODO: See if bot works

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

client.run(config.bot_api_key)
