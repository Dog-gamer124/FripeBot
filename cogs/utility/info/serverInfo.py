from assets.stuff import *


class ServerInfo(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(help="Counts the amount of people in the server (can have bots/all specified at the end)")
    async def members(self, ctx):
        embed = discord.Embed(colour=ctx.author.colour, timestamp=ctx.message.created_at, title="Member Info")
        embed.set_footer(text=f"Requested by {ctx.author.display_name}")
        embed.add_field(name=f"Users:", value=f"{len([member for member in ctx.guild.members if not member.bot])}")
        embed.add_field(name=f"Bots:", value=f"{len([member for member in ctx.guild.members if member.bot])}")
        embed.add_field(name=f"Total:", value=f"{len(ctx.guild.members)}")
        await ctx.reply(embed=embed)

    @command()
    async def allroles(self, ctx):
        embed = discord.Embed(colour=0x2c7bd2, title="e", description=f"")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ServerInfo(bot))
