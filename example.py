import discord
from discord.ext import commands

class Examples(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is Online.')
    
    
def setup(client):
    client.add_cog(Examples(client))