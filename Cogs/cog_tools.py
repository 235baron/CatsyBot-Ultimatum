import discord
from discord.ext import commands
import datetime
from googletrans import Translator


snipe_message_content = None
snipe_message_author = None
snipe_message_id = None


class Tools(commands.Cog):
    """All commands which tell you info are here"""
    def __init__(self, client):
        self.guild = None
        self.author = None
        self.client = client
        self.show = True

    # @commands.Cog.listener()
    # async def on_message_delete(self, message):
    #
    #     global snipe_message_content
    #     global snipe_message_author
    #     global snipe_message_id
    #
    #     snipe_message_content = message.content
    #     snipe_message_author = message.author.name
    #     snipe_message_id = message.id
    #     await asyncio.sleep(60)
    #
    #     if message.id == snipe_message_id:
    #         snipe_message_author = None
    #         snipe_message_content = None
    #         snipe_message_id = None
    #
    # @commands.slash_command(guild_ids=[689859328768999443])
    # async def snipe(self, message):
    #     if snipe_message_content is None:
    #         em = discord.Embed(title="", description="There`s nothing to snipe.", color=discord.Colour.blurple(),
    #                            timestamp=datetime.datetime.utcnow())
    #         await message.channel.send(embed=em)
    #     else:
    #         embed = discord.Embed(description=f"{snipe_message_content}", color=discord.Colour.blurple())
    #         embed.set_footer(text=f"Asked by {message.author.name}#{message.author.discriminator}")
    #         embed.set_author(name=f"{snipe_message_author}")
    #         await message.channel.respond(embed=embed)
    #         return

    @commands.slash_command(guild_ids=[689859328768999443])
    async def ping(self, ctx):
        """PING PONG"""
        em = discord.Embed(title="", description=f":ping_pong: Pong with {str(round(self.client.latency, 2))}", color=discord.Colour.blurple(),
                           timestamp=datetime.datetime.utcnow())
        await ctx.respond(embed=em)

    @commands.slash_command(guild_ids=[689859328768999443])
    async def invite(self, ctx):
        """Gives you the invite link"""
        example = discord.Embed(
            title="Invite Link",
            url="https://discord.com/oauth2/authorize?client_id=796082374248103958&scope=bot&permissions=403172438",
            description="Click the title of this message to invite CatsyBot to your server.",
            color=discord.Colour.blurple(),
            timestamp=datetime.datetime.utcnow()
        )
        await ctx.respond(embed=example)

    # @commands.command()
    # async def servers(self, ctx):
    #     activeservers = self.client.guilds
    #     for guild in activeservers:
    #         await ctx.send(guild.name)
    #         print(guild.name)

    # @commands.command(aliases=["cmd"], guild_ids=[797774019402268682])
    # async def suggest_cmd(self, ctx, command, *, description):
    #     """Suggest a command. Note: the suggestions go to the Test server"""
    #     embed = discord.Embed(title='Command Suggestion',
    #                           description=f'Suggested by: {ctx.author.mention}\nCommand Name: *{command}*',
    #                           color=discord.Color.green())
    #     embed.add_field(name='Description', value=description)
    #     if ctx.channel.name == "ideas-and-feedback":
    #         channel = ctx.guild.get_channel(798154347678400583)
    #         msg = await channel.send(embed=embed)
    #         await msg.add_reaction('👍')
    #         await msg.add_reaction('👎')

    @commands.slash_command(guild_ids=[689859328768999443])
    async def testserver(self, ctx):
        """Invites you to the test server"""
        example = discord.Embed(
            title="Invite Link",
            url="https://discord.gg/ajqAeW4MHp",
            description="Click the Title to get invited to Darth Cat's test server",
            color=discord.Colour.blurple(),
            timestamp=datetime.datetime.utcnow()
        )
        await ctx.respond(embed=example)

    @commands.slash_command(guild_ids=[689859328768999443], aliases=["mc"])
    async def member_count(self, ctx):
        """Tells you how many members there are"""
        a = ctx.guild.member_count
        b = discord.Embed(title=f"Members in {ctx.guild.name}", description=a, color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
        await ctx.respond(embed=b)

    @commands.slash_command(guild_ids=[689859328768999443])
    async def serverinfo(self, ctx):
        """Tells you some info about the current server"""
        name = str(ctx.guild.name)
        description = "You can't keep up with the server changes, huh?"

        owner = str(ctx.guild.owner)
        identification = str(ctx.guild.id)
        region = str(ctx.guild.region)
        count = str(ctx.guild.member_count)
        role_count = len(ctx.guild.roles)
        list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]

        embed = discord.Embed(
            title=name + " Server Information",
            description=description,
            color=discord.Colour.blurple(),
            timestamp=datetime.datetime.utcnow()
        )
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=identification, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=count, inline=True)
        embed.add_field(name="Role Count", value=str(role_count), inline=True)
        embed.add_field(name='Bots:', value=(', '.join(list_of_bots)), inline=True)
        embed.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y at %H:%M:%S'), inline=False)

        await ctx.respond(embed=embed)

    @commands.slash_command(description="Keep in mind, lang = the language you want to translate to", guild_ids=[689859328768999443])
    async def translate(self, ctx, lang, *, thing):
        translator = Translator()
        translation = translator.translate(thing, dest=lang)
        await ctx.respond(translation.text)

    # @commands.command(case_insensitive=True, aliases=["remind", "remindme", "remind_me"])
    # @commands.bot_has_permissions(attach_files=True, embed_links=True)
    # async def reminder(self, ctx, time, *, reminder):
    #     print(time)
    #     print(reminder)
    #     embed = discord.Embed(color=0x55a7f7, timestamp=datetime.datetime.utcnow())
    #     embed.set_footer(
    #         text="If you have any questions, suggestions or bug reports, please join our support Discord Server: https://discord.gg/KsYMRP9dW7",
    #         icon_url=f"{self.client.user.avatar_url}")
    #     seconds = 0
    #     if reminder is None:
    #         embed.add_field(name='Warning',
    #                         value='Please specify what do you want me to remind you about.')  # Error message
    #     if time.lower().endswith("d"):
    #         seconds += int(time[:-1]) * 60 * 60 * 24
    #         counter = f"{seconds // 60 // 60 // 24} days"
    #     if time.lower().endswith("h"):
    #         seconds += int(time[:-1]) * 60 * 60
    #         counter = f"{seconds // 60 // 60} hours"
    #     elif time.lower().endswith("m"):
    #         seconds += int(time[:-1]) * 60
    #         counter = f"{seconds // 60} minutes"
    #     elif time.lower().endswith("s"):
    #         seconds += int(time[:-1])
    #         counter = f"{seconds} seconds"
    #     if seconds == 0:
    #         embed.add_field(name='Warning',
    #                         value='Please specify a proper duration, send `reminder_help` for more information.')
    #     elif seconds < 300:
    #         embed.add_field(name='Warning',
    #                         value='You have specified a too short duration!\nMinimum duration is 5 minutes.')
    #     elif seconds > 7776000:
    #         embed.add_field(name='Warning',
    #                         value='You have specified a too long duration!\nMaximum duration is 90 days.')
    #     else:
    #         await ctx.send(f"Alright, I will remind you about {reminder} in {counter}.")
    #         await asyncio.sleep(seconds)
    #         await ctx.send(f"Hi, you asked me to remind you about {reminder} {counter} ago.")
    #         return
    #     await ctx.send(embed=embed)
    #
    # @commands.command(name="reminder_help")
    # async def reminder_help(self, ctx):
    #     """Help about reminders"""
    #     await ctx.send(f"Instead of writing the name of duration, write the first letter of the duration name.")


def setup(bot):
    bot.add_cog(Tools(bot))
