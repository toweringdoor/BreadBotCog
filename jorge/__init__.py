from .core import JorgeSetup


async def setup(bot):
    bot.add_cog(JorgeSetup(bot))