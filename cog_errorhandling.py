import discord
import traceback
import sys
from discord.ext import commands
import datetime


class Errors(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.show = False

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """The event triggered when an error is raised while invoking a command.
        Parameters
        ------------
        ctx: commands.Context
            The context used for command invocation.
        error: commands.CommandError
            The Exception raised.
        """
        if hasattr(ctx.command, 'on_error'):
            return

        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        error = getattr(error, 'original', error)

        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(
                title="Command is on Cooldown",
                description='This command is on a %.2f cooldown' % error.retry_after,
                color=discord.Colour.og_blurple(),
                timestamp=datetime.datetime.utcnow()
            )
            await ctx.send(embed=em)
        elif isinstance(error, commands.MissingPermissions):
            em1 = discord.Embed(
                title="Missing Perms",
                description="Oops, it seems like you want to do something you don't have permission to!",
                color=discord.Colour.og_blurple(),
                timestamp=datetime.datetime.utcnow()
            )
            await ctx.send(embed=em1)
        elif isinstance(error, commands.BotMissingPermissions):
            em3 = discord.Embed(
                title="I don't have permission",
                description="You can't tell me to do what I can't!",
                color=discord.Colour.og_blurple(),
                timestamp=datetime.datetime.utcnow()
            )
            await ctx.send(embed=em3)
        elif isinstance(error, commands.ChannelNotFound):
            em4 = discord.Embed(
                title="Channel Not Found",
                description="I can't seem to find the channel you specified. Please try again",
                color=discord.Colour.og_blurple(),
                timestamp=datetime.datetime.utcnow()
            )
            await ctx.send(embed=em4)
        elif isinstance(error, commands.ConversionError):
            em5 = discord.Embed(
                title="Small Bug",
                description="235baron seems to have made a mistake in my code (warn him about it, it's uncomfortable to have bugs inside me)",
                color=discord.Colour.og_blurple(),
                timestamp=datetime.datetime.utcnow()
            )
            await ctx.send(embed=em5)
        elif isinstance(error, commands.EmojiNotFound):
            em6 = discord.Embed(
                title="Emoji Not Found",
                description="Either you told me to send an emoji which doesn't exist or 235baron made a mistake when creating an emoji.",
                color=discord.Colour.og_blurple(),
                timestamp=datetime.datetime.utcnow()
            )
            await ctx.send(embed=em6)
        elif isinstance(error, commands.MemberNotFound):
            em7 = discord.Embed(
                title="Member Not Found",
                description="Couldn't seem to find the member you specified (check the spelling of the name)",
                color=discord.Colour.og_blurple(),
                timestamp=datetime.datetime.utcnow()
            )
            await ctx.send(embed=em7)
        elif isinstance(error, commands.MissingRequiredArgument):
            em8 = discord.Embed(
                title="Missing a Required Option",
                description="The command you just used has an option which you HAVE to fill in (which you didn't). Please try again",
                color=discord.Colour.og_blurple(),
                timestamp=datetime.datetime.utcnow()
            )
            await ctx.send(embed=em8)
        elif isinstance(error, commands.BotMissingRole):
            em9 = discord.Embed(
                title="I'm Missing a Role",
                description="As it seems, what you wanted me to do just know requires me to have a role which I don't have",
                color=discord.Colour.og_blurple(),
                timestamp=datetime.datetime.utcnow()
            )
            await ctx.send(embed=em9)
        elif isinstance(error, commands.MissingRole):
            em10 = discord.Embed(
                title="Missing a Role",
                description="You require a certain role which you don't have.",
                color=discord.Colour.og_blurple(),
                timestamp=datetime.datetime.utcnow()
            )
            await ctx.send(embed=em10)
        elif isinstance(error, commands.RoleNotFound):
            em11 = discord.Embed(
                title="Role Not Found",
                description="Oops, couldn't find the role specified!",
                color=discord.Colour.og_blurple(),
                timestamp=datetime.datetime.utcnow()
            )
            await ctx.send(embed=em11)
        elif isinstance(error, commands.UserNotFound):
            em12 = discord.Embed(
                title="User Not Found",
                description="The user specified has not been found (check the spelling of the name)",
                color=discord.Colour.og_blurple(),
                timestamp=datetime.datetime.utcnow()
            )
            await ctx.send(embed=em12)
        elif isinstance(error, commands.TooManyArguments):
            em13 = discord.Embed(
                title="Too Many Options",
                description="Take a chillpill, bruv! Don't give me so many options!",
                color=discord.Colour.og_blurple(),
                timestamp=datetime.datetime.utcnow()
            )
            await ctx.send(embed=em13)
        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    @commands.command(name='repeat', aliases=['mimic', 'copy'], hidden=True)
    async def do_repeat(self, ctx, *, inp: str):
        """A simple command which repeats your input!
        Parameters
        ------------
        inp: str
            The input you wish to repeat.
        """
        await ctx.send(inp)

    @do_repeat.error
    async def do_repeat_handler(self, ctx, error):
        """A local Error Handler for our command do_repeat.
        This will only listen for errors in do_repeat.
        The global on_command_error will still be invoked after.
        """

        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'inp':
                await ctx.send("You forgot to give me input to repeat!")


def setup(bot):
    bot.add_cog(Errors(bot))
