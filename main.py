import discord
# from discord.ui import Button, View
from discord.ext import commands
# from discord.ext import ipc
import random

# greetings = [
#     "Hello",
#     "Hi",
#     "Greetings",
#     "Hello there",
#     "So...",
#     "*snoring* *looks up* Oh hello"
# ]


# def get_prefix(client, message):
#     with open("prefixes.json", "r") as f:
#         prefixes = json.load(f)
#     return prefixes[str(message.guild.id)]


# class MyBot(commands.Bot):
# 	def __init__(self, *args, **kwargs):
# 		super().__init__(*args, **kwargs)
# 		self.ipc = ipc.Server(self, secret_key="super secret key")
#
#
# 	async def on_ready(self):
# 		"""Called upon the READY event"""
# 		print("Bot is ready.")
#
#
# 	async def on_ipc_ready(self):
# 		"""Called upon the IPC Server being ready"""
# 		print("Ipc server is ready.")
#
#
# 	async def on_ipc_error(self, endpoint, error):
# 		"""Called upon an error being raised within an IPC route"""
# 		print(endpoint, "raised", error)


# menu = DefaultMenu(page_left="⬅", page_right="➡", remove="🛑", active_time=5)
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", owner_id=762628291508043786, intents=intents)
# bot = MyBot(command_prefix=get_prefix, owner_id=762628291508043786, intents=intents)
bot.remove_command("help")
ending_note = "Please report any bugs at the Test Server\nFor command {help.clean_prefix}{help.invoked_with}"
color = discord.Colour.blue()
# bot.help_command = PrettyHelp(menu=menu, ending_note=ending_note, color=color)
bot.load_extension('Cogs.cog_errorhandling')
bot.load_extension('Cogs.cog_tools')
bot.load_extension('Cogs.cog_fun')
bot.load_extension('Cogs.cog_inventory')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="/help | on " + str(len(bot.guilds)) + " Servers.", type=0))
    print('Darth Cats is online')
    print('██████╗░░█████╗░████████╗  ██╗░██████╗  ██████╗░███████╗░█████╗░██████╗░██╗░░░██╗')
    print('██╔══██╗██╔══██╗╚══██╔══╝  ██║██╔════╝  ██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗░██╔╝')
    print('██████╦╝██║░░██║░░░██║░░░  ██║╚█████╗░  ██████╔╝█████╗░░███████║██║░░██║░╚████╔╝░')
    print('██╔══██╗██║░░██║░░░██║░░░  ██║░╚═══██╗  ██╔══██╗██╔══╝░░██╔══██║██║░░██║░░╚██╔╝░░')
    print('██████╦╝╚█████╔╝░░░██║░░░  ██║██████╔╝  ██║░░██║███████╗██║░░██║██████╔╝░░░██║░░░')
    print('                        %%%%%%%@@')
    print('                   %%%%%%%%%%%%%%%%@@')
    print('                 %%%%%%%%%%%%%%%%%%%%@@')
    print('                %%%%%%%%%%%%')
    print('               @%%%%%%%%     +::::::::----+@')
    print('               @%%%%%%%  @=::::::::::.........:')
    print('              @@%%%%%%   ==:::::::::::::::....:%')
    print('              @@%%%%%  @===:::::::::::::::::::=')
    print('     %%%%%%   @@%%%%%@  ======+:::::::::::::*==')
    print('    %%%%%%%   @@%%%%%%%  %=====================')
    print('    @@@@@@@   @@@%%%%%%%%   %================@')
    print('    @@@@@@@   @@@%%%%%%%%%')
    print('    @@@@@@@   @@@%%%%%%%%%%%@@             %%%')
    print('    @@@@@@@   @@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print('    @@@@@@@   @@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print('    @@@@@@@   @@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print('    @@@@@@@   @@@@%%%%%%%%%%%%%%%%%%%%%%%%%@@')
    print('    @@@@@@@   @@@@@%%%%%%%%%%%%%%%%%%%%%%%@@@')
    print('    @@@@@@@   @@@@@@@%%%%%%%%%%%%%%%%%%%%@@@@')
    print('    @@@@@@@   @@@@@@@@@@%%%%%%%%%%%%%%@@@@@@@')
    print('     @@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('      @@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('              @@@@@@@@@@@@             @@@@@')
    print('              @@@@@@@@@@@           @@@@@@@')
    print('              @@@@@@@@@@@        @@@@@@@@@@')
    print('              @@@@@@@@@@@        @@@@@@@@@@')
    print('              @@@@@@@@@@@         @@@@@@@@')
    print('               @@@@@@@@@@')
    print('               @@@@@@@@')


@bot.listen()
async def on_message(message):
    if message.content.startswith('Hello there'):
        msg = 'General Kenobi... you are a bold one'.format(message)
        await message.channel.send(msg)


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@bot.listen
async def on_member_remove(member):
    await bot.get_channel(798111019255595008).send(
        f"{member.name} has died in the battlefield. May he rest in peace...")


# @bot.command()
# async def help(ctx, category)
# 	pass


@bot.slash_command(guild_ids=[689859328768999443], hidden=True)
async def test(ctx):
    em = discord.Embed(title="", description="hi", color=discord.Colour.dark_teal())
    await ctx.respond(embed=em)
    await ctx.respond("there")


@bot.slash_command(description="Categories: Fun, Tools, Economy", guild_ids=[689859328768999443])
async def help(ctx, category):
    if category == "Fun":
        em = discord.Embed(title="CatsyBot Help", color=discord.Colour.blurple())
        em.add_field(name="/coinflip", value="Wanna bet? Flip a coin!")
        em.add_field(name="/brooklyn_99", value="Quotes from this well-beloved TV show.")
        em.add_field(name="/fun_fact", value="Another few funt facts!")
        em.add_field(name="/say", value="Be anonymous...")
        em.add_field(name="/meme", value="Check some memes! (family friendly)")
        em.add_field(name="/prequel", value="Some Star Wars memes")
        em.add_field(name="/ko", value="Knockout the person you hate!")
        em.add_field(name="/choose", value="Can't choose? Let the bot choose for you!")
        em.add_field(name="/ssp", value="Rock, Paper, Scissors... Shoot!")
        em.add_field(name="/minesweeper", value="Another electronized board game")
        await ctx.respond(embed=em)
    elif category == "Tools":
        em = discord.Embed(title="CatsyBot Help", color=discord.Colour.blurple())
        em.add_field(name="/help", value="What you are seeing now")
        em.add_field(name="/ping", value="Check how fast the bot will reply!")
        em.add_field(name="/invite", value="Invite the bot! (not pushing but pls upvote bot)")
        em.add_field(name="/testserver", value="Invite for the CatsyBot Test Server")
        em.add_field(name="/member_count", value="See the server's member count")
        em.add_field(name="/serverinfo", value="Check the server's general information")
        await ctx.respond(embed=em)
    elif category == "Economy":
        em = discord.Embed(title="CatsyBot Help", color=discord.Colour.blurple())
        em.add_field(name="/balance", value="Shows how much money you have")
        em.add_field(name="/beg", value="Wait, you actually consider using this command? haha beggar")
        em.add_field(name="/work", value="Gain a decent amount of money respectably")
        em.add_field(name="/withdraw", value="Transfers some money from the bank to cash")
        em.add_field(name="/deposit", value="Dump all your cash in the bank")
        em.add_field(name="/pay", value="Pay your debts with another user")
        em.add_field(name="/sell", value="Sell some of your items if you're desperate")
        em.add_field(name="/slots", value="Bet some money (WARNING: you can lose a lot)")
        em.add_field(name="/rob", value="Rob someone (they won't like it)")
        em.add_field(name="/shop", value="Check out some cool stuff you can buy")
        em.add_field(name="/buy", value="Buy some of the sick stuff you saw in the shop")
        em.add_field(name="/inventory", value="Admire the stuff you bought")
        em.add_field(name="/use", value="Use some of the stuff you bought")
        em.add_field(name="/race", value="Race with your friends (you need a ferrari or bugatti to unlock this)")
        em.add_field(name="/leaderboard", value="See if you're the richest person in CatEconomy")
        em.add_field(name="/add_money", value="Only for admins (to anyone who ain't admin, it will say that bot didn't respond)")
        await ctx.respond(embed=em)


@bot.slash_command(guild_ids=[689859328768999443])
async def button_test(ctx):
    choices = [
        "Pizza",
        "Hamburger",
        "Hotdog",
        "Apple",
        "Orange",
        "Donut"
    ]
    button = discord.ui.Button(label=f"{random.choice(choices)}", style=discord.ButtonStyle.primary, emoji="🍩")
    button1 = discord.ui.Button(label=f"{random.choice(choices)}", style=discord.ButtonStyle.primary, emoji="🍩")

    async def button_callback(interaction):
        await interaction.response.send_message("I also really like that!")

    button.callback = button_callback
    button1.callback = button_callback
    view = discord.ui.View()
    view.add_item(button)
    view.add_item(button1)
    await ctx.send("Which is tastier?", view=view)


# @bot.listen()
# async def on_message(message):
#     greetings = [
#         "Hello",
#         "hello",
#         "Hi",
#         "hi",
#         "Hello there",
#         "hello there",
#         "Wassup",
#         "Hi there",
#         "Why hello!",
#         "hey",
#         "Yo wassup",
#         "wassup bruv",
#         "sup"]
#     if [i for i in greetings if message.content.startswith(i)]:
#         if message.author == bot.user:
#             return
#         replies = [
#             "Hi there",
#             "Why hello!",
#             "hey",
#             "Yo wassup",
#             "wassup bruv",
#             "Ah, someone trying to revive the chat...",
#             "sup",
#             "Hello",
#             "hello",
#             "Hi",
#             "hi",
#             "Hello there",
#             "hello there",
#             "Wassup"
#         ]
#         await message.channel.send(random.choice(replies))
#
#
# @bot.event
# async def on_guild_join(guild):
#     with open("prefixes.json", "r") as f:
#         prefixes = json.load(f)
#     prefixes[str(guild.id)] = "."
#     with open("prefixes.json", "w") as f:
#         json.dump(prefixes, f)
#
#
# @bot.slash_command(description="If you don't have Admin perms, this command won't work, remember...",
#                    guild_ids=[689859328768999443], hidden=True)
# @commands.has_permissions(administrator=True)
# async def changeprefix(ctx, prefix):
#     with open("prefixes.json", "r") as f:
#         prefixes = json.load(f)
#     prefixes[str(ctx.guild.id)] = prefix
#     with open("prefixes.json", "w") as f:
#         json.dump(prefixes, f)
#     await ctx.send(f"The prefix has been changed to {prefix}")
#
#
# @bot.event
# async def on_message(msg):
#     try:
#         if msg.mentions[0] == bot.user:
#             with open("prefixes.json", "r") as f:
#                 prefixes = json.load(f)
#             pre = prefixes[str(msg.guild.id)]
#             await msg.channel.send(f"My prefix for this server is {pre}")
#     except:
#         pass
#     await bot.process_commands(msg)
#
#
# @bot.ipc.route()
# async def get_guild_count(data):
# 	return len(bot.guilds)
#
#
# @bot.ipc.route()
# async def get_guild_ids(data):
# 	final = []
# 	for guild in bot.guilds:
# final.append(guild.id)
# 		return final

#
# @bot.ipc.route()
# async def get_guild(data):
# 	guild = bot.get_guild(data.guild_id)
# 	if guild is None: return None
#
# 	guild_data = {
# 	"name": guild.name,
# 	"id": guild.id,
# 	"prefix": "."
# 	}
#
# 	return guild_data
#
#
# bot.ipc.start()
bot.run("Nzk2MDgyMzc0MjQ4MTAzOTU4.X_SvfA.wOIo_r840K9heQoSPWVLAhY2adE")
