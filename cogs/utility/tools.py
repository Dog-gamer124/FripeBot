from assets.stuff import *


class Tools(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(aliases=['Exec'], help="Executes code")
    async def execute(self, ctx, *, code):
        #    if ctx.author.id in trusted:
        if ctx.author.id == ownerid:  # Checking if the person is the owner
            if code is None:
                await ctx.reply("I cant execute nothing")
                return
            code = code.replace('```py', '').replace('```', '').strip()
            code = '\n'.join([f'\t{line}' for line in code.splitlines()])
            function_code = (
                'async def exec_code(self, ctx):\n'
                f'  {code}')
            try:
                exec(function_code)
                output = await locals()['exec_code'](self, ctx)
                if output:
                    formatted_output = '\n'.join(output) if len(code.splitlines()) > 1 else output
                    await ctx.reply(embed=discord.Embed(colour=0xff0000,
                                                        timestamp=ctx.message.created_at,
                                                        title="Your code failed ran successfully!",
                                                        description=f"```{formatted_output}```"))
                await ctx.message.add_reaction("<:yes:823202605123502100>")
            except Exception as error:
                await ctx.message.add_reaction("<:no:823202604665929779>")
                await ctx.reply(embed=discord.Embed(colour=0xff0000,
                                                    timestamp=ctx.message.created_at,
                                                    title="Your code failed to run!",
                                                    description=f"```{error}```"))
        else:
            await ctx.message.add_reaction("🔐")

    @command(aliases=['Eval'], help="Evaluates things")
    async def evaluate(self, ctx, *, arg=None):
        if arg is None:
            await ctx.reply("I cant evaluate nothing")
            return
        if ctx.author.id in trusted:  # Checks if the user is trusted
            # Checks if the bots token is in the output
            if os.getenv('TOKEN') in str(eval(arg)):
                # Sends a randomly generated string that looks like a token
                await ctx.reply \
                    (''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.-_", k=59)))
            else:
                try:
                    await ctx.reply(eval(arg))  # Actually Evaluates
                    await ctx.message.add_reaction("<:yes:823202605123502100>")
                except Exception as error:
                    await ctx.message.add_reaction("<:no:823202604665929779>")
                    await senderror(ctx, Exception)
        else:
            await ctx.message.add_reaction("🔐")


def setup(bot):
    bot.add_cog(Tools(bot))
