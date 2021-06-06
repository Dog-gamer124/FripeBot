from assets.stuff import *


class MemberInfo(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(aliases=["pfpget", "gpfp", "pfp"], help="Gets a users profile picture at a high resolution")
    async def getpfp(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author

        embed = discord.Embed(colour=member.colour, timestamp=ctx.message.created_at,
                              title=f"{member.display_name}'s pfp")
        embed.set_image(url=getpfp(member))
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)

    # Command to get info about a account
    @command(help="Displays information about a discord user")
    async def whois(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        roles = [role.mention for role in member.roles[1:]]
        roles.reverse()
        pfp = str(member.avatar_url)[:-4] + "4096"

        embed = discord.Embed(colour=member.colour, timestamp=ctx.message.created_at,
                              title=f"User Info - {member}")
        embed.set_thumbnail(url=pfp)
        embed.set_footer(text=f"Requested by {ctx.author}")

        embed.add_field(name=f"Info about {member.name}", value=f"""**Username:** {rembackslash(member.name)}
        **Nickname:** {rembackslash(member.display_name)}
        **Mention:** {member.mention}
        **ID:** {member.id}
        **Account Created At:** {member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}
        **Joined server at:** {member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}
        **Is user on mobile:** {member.is_on_mobile()}
        **Highest Role:** {member.top_role.mention}

        **Roles:** {" ".join(roles)}""")
#            **Activity:** {afunctionthatfroopwants(member.activity.name)}
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(MemberInfo(bot))
