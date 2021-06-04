import discord, asyncio
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix  = ".", intents = intents)


@client.command()
@commands.cooldown(1, 60 * 60, commands.BucketType.user)
async def ticket(ctx):
    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages = False),
        ctx.author: discord.PermissionOverwrite(read_messages = True)
    }
    await ctx.guild.create_text_channel(name = f"ticket-{ctx.author.name}", overwrites = overwrites)
    success = discord.Embed(
        description = f"{ctx.author.mention} your ticket has been created.",
        color = discord.Color.green()
    )
    await ctx.author.send(embed = success)

@ticket.error
async def error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.author.send("Please wait **1 hour** to make another ticket.") 
    else:
        print(error)
client.run("TOKEN")