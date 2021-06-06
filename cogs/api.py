from assets.stuff import *


class Api(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(aliases=['def'], help="Makes the bot say things")
    async def define(self, ctx, word, lang="en_US"):
        resp = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/{lang}/{word}')
        resp = resp.json()

        """
        if resp["title"] == "No Definitions Found":
            await ctx.reply(f"Couldnt find a definition for `{word}`")
            return
        """

        resp = resp[0]["meanings"]
        embed = discord.Embed(title=f"Defenition of the word {word}")

        for i in resp:
            for e in i["definitions"]:
                try:
                    embed.add_field(name=i["partOfSpeech"], value=f'**Defenition:** `{e["definition"]}`\n**Example:** `{e["example"]}`')
                except KeyError:
                    try:
                        embed.add_field(name=i["partOfSpeech"], value=f'Defenition: `{e["definition"]}`')
                    except KeyError:
                        embed.add_field(name="e", value=f'Defenition: `{e["definition"]}`')

        await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(Api(bot))
