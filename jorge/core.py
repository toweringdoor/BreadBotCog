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
    async def bitcoin(self, ctx):
        url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
        raw_response = requests.get(url)
        response = raw_response.text
        response = json.loads(response)
        await ctx.send("Bitcoin price is: $" + response['bpi']['USD']['rate'])

    @commands.command()
    async def dj(self, ctx):
        await ctx.send("<:dj:730289249122910248>")

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
            url="https://cdn.discordapp.com/attachments/661670376744550416/730246288896950334/angry_pog.jpg"
        )
        await ctx.send(embed=embed, content="jacob is mega dumb")

    @commands.command()
    async def putinwalk(self, ctx):
        embed = discord.Embed(color=0x000000)
        embed.set_image(
            url="https://media.discordapp.net/attachments/620444581871353868/733571027929399326/8680_PutinWideWalking.gif"
        )
        await ctx.send(embed=embed, content="putin do be walking tho :flushed:")

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