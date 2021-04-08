from assets.stuff import *


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @bot.command(help="Sets the bots status")
        async def setstatus(ctx, activity, *, new_status):
            if ctx.author.id in trusted:
                status = new_status
                if activity == "watching":
                    print(f'{bcolors.BOLD + bcolors.OKBLUE}Status set to "{bcolors.OKCYAN}{activity} {status}{bcolors.OKBLUE}"{bcolors.ENDC}')
                    await bot.change_presence(
                        activity=discord.Activity(name=status, type=discord.ActivityType.watching))
                    await ctx.reply(f'Status set to "{activity} {status}"')

                elif activity == "playing":
                    print(f'{bcolors.BOLD + bcolors.OKBLUE}Status set to "{bcolors.OKCYAN}{activity} {status}{bcolors.OKBLUE}"{bcolors.ENDC}')
                    await bot.change_presence(
                        activity=discord.Activity(name=status, type=discord.ActivityType.playing))
                    await ctx.reply(f'Status set to "{activity} {status}"')

                elif activity == "listening":
                    print(f'{bcolors.BOLD + bcolors.OKBLUE}Status set to "{bcolors.OKCYAN}{activity} {status}{bcolors.OKBLUE}"{bcolors.ENDC}')
                    await bot.change_presence(
                        activity=discord.Activity(name=status, type=discord.ActivityType.listening))
                    await ctx.reply(f'Status set to "{activity} to {status}"')

                elif activity == "competing":
                    print(f'{bcolors.BOLD + bcolors.OKBLUE}Status set to "{bcolors.OKCYAN}{activity} {status}{bcolors.OKBLUE}"{bcolors.ENDC}')
                    await bot.change_presence(
                        activity=discord.Activity(name=status, type=discord.ActivityType.competing))
                    await ctx.reply(f'Status set to "{activity} in {status}"')
                else:
                    await ctx.reply(f"That's not a valid activity!")

            else:
                print(f'{bcolors.FAIL}{ctx.author.name}{bcolors.WARNING} Tried to change the status to "{bcolors.FAIL}{activity} {new_status}{bcolors.WARNING}"{bcolors.ENDC}')
                await ctx.message.add_reaction("🔐")

        @bot.command(help="Restarts the bot")  # Currently not working
        async def reload(ctx, to_reload=None):
            if ctx.author.id in trusted:
                reloads = []
                failedreloads = []
                successfulreloads = []
                await ctx.message.add_reaction("👍")
                print(f"{bcolors.OKBLUE}Reloading cogs!{bcolors.ENDC}")
                for cog in COGS:
                    try:
                        bot.reload_extension(f"cogs.{cog}")
                        reloads.append(f"{bcolors.OKBLUE}│ {bcolors.OKGREEN}{cog}{bcolors.ENDC}")
                        successfulreloads.append(cog)
                    except:
                        reloads.append(f"{bcolors.FAIL}│ {bcolors.WARNING}{cog}{bcolors.ENDC}")
                        failedreloads.append(cog)
                print("\n".join(reloads))
                if len(failedreloads) > 0:
                    embedcolor = 0xeb4034
                else:
                    embedcolor = 0x34eb40
                embed = discord.Embed(title=f"Reloaded cogs!", color=embedcolor,
                                      #description="**Successful reloads:**\n" + "\n".join(successfulreloads) + "\n**Failed reloads:**\n" + "\n".join(failedreloads)
                                      )
                embed.add_field(name="Successful reloads:", value="‍"+"\n".join(successfulreloads))
                embed.add_field(name="Failed reloads:", value="‍"+"\n".join(failedreloads))
                embed.set_footer(text=f"Requested by {ctx.author}")
                await ctx.send(embed=embed)
            else:
                await ctx.message.add_reaction("🔐")

        @bot.command(aliases=['die', 'kill'], help="Stops the bot")
        async def stop(ctx):
            if ctx.author.id in trusted:
                await ctx.message.add_reaction("👍")
                await ctx.reply("Ok. :(")
                print(f"{bcolors.FAIL + bcolors.BOLD}{ctx.author.name} Told me to stop{bcolors.ENDC}")
                await bot.logout()
                await bot.close()
            else:
                await ctx.message.add_reaction("🔐")


def setup(bot):
    bot.add_cog(Admin(bot))