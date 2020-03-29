import discord
from discord.ext import commands

class attachments(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, message):
        channel = self.bot.get_channel(673135393616691211)
        if not message.channel.category_id:
            return
        if not message.channel.category_id == 622343159439163394:
            return
        if message.attachments:
            for i in message.attachments:
                embed = discord.Embed(title="shitty shit")
                embed.set_image(url=i.url)
                await channel.send(embed=embed)
        else:
            return

def setup(bot):
    bot.add_cog(attachments(bot))
