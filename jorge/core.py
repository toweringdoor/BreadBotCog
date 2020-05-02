import discord
from redbot.core import commands, checks
import asyncio
import aiohttp
import json
import requests

BaseCog = getattr(commands, "Cog", object)


class JorgeSetup(BaseCog):
    """
    For thou
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(
            "Hey! What can I help you with? (If you need to ask any questions about this bot, please DM my creator ToweringDoor#3668)"
        )

    @commands.command()
    async def genesis(self, ctx):
        await ctx.send("gen is a big bot at rl")
        print("Gen is pretty bad ngl")

    @commands.command()
    async def test(self, ctx):
        await ctx.send("testing.... 1...2...3")
        print("testcomplete")

    @commands.command()
    async def whyamimakingallthesecommands(self, ctx):
        await ctx.send("i don't even know")
        print("?")

    @commands.command()
    async def connection(self, ctx):
        await ctx.send("I am successfully connected to Discord")
        print("Discord connect successful")

    @commands.command()
    async def dj(self, ctx):
        embed = discord.Embed(color=0x000000)
        embed.set_image(url="https://cdn.discordapp.com/emojis/606483938176925697.png?v=1")
        await ctx.send(embed=embed)

    @commands.command()
    async def xavier(self, ctx):
        await ctx.send(
            "XAVIER = TRYHARD XAVIER = TRYHARD XAVIER = TRYHARD https://youtu.be/mRqOu150eFs"
        )
        print("XavierDONE")

    @commands.command()
    async def usinfo(self, ctx, user: discord.Member):
        embed = discord.Embed(
            title="{}'s info".format(user.name),
            description="Here's what I could find.",
            color=0x00FF00,
        )
        embed.add_field(name="Name", value=user.name, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Status", value=user.status, inline=True)
        embed.add_field(name="Highest role", value=user.top_role)
        embed.add_field(name="Joined", value=user.joined_at)
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def jacob(self, ctx):
        embed = discord.Embed(color=0x000000)
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/538926565774458890/637785286482460672/unknown.png"
        )
        await ctx.send(embed=embed, content="jacob is mega dumb")

    @commands.command()
    async def doinyamom(self, ctx):
        await ctx.send("doin ya mom doin doin ya mom")

    @commands.command()
    async def pig(self, ctx):
        await ctx.send(":bacon:")

    @commands.command()
    async def joemama(self, ctx):
        await ctx.send("no u")

    @commands.command()
    async def bruh(self, ctx):
        await ctx.send(":loud_sound: bruh")

    @commands.command()
    async def guildinfo(self, ctx): # Had to rename, since serverinfo is already a command
        embed = discord.Embed(name="{}'s info".format(ctx.guild.name), description="Here's what I could find.", color=0x00ff00)
        embed.set_author(name="ToweringDoor")
        embed.add_field(name="Name", value=ctx.guild.name, inline=True)
        embed.add_field(name="ID", value=ctx.guild.id, inline=True)
        embed.add_field(name="Roles", value=len(ctx.guild.roles), inline=True)
        embed.add_field(name="Members", value=len(ctx.guild.members), inline=True)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def secret1(self, ctx):
        await ctx.send("https://gyazo.com/96f189b524ad81c63d9be2882594e24d")

    @commands.command()
    async def lenny(self, ctx):
        await ctx.send("( ͡° ͜ʖ ͡°)")

    @commands.command()
    async def uflip(self, ctx, user: discord.Member): #rename due to already use of command. u
        await ctx.send("(╯°□°）╯︵ {}".format(user.name))
        print("flipDONE")

    @commands.command()
    async def lex(self, ctx):
        await ctx.send("lex is mega gamer")

    @commands.command()
    async def hoesmad(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/540342714785464341/626531703648944138/hoesmad.jpg")

    @commands.command()
    async def invitelink(self, ctx):
        await ctx.send("https://discordapp.com/oauth2/authorize?&client_id=592543480547639299&scope=bot&permissions=470019135")
        print("LinkDONE")

    @commands.command()
    async def bitcoin(self, ctx):
        url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
        raw_response = requests.get(url)
        response = raw_response.text
        response = json.loads(response)
        await ctx.send("Bitcoin price is: $" + response['bpi']['USD']['rate'])

    @commands.command()
    async def list_servers(self, ctx):
        await ctx.send("This command does not send the server list to the chat. Instead, it sends the list to my creator or someone who has access to the bot.py file.")
        print("Current Servers:")
        for server in ctx.bot.guilds:
            print(server.name)

    @commands.command()
    async def cheeseburger(self, ctx):
        await ctx.send("Here ya go! :hamburger:")
        print("BurgerDone")

    @commands.command()
    async def vibecheck(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=PLOPygVcaVE&t")
        print("vibeDONE")

    @commands.command()
    async def cheeseburger2(self, ctx):
        await ctx.send("https://giphy.com/gifs/mcdonalds-cheeseburger-11KjGKVlosnuw0")
        print("Burger2Done")

    @commands.command()
    async def genesis2(self, ctx):
        await ctx.send("yea i agree")
