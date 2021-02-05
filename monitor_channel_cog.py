import discord
import logging

from discord.ext import commands

class MonitorChannelCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.command_channel = None
        self.proposal_channel = None

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        logging.info("{} | {}".format(self.proposal_channel, message.channel.id))

        if self.proposal_channel is not None and message.channel.id == self.proposal_channel.id:
            await message.channel.send('ok')
        else:
            pass
            # await bot.process_commands(message)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        await message.channel.send("'{}' was deleted.".format(message.id))

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        await before.channel.send("'{}' was edited to '{}'.".format(before.id, after.id))

    @commands.command()
    async def monitor(self, ctx, channel: discord.TextChannel):
        self.proposal_channel = channel
        logging.info(channel.id)
        await ctx.send('You want me to monitor "{}"?'.format(channel))
