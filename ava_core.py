import os
import discord
from discord import activity
from discord import member
from discord import user
from discord.enums import Status
from discord.ext import commands, tasks
from discord.flags import alias_flag_value
from discord.player import AudioSource
import requests
import json
import random
import time
from itertools import cycle


client = commands.Bot(command_prefix=['>', 'ava '])
status = cycle(["your Life", "Sytem Core Updates", "ΛVΛ's Core", "The Omega Citadel", "the Jade Palace", "the Antimatter Fusion Core"])


@client.event
async def on_ready():
  change_status.start()
  print("We've logged in as {0.user}".format(client))

#Discord Presence Container : Start
@tasks.loop(seconds=30)
async def change_status():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=next(status)))
#Discord Presence Container : End

# Quotes Command Container : Start
@ client.command('inspire')
async def on_message(message):
  if message.author == client.user:
    return

  def get_quote():
    response=requests.get('https://zenquotes.io/api/random')
    json_data=json.loads(response.text)
    quote='"*' + json_data[0]['q'] + '*"' + \
        " -" + "**" + json_data[0]['a'] + "**"
    return(quote)

  quote=get_quote()
  await message.channel.send(quote)

# Quotes Command Container : End

# 8ball Command Container : Start
@ client.command('8ball')
async def _8ball(ctx, *, question):
  responses=["as I see it, yes.", "ask again later.", "better not tell you now.", "cannot predict now.", "concentrate and ask again.",
             "don’t count on it.", "it is certain.", "it is decidedly so.", "most likely.", "my reply is no.", "my sources say no.",
             "mutlook not so good.", "outlook good.", "reply hazy, try again.", "signs point to yes.", "very doubtful.", "Without a doubt.",
             "yes!", "Yes – definitely.", "you may rely on it."]
  prefixes=["Hmm... ", "Well... "]
  await ctx.send(f'{random.choice(prefixes + responses)}')
# 8ball Command Container : End

# Ping Command Container : Start
@ client.command('ping')
async def ping(ctx):
  await ctx.send(f'Pong!{round(client.latency*1000)}ms')
# Ping Command Container : End

# Purge Command : Start
@ client.command()
async def clear(ctx, amount=5):
  await ctx.channel.purge(limit=amount)
  await ctx.send(f'Purged {amount} messages!')
  time.sleep(3)
  await ctx.channel.purge(limit=1)
# Purge Command Container : End

# Kick Command Container : Start
@ client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  if reason == None:
    reason="nothing."
  await ctx.send(f'Kicked {member} for {reason}')
# Kick Command Container : End

# Ban Command Container : Start
@client.command(aliases=['bun'])
async def ban(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  if reason == None:
    reason="something which is sus."
  await ctx.send(f'Banned {member} for {reason}')
# Kick Command Container : End

# UnBan Command Container : Start
@client.command()
async def unban(ctx, *, member):
  banned_members = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_members:
    user = ban_entry.user

    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f"{user.name}#{user.discriminator} has been Unbanned")
# UnBan Command Container : End

# Cogs Container : Start
# Load
@client.command()
async def load(ctx, extention):
  client.load_extention(f'cogs.{extention})')

#Unload
@client.command()
async def unload(ctx, extention):
  client.unload_extention(f'cogs.{extention}')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

# Cogs Container : End





















client.run('ODY1MTI1NTEwODI0NzIyNDQy.YO_c6w.uJtchskutoT3rxxfMPBxY9mrFXI')
