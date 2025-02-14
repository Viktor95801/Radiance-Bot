## INTERNAL ----------------------------------------------
import token_1

## EXTERNAL ----------------------------------------------
import discord as dc
from discord.ext import commands
from discord import app_commands as apc

import os

def get_cogs(path: str) -> list[str]:
    out = []
    print("Cogs: ", end="")
    for file in os.listdir(path):
        if file.endswith(".py"):
            out.append(file.replace(".py", ""))
            print(file.replace(".py", ""), end=", ")
    print("\n")
    
    return out

cogs: list[str] = get_cogs("cogs")
bot = commands.Bot(command_prefix="r!", intents=dc.Intents.all())

@bot.event
async def on_ready():
    print(f"\n\nLogged in as {bot.user.name}#{bot.user.discriminator} (ID: {bot.user.id})")
    print("Guilds: ", end="")
    if len(bot.guilds) == 0:
        print("None")
    else:
        for guild in bot.guilds:
            print(f"{guild.name} (ID: {guild.id})", end=", ")
        print("\n")
    for cog in cogs:
        await bot.load_extension(f"cogs.{cog}")
    await bot.tree.sync(guild=dc.Object(id=token_1.DC_GUILD_ID))
    
    print(f"{[next(bot.tree.walk_commands(guild=dc.Object(id=token_1.DC_GUILD_ID))).name for _ in bot.tree.walk_commands(guild=dc.Object(id=token_1.DC_GUILD_ID))]}\n")
        
    game = dc.Game("r!help")
    await bot.change_presence(status=dc.Status.idle, activity=game)

bot.run(token_1.DC_TOKEN, reconnect=True)