import discord
import logging

from discord.ext import commands

class MonitorChannelCog(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self._db = db
        self.command_channel = None
        self.proposal_channel = None

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if self.proposal_channel is not None and message.channel.id == self.proposal_channel.id:
            self._db.add_message(message)
            await message.channel.send('ok')
        else:
            pass
            # await bot.process_commands(message)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        self._db.edit_message(after)
        await before.channel.send("'{}' was edited to '{}'.".format(before.id, after.id))

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        self._db.delete_message(message)
        await message.channel.send("'{}' was deleted.".format(message.id))

    @commands.command()
    async def monitor(self, ctx, channel: discord.TextChannel):
        self.proposal_channel = channel
        await ctx.send('You want me to monitor "{}"?'.format(channel))

    @commands.command()
    async def clear(self, ctx):
        self._db.clear()

    @commands.command()
    async def debug(self, ctx):
        await ctx.send("Monitoring:\t{}\nMessage Count:\t{}".format(self.proposal_channel, self._db.get_count()))
