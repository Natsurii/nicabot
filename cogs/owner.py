from discord.ext import commands
import asyncio
import traceback
import discord
import inspect
import textwrap
from contextlib import redirect_stdout
import io

class OwnerCog:

    def __init__(self, bot):
        self.bot = bot

    def is_owner(ctx):
        return ctx.message.author.id == 305998511894167552
    
    # Hidden means it won't show up on the default help.
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def cog_load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='unload', hidden=True)
    @commands.check(is_owner)
    async def cog_unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='reload', hidden=True)
    @commands.check(is_owner)
    async def cog_reload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')
    @commands.command(name='logout', hidden=True)
    @commands.check(is_owner)
    async def logout(self, ctx):
        await ctx.send(f'Goodbye Senpai {ctx.author} UmU')
        await ctx.bot.logout()

   

def setup(bot):
    bot.add_cog(OwnerCog(bot))
