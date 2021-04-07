from assets.stuff import *


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @bot.command(help="Shows this page")
        async def help(ctx):
            commandlist = ''
            for command in self.bot.walk_commands():
                commandlist += f'**{command}** - {command.help}\n'
            embed = discord.Embed(colour=ctx.author.colour, timestamp=ctx.message.created_at, title=f"Help",
                                  description=f"**{bot.user.name}**, a bot created by <@444800636681453568> when he was bored!")
            embed.add_field(name="Commands", value=commandlist)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.reply(embed=embed)

        # Command to get info about the minecraft discord dyno tags
        @bot.command(aliases=['dynotags', 'dt'], help="Tags for dyno in maincord")
        async def dynotag(ctx, tagname=None, extra=None):
            if tagname != None:
                if extra != None and extra.lower() == "dyno" or "d":
                    await ctx.message.delete()
                    await ctx.send(dynotags[tagname])
                else:
                    try:
                        embed = discord.Embed(colour=0x00ffff, timestamp=ctx.message.created_at)
                        embed.set_footer(text=f"Requested by {ctx.author}")
                        embed.add_field(name="Tag content:", value=dynotags[tagname])
                        embed.add_field(name="Raw tag data:", value=f"```{dynotags[tagname]}```")
                        await ctx.reply(embed=embed)
                    except KeyError:
                        await ctx.reply("That's not a valid tag!")
            else:
                embed = discord.Embed(colour=0x00ffff, title="Dyno tags", timestamp=ctx.message.created_at)
                embed.set_footer(text=f"Requested by {ctx.author}")
                embed.add_field(name="Tags:", value=", ".join(k for k in dynotags.keys()))
                await ctx.reply(embed=embed)
                # await ctx.send(dynotags.keys())

        # Prints all the minecraft discord dyno tags
        @bot.command(help="Prints all tags (admin only)")
        @has_permissions(administrator=True)
        async def alltags(ctx):
            print(f'{bcolors.OKGREEN}Printing all tags in channel: {bcolors.OKCYAN}#{ctx.channel}{bcolors.OKGREEN} ID:"{bcolors.OKCYAN}{ctx.channel.id}{bcolors.OKGREEN}"{bcolors.ENDC}')
            for key in dynotags.keys():
                embed = discord.Embed(colour=0x2c7bd2, title=f"?t {key}", description=dynotags[key])
                await ctx.send(embed=embed)

        @bot.command()
        async def Stats(ctx):
            embed = discord.Embed(colour=0x09CCA2, timestamp=ctx.message.created_at,
                                  title="System Info")
            embed.add_field(name="RAM usage", value=f"{round(psutil.virtual_memory().used / 1000000000, 1)}GB out of a total of {round(psutil.virtual_memory().total / 1000000000, 1)}GB")
            embed.add_field(name="CPU usage", value=f"{psutil.cpu_percent()}%")
            embed.add_field(name="e", value=os.uname())
            await ctx.reply(embed=embed)

        # Command to get info about a account
        @bot.command(help="Displays information about a discord user")
        async def whois(ctx, member: discord.Member = None):
            if not member:
                member = ctx.message.author
            roles = [role.mention for role in member.roles[1:]]
            embed = discord.Embed(colour=member.colour, timestamp=ctx.message.created_at,
                                  title=f"User Info - {member}")
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author}")

            embed.add_field(name=f"Info about {member.name}", value=f"""**Username:** {member.name}
            **Nickname:** {member.display_name}
            **Mention:** {member.mention}
            **ID:** {member.id}
            **Account Created At:** {member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}
            **Activity:** {member.activity.name}
            **Joined server at:** {member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}
            **Is user on mobile:** {member.is_on_mobile()}
            **Highest Role:** {member.top_role.mention}

            **Roles:** {" ".join(roles)}""")
            await ctx.send(embed=embed)

        @bot.command(aliases=['Exec'], help="Executes code")
        async def execute(ctx, *, arg):
            #    if ctx.author.id in trusted:
            if ctx.author.id == ownerid:  # Checking if the person is the owner
                try:
                    exec(arg)
                    await ctx.message.add_reaction("<:yes:823202605123502100>")
                except Exception:
                    await ctx.message.add_reaction("<:no:823202604665929779>")
            else:
                await ctx.message.add_reaction("🔐")

        @bot.command(aliases=['Eval'], help="Evaluates things")
        async def evaluate(ctx, *, arg=None):
            if arg is None:
                await ctx.reply("I cant evaluate nothing")
                return
            if ctx.author.id in trusted:  # Checks if the user is trusted
                # Checks if the bots token is in the output
                if os.getenv('TOKEN') in str(eval(arg)):
                    # Sends a randomly generated string that looks like a token
                    await ctx.reply(''.join(random.choices(string.ascii_letters + string.digits, k=59)))
                else:
                    try:
                        await ctx.reply(eval(arg))  # Actually Evaluates
                        await ctx.message.add_reaction("<:yes:823202605123502100>")
                    except Exception:
                        await ctx.message.add_reaction("<:no:823202604665929779>")
            else:
                await ctx.message.add_reaction("🔐")

        @bot.command(help="Counts the amount of people in the server (can have bots/all specified at the end)")
        async def members(ctx, bots=None):
            if bots is None:  # Defaults to just users
                servermembers = [member for member in ctx.guild.members if not member.bot]
                await ctx.send(f"There is a total of {len(servermembers)} people in this server.")
            elif bots.lower() == "all":  # Command to count all accounts in the server
                await ctx.send(f"There is a total of {str(len(ctx.guild.members))} members in this server.")
            elif bots.lower() == "bots":  # Command to only count the bots
                servermembers = [member for member in ctx.guild.members if member.bot]
                await ctx.send(f"There is a total of {len(servermembers)} bots in this server.")
            else:  # Bad code but it works
                servermembers = [member for member in ctx.guild.members if not member.bot]
                await ctx.send(f"There is a total of {len(servermembers)} people in this server.")

        @bot.command(aliases=['fripemail'], help="Sends a message to fripe")
        @commands.cooldown(1, 150, commands.BucketType.user)
        async def mailfripe(ctx, *, arg):
            if arg == "None":
                await ctx.send("You have to specify a message!")
            else:
                await ctx.send("Messaged Fripe!")
                await bot.get_channel(823989070845444106).send(f'{ctx.author.mention}\n- {arg}')


def setup(bot):
    bot.add_cog(Utility(bot))