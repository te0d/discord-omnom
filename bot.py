import logging
import os

from discord.ext import commands
from monitor_channel_cog import MonitorChannelCog

logging.basicConfig(level=logging.INFO)

bot_token = os.environ.get("OMNOM_TOKEN", None)
if not bot_token:
    exit("A token for a bot from Discord is required. Set the environment variable OMNOM_TOKEN to the bot's secret token provided by Discord.")

bot = commands.Bot(command_prefix='!')
bot.add_cog(MonitorChannelCog(bot))
bot.run(bot_token)
