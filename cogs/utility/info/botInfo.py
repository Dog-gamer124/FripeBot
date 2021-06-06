from assets.stuff import *


class BotInfo(Cog):
    def __init__(self, bot):
        self.bot = bot

    # Command to get the bots ping
    @command(help="Displays the bots ping")
    async def ping(self, ctx, real=None):
        await ctx.message.add_reaction("🏓")
        bot_ping = round(bot.latency * 1000)
        if bot_ping < 130:
            color = 0x44ff44
        elif bot_ping > 130 and bot_ping < 180:
            color = 0xff8c00
        else:
            color = 0xff2200
        embed = discord.Embed(title="Pong! :ping_pong:",
                              description=f"The ping is **{bot_ping}ms!**",
                              color=color)
        await ctx.reply(embed=embed)

    # Code stolen (with consent) from "! Thonk##2761" on discord
    # Code is heavily modified by me
    @command(aliases=['source'], help="Links my GitHub profile")
    async def github(self, ctx, member: discord.Member = None):
        embed = discord.Embed(title="Fripe070", url="https://github.com/Fripe070",
                              color=0x00ffbf, timestamp=ctx.message.created_at)
        embed.set_author(name="Fripe070", url="https://github.com/Fripe070",
                         icon_url="https://github.com/TechnoShip123/DiscordBot/blob/master/resources/GitHub-Mark-Light-32px.png?raw=true")
        embed.set_thumbnail(url="https://avatars.githubusercontent.com/fripe070")
        embed.add_field(name="This bot:", value="https://github.com/Fripe070/FripeBot")
        embed.set_footer(text="Requested by: " + ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.message.delete()
        if member != None:
            await ctx.send(f'{member.mention} Please take a look to my github', embed=embed)
        else:
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(BotInfo(bot))
