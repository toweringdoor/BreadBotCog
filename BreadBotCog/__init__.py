from .core import BreadBot


async def setup(bot):
    bot.add_cog(BreadBot(bot))