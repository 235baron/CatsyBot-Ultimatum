import discord
from discord.ext import commands
import asyncio
import datetime


class Utilities(commands.Cog):
    """Only for Admins"""

    def __init__(self, client):
        self.guild = None
        self.author = None
        self.client = client
        self.show = True

    @commands.Cog.listener()
    async def on_ready(self):
        print("Admin cog ready")

    async def cog_check(self, ctx):
        return ctx.channel.permissions_for(ctx.author).manage_channels

    @commands.command(pass_context=True, aliases=["purge"])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, limit: int):
        """Clears some messages"""
        await ctx.channel.purge(limit=limit)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lockdown(self, ctx, role: discord.Role):
        """Locks a channel"""
        await ctx.channel.set_permissions(role, send_messages=False, embed_links=False, attach_files=False)
        em = discord.Embed(title="", description=ctx.channel.mention + " ***is now in lockdown.***",
                           color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=em)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx, role: discord.Role):
        """Unlocks a channel"""
        await ctx.channel.set_permissions(role, send_messages=True, embed_links=True, attach_files=True)
        em = discord.Embed(title="", description=ctx.channel.mention + " ***is now unlocked.***",
                           color=discord.Colour.blurple(),
                           timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=em)

    @commands.command(pass_context=True)
    async def giverole(self, ctx, user: discord.Member, role: discord.Role):
        """Gives a role to a user"""
        await user.add_roles(role)
        em = discord.Embed(title="",
                           description=f"hey {ctx.author.name}, {user.name} has been giving a role called: {role.name}",
                           color=discord.Colour.blurple(),
                           timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=em)

    @commands.command(aliases=['make_role'])
    @commands.has_permissions(manage_roles=True)
    async def create_role(self, ctx, *, name):
        """Creates a role"""
        guild = ctx.guild
        await guild.create_role(name=name)
        em = discord.Embed(title="", description=f'Role `{name}` has been created', color=discord.Colour.blurple(),
                           timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=em)

    @commands.command(name='create-channel')
    async def create_channel(self, ctx, channel_name='new-channel'):
        """Creates a channel"""
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if not existing_channel:
            print(f'Creating a new channel: {channel_name}')
            await guild.create_text_channel(channel_name)

    @commands.command(pass_context=True)
    async def chnick(self, ctx, member: discord.Member, nick):
        """Changes a Member`s nickname"""
        await member.edit(nick=nick)
        em = discord.Embed(title="", description=f'Nickname was changed for {member.mention} ',
                           color=discord.Colour.blurple(),
                           timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=em)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason="No reason provided"):
        await user.kick(reason=reason)
        kick = discord.Embed(
            title=f":boom: Kicked {user.name}!",
            description=f"Reason: {reason}\nBy: {ctx.author.mention}",
            color=discord.Colour.blurple(),
            timestamp=datetime.datetime.utcnow()
        )
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await user.send(embed=kick)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason="No reason provided"):
        await user.ban(reason=reason)
        ban = discord.Embed(
            title=f":boom: Banned {user.name}!",
            description=f"Reason: {reason}\nBy: {ctx.author.mention}",
            color=discord.Colour.blurple(),
            timestamp=datetime.datetime.utcnow()
        )
        await ctx.message.delete()
        await ctx.channel.send(embed=ban)
        await user.send(embed=ban)

    @commands.command(name='unban')
    async def _unban(self, ctx, id: int):
        user = await self.client.fetch_user(id)
        await ctx.guild.unban(user)
        em = discord.Embed(
            title=f":boom: Unbanned {user.name}!",
            description=f"Kind {ctx.author} has unbanned {user.name}",
            color=discord.Colour.blurple(),
            timestamp=datetime.datetime.utcnow()
        )
        await ctx.send(embed=em)

    @commands.command()
    async def mute(self, ctx, member: discord.Member):
        """Mutes a member"""
        role = ctx.guild.get_role(784168505498533920)
        guild = ctx.guild
        if role not in guild.roles:
            perms = discord.Permissions(send_messages=False, speak=False)
            await guild.create_role(name="Muted", permissions=perms)
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            await member.add_roles(role)
            embed = discord.Embed(
                description=f"{member} was muted.", colour=discord.Colour.blurple(),
                timestamp=datetime.datetime.utcnow()
            )
            await ctx.send(embed=embed)
        else:
            await member.add_roles(role)
            embed = discord.Embed(
                description=f"{member} was muted.", colour=discord.Colour.blurple(),
                timestamp=datetime.datetime.utcnow()
            )
            await ctx.send(embed=embed)

    @commands.command(description="Unmutes a specified user.")
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        embed = discord.Embed(title="Unmuted", description=f" unmuted-{member.mention}",
                              colour=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def tempmute(self, ctx, member: discord.Member, time):
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
        tempmute = int(time[0]) * time_convert[time[-1]]
        await ctx.message.delete()
        await member.add_roles(muted_role)
        embed = discord.Embed(description=f"✅ **{member.display_name}#{member.discriminator} muted successfuly**",
                              color=discord.Color.blurple(), timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=embed)
        await asyncio.sleep(tempmute)
        await member.remove_roles(muted_role)


def setup(bot):
    bot.add_cog(Utilities(bot))
