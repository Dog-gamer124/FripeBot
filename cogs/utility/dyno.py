from assets.stuff import *


class Dyno(Cog):
    def __init__(self, bot):
        self.bot = bot

    # Command to get info about the minecraft discord dyno tags
    @command(aliases=['dynotags', 'dt'], help="Tags for dyno in maincord. Syntax f!dt [tagname] {raw/d/dyno}")
    async def dynotag(self, ctx, tagname=None, extra=None):
        if tagname != None:
            if extra != None:
                if extra.lower() == "dyno" or extra.lower() == "d" or extra.lower() == "raw":
                    await ctx.message.delete()
                    await ctx.send(dynotags[tagname])
            elif tagname in dynotags:
                try:
                    embed = discord.Embed(colour=0x00ffff, timestamp=ctx.message.created_at)
                    embed.set_footer(text=f"Requested by {ctx.author}")
                    embed.add_field(name="Tag content:", value=dynotags[tagname])
                    embed.add_field(name="Raw tag data:", value=f"```{dynotags[tagname]}```")
                    await ctx.reply(embed=embed)
                except KeyError:
                    await ctx.reply("That's not a valid tag!")
            else:
                await ctx.reply("That does not exist")
        else:
            embed = discord.Embed(colour=0x00ffff, title="Dyno tags", timestamp=ctx.message.created_at)
            embed.set_footer(text=f"Requested by {ctx.author}")
            embed.add_field(name="Tags:", value=", ".join(k for k in dynotags.keys()))
            await ctx.reply(embed=embed)
            # await ctx.send(dynotags.keys())

    # Prints all the minecraft discord dyno tags
    @command(help="Prints all tags (admin only)")
    async def alltags(self, ctx, channel: discord.TextChannel):
        if ctx.author.id in trusted or ctx.author.server_premission.administrator:
            await ctx.message.add_reaction("<a:loading:848604953953435670>")
            message = await ctx.reply(f"Deleting mesages in {channel.mention}")
            await channel.purge(limit=200)
            await message.edit(content=f"Sending all the tags in {channel.mention}")
            print(
                f'{bcolors.OKGREEN}Printing all tags in channel: {bcolors.OKCYAN}#{channel}{bcolors.OKGREEN} ID:"{bcolors.OKCYAN}{channel.id}{bcolors.OKGREEN}"{bcolors.ENDC}')
            for key in dtags.keys():
                embed = discord.Embed(colour=0x2c7bd2, title=key, description=dtags[key])
                await channel.send(embed=embed)
            await message.edit(content="Tag printing complete!")
        else:
            ctx.reply("You don't have the required permissions to perform this command! :pensive:")

    @command(help="Gets all tags")
    async def updatetags(self, ctx, channel: discord.TextChannel):
        if ctx.author.id in trusted or ctx.author.server_premission.administrator:
            await ctx.message.add_reaction("<a:loading:848604953953435670>")
            message = await ctx.reply("Getting all the tags (this might take some time)")
            channel = bot.get_channel(channel.id)
            tags = {}
            some_list = []

            async for e in channel.history(limit=200):
                some_list.append(e.content)
            some_list.reverse()  # Reverses the list

            await message.edit(content="Saving all the tags (this might take some time)")
            for index in range(0, len(some_list), 2):
                tags[some_list[index]] = some_list[index + 1]

            with open('assets/dynotags.json', 'w') as f:
                json.dump(tags, f, indent=4)
            await ctx.message.remove_reaction("<a:loading:848604953953435670>", ctx.guild.me)
            await message.edit(content="Updated all the tags!")
            await ctx.message.add_reaction("<:yes:823202605123502100>")
        else:
            ctx.reply("You don't have the required permissions to perform this command! :pensive:")


def setup(bot):
    bot.add_cog(Dyno(bot))
