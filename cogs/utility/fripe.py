from assets.stuff import *


class Fripe(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(aliases=['fripemail'], help="Sends a message to fripe")
    @commands.cooldown(1, 150, commands.BucketType.user)
    async def mailfripe(self, ctx, *, arg):
        if arg == "None":
            await ctx.send("You have to specify a message!")
        else:
            await ctx.message.delete()
            await ctx.send("Messaged Fripe!")
            await bot.get_channel(823989070845444106).send(f'{ctx.author.mention}\n- {arg}')

    @command(aliases=['remfripe'], help="Sends a reminder to fripe")
    @commands.cooldown(1, 150, commands.BucketType.user)
    async def remindfripe(self, ctx, *, arg):
        if arg == "None":
            await ctx.send("You have to specify a message!")
        else:
            await ctx.send("Reminded Fripe!")
            await bot.get_channel(824022687759990845).send(f'{ctx.author.mention}\n- {arg}')


def setup(bot):
    bot.add_cog(Fripe(bot))
