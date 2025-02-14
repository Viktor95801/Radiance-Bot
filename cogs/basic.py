# basic.py
import discord
from discord.ext import commands
from discord import app_commands as apc

from token_1 import DC_GUILD_ID

class Basic(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="ping")
    async def ping_2(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")
async def setup(bot):
    tree = bot.tree
    @tree.command(name="ping", description="Returns the bot latency in ms.", guild=discord.Object(DC_GUILD_ID))
    async def ping(interaction: discord.Interaction):
        await interaction.response.send_message(f"Pong! {round(bot.latency * 1000)}ms")
    await bot.add_cog(Basic(bot))