from discord.ext import commands
import discord
import os
import json
import random
import asyncio
import datetime

os.chdir("C:\\Users\\peres\\PycharmProjects\\Learning")


mainshop = [{"name": "Watch", "value": 50, "price": 100, "description": "A nice rolex watch", "unlocked": ".use watch"},
            {"name": "ChillPill", "value": 50, "price": 100, "description": "Calm down...", "unlocked": ".use chillpill"},
            {"name": "Bread", "value": 0, "price": 40, "description": "You like baguettes?", "unlocked": ".use bread"},
            {"name": "Phone", "value": 250, "price": 500, "description": "Play Brawl Stars", "unlocked": ".use phone"},
            {"name": "Airpods", "value": 350, "price": 700, "description": "Listen to music"},
            {"name": "Laptop", "value": 500, "price": 1000, "description": "Have online work meetings. You'll get a raise, trust me"},
            {"name": "PC", "value": 750, "price": 1500, "description": "Play some Minecraft", "unlocked": ".use pc"},
            {"name": "Yaris", "value": 10000, "price": 20000, "description": "Simple, small, good-looking car"},
            {"name": "Corrola", "value": 12500, "price": 25000, "description": "Sizeable car. Good for flexing."},
            {"name": "Bugatti", "value": 45000, "price": 90000, "description": "Super fast and cool looking car", "unlocked": ".race"},
            {"name": "Ferrari", "value": 40000, "price": 80000, "description": "Fancy Shmancy car", "unlocked": ".race"},
            {"name": "CatsyCoin", "value": 60000, "price": 120000, "description": "Flex to your friends that you were able to buy this", "unlocked": ".use catsycoin"},
            {"name": "CatsyTrophy", "value": 500000, "price": 1000000, "description": "The Ultimate Flex weapon", "unlocked": ".use catsytrophy"},
            {"name": "Tank", "value": 10000, "price": 20000, "description": "Increases the loot from the rob command"},
            {"name": "CatsyNobel Prize", "value": 1500000, "price": 3000000, "description": "Sheeeeeesh"},
            {"name": "Cruiseship", "value": 50000, "price": 100000, "description": "Increases amount of loot for work and beg"}
            ]


class Economy(commands.Cog):
    """DA MONEY COMMANDS"""

    def __init__(self, client):
        self.client = client
        self.show = True

    @commands.slash_command(guild_ids=[689859328768999443])
    async def balance(self, ctx):
        """Check the money you have"""
        await self.open_account(ctx.author)
        user = ctx.author
        users = await self.get_bank_data()
        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]
        em = discord.Embed(title=f"{ctx.author.name}'s balance", colour=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
        em.add_field(name="Wallet", value=f"{wallet_amt} <:currency_symbol:832506792767389716>")
        em.add_field(name="Bank", value=f"{bank_amt} <:currency_symbol:832506792767389716>")
        await ctx.respond(embed=em)

    @commands.slash_command(guild_ids=[689859328768999443])
    async def beg(self, ctx):
        """Out of money? Well, beg for some more"""
        await self.open_account(ctx.author)
        user = ctx.author
        users = await self.get_bank_data()
        bag = users[str(user.id)]["bag"]
        for thing in bag:
            if thing["item"] == "cruiseship":
                money = random.randrange(2000, 15000)
                replies = [
                    f"A businessman came by and thought you looked cool. He did a deal with you and you earned some chillpills and {money} <:currency_symbol:832506792767389716>",
                    f"some chillpills and {money} <:currency_symbol:832506792767389716> fell out of the sky",
                    f"You saved someone from drowning. He gave you some chillpills and {money} <:currency_symbol:832506792767389716> as thanks"
                ]
                em = discord.Embed(title="", description=f"{random.choice(replies)}", colour=discord.Colour.blurple())
                em.set_footer(text="+ Cruiseship bonus")
                await ctx.respond(embed=em)
                amount = random.randint(2, 5)
                item_name = "chillpill"
                try:
                    index = 0
                    t = None
                    for thing in users[str(user.id)]["bag"]:
                        n = thing["item"]
                        if n == item_name:
                            old_amt = thing["amount"]
                            new_amt = old_amt + amount
                            users[str(user.id)]["bag"][index]["amount"] = new_amt
                            t = 1
                            break
                        index += 1
                    if t is None:
                        obj = {"item": item_name, "amount": amount}
                        users[str(user.id)]["bag"].append(obj)
                except:
                    obj = {"item": item_name, "amount": amount}
                    users[str(user.id)]["bag"] = [obj]
                with open("mainbank.json", "w") as f:
                    json.dump(users, f)
                users[str(user.id)]["wallet"] += money
                with open("mainbank.json", "w") as f:
                    json.dump(users, f)
                return
        money = random.randrange(2000)
        replies = [
            "How unlucky... You didn't get anything... but what you did get was some bread!", f"Nice you got {money} <:currency_symbol:832506792767389716> \
            and some bread from a cool dude",
            f"Someone felt nice and gave you {money} <:currency_symbol:832506792767389716>",
            f"You seem to have a way with people! Someone gave you bread and {money} <:currency_symbol:832506792767389716>",
            f"What a lucky day!! Someone gave you bread and {money} <:currency_symbol:832506792767389716>",
            f"A rich man passed by you and felt bad. So he gave you bread and {money} <:currency_symbol:832506792767389716>",
            f"A shady man walked up to you and said 'I know how tough it can be out here' before giving you bread and \
            {money} <:currency_symbol:832506792767389716>"
        ]
        em = discord.Embed(title="", description=f"{random.choice(replies)}", colour=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
        await ctx.respond(embed=em)
        users[str(user.id)]["wallet"] += money
        with open("mainbank.json", "w") as f:
            json.dump(users, f)

    @commands.slash_command(guild_ids=[689859328768999443])
    async def work(self, ctx):
        """Work for some money"""
        await self.open_account(ctx.author)
        user = ctx.author
        users = await self.get_bank_data()
        bag = users[str(user.id)]["bag"]
        for thing in bag:
            if thing["item"] == "cruiseship":
                money = random.randrange(10000, 75000)
                replies = [
                    f'You worked at the pizzeria for {money} <:currency_symbol:832506792767389716>',
                    f'{money} <:currency_symbol:832506792767389716> dropped from the sky',
                    f'Your friend saw you get fired and gave you {money} <:currency_symbol:832506792767389716> out of sympathy',
                    f'You got {money} <:currency_symbol:832506792767389716>'
                ]
                em = discord.Embed(title="", description=f"{random.choice(replies)}", colour=discord.Colour.blurple())
                em.set_footer(text="+ Cruiseship bonus")
                await ctx.respond(embed=em)
                users[str(user.id)]["wallet"] += money
                with open("mainbank.json", "w") as f:
                    json.dump(users, f)
                return
        money = random.randrange(1000, 50000)
        replies = [
            f'You worked at the pizzeria for {money} <:currency_symbol:832506792767389716>',
            f'{money} <:currency_symbol:832506792767389716> dropped from the sky',
            f'Your friend saw you get fired and gave you {money} <:currency_symbol:832506792767389716> out of sympathy',
            f'You got {money} <:currency_symbol:832506792767389716>'
        ]
        em = discord.Embed(title="", description=f"{random.choice(replies)}", colour=discord.Colour.blurple())
        if money > 10000:
            em.set_footer(text=f"You got the top bucks today")
        else:
            em.set_footer(text=f"Normal day")
        await ctx.respond(embed=em)
        users[str(user.id)]["wallet"] += money
        with open("mainbank.json", "w") as f:
            json.dump(users, f)

    @commands.slash_command(guild_ids=[689859328768999443])
    async def withdraw(self, ctx, amount=None):
        """Get some money into your wallet"""
        await self.open_account(ctx.author)
        if amount is None:
            em = discord.Embed(title="", description="Please enter amount", color=discord.Colour.og_blurple(),
                               timestamp=datetime.datetime.utcnow())
            await ctx.respond(embed=em)
            return
        bal = await self.update_bank(ctx.author)
        if amount == "all":
            amount = bal[1]
        amount = int(amount)
        if amount > bal[1]:
            em1 = discord.Embed(title="", description="You don't have that much money", color=discord.Colour.og_blurple(),
                               timestamp=datetime.datetime.utcnow())
            await ctx.respond(embed=em1)
            return
        if amount < 0:
            em2 = discord.Embed(title="", description="Amount must be positive", color=discord.Colour.og_blurple(),
                               timestamp=datetime.datetime.utcnow())
            await ctx.respond(embed=em2)
            return
        await self.update_bank(ctx.author, amount)
        await self.update_bank(ctx.author, -1*amount, "bank")
        em3 = discord.Embed(title="", description=f"You withdrew {amount} <:currency_symbol:832506792767389716>", color=discord.Colour.blurple(),
                           timestamp=datetime.datetime.utcnow())
        await ctx.respond(embed=em3)

    @commands.command(guild_ids=[689859328768999443])
    async def deposit(self, ctx, amount=None):
        """That money is heavy. let's put it in the bank"""
        await self.open_account(ctx.author)
        if amount is None:
            em = discord.Embed(title="", description="Please enter amount", color=discord.Colour.og_blurple(),
                               timestamp=datetime.datetime.utcnow())
            await ctx.respond(embed=em)
            return
        bal = await self.update_bank(ctx.author)
        if amount == "all":
            amount = bal[0]
        amount = int(amount)
        if amount > bal[0]:
            em1 = discord.Embed(title="", description="You don't have that much money", color=discord.Colour.og_blurple(),
                                timestamp=datetime.datetime.utcnow())
            await ctx.respond(embed=em1)
            return
        if amount < 0:
            em2 = discord.Embed(title="", description="Amount must be positive", color=discord.Colour.og_blurple(),
                                timestamp=datetime.datetime.utcnow())
            await ctx.respond(embed=em2)
            return
        await self.update_bank(ctx.author, -1 * amount)
        await self.update_bank(ctx.author, amount, "bank")
        em3 = discord.Embed(title="", description=f"You deposited {amount} <:currency_symbol:832506792767389716>", color=discord.Colour.blurple(),
                           timestamp=datetime.datetime.utcnow())
        await ctx.respond(embed=em3)

    @commands.slash_command(guild_ids=[689859328768999443])
    async def pay(self, ctx, person: discord.Member, amount=None):
        """Give someone money"""
        await self.open_account(ctx.author)
        await self.open_account(person)
        if amount is None:
            em = discord.Embed(title="", description="Please enter amount", color=discord.Colour.blurple(),
                               timestamp=datetime.datetime.utcnow())
            await ctx.respond(embed=em)
            return
        bal = await self.update_bank(ctx.author)
        if amount == "all":
            amount = bal[0]
        amount = int(amount)
        if amount > bal[0]:
            em1 = discord.Embed(title="", description="You don't have that much money", color=discord.Colour.blurple(),
                                timestamp=datetime.datetime.utcnow())
            await ctx.respond(embed=em1)
            return
        if amount < 0:
            em2 = discord.Embed(title="", description="Amount must be positive", color=discord.Colour.blurple(),
                                timestamp=datetime.datetime.utcnow())
            await ctx.respond(embed=em2)
            return
        await self.update_bank(ctx.author, -1 * amount, "bank")
        await self.update_bank(person, amount, "bank")
        em3 = discord.Embed(title="", description=f"You gave {amount} <:currency_symbol:832506792767389716> to {person}", color=discord.Colour.blurple(),
                           timestamp=datetime.datetime.utcnow())
        await ctx.respond(em3)

    @commands.slash_command(guild_ids=[689859328768999443])
    async def sell(self, ctx, item, amount=1):
        await self.open_account(ctx.author)

        res = await self.sell_this(ctx.author, item, amount)

        if not res[0]:
            if res[1] == 1:
                em = discord.Embed(title="", description="That Object isn't there!", color=discord.Colour.blurple(),
                                   timestamp=datetime.datetime.utcnow())
                await ctx.respond(embed=em)
                return
            if res[1] == 2:
                em1 = discord.Embed(title="", description=f"You don't have {amount} {item} in your bag.", color=discord.Colour.blurple(),
                                   timestamp=datetime.datetime.utcnow())
                await ctx.respond(embed=em1)
                return
            if res[1] == 3:
                em2 = discord.Embed(title="", description=f"You don't have {item} in your inventory.", color=discord.Colour.blurple(),
                                   timestamp=datetime.datetime.utcnow())
                await ctx.respond(embed=em2)
                return
        em3 = discord.Embed(title="", description=f"You just sold {amount} {item}.", color=discord.Colour.blurple(),
                           timestamp=datetime.datetime.utcnow())
        await ctx.respond(embed=em3)

    @commands.slash_command(guild_ids=[689859328768999443])
    async def slots(self, ctx, amount=None):
        """Test your luck"""
        await self.open_account(ctx.author)
        if amount is None:
            em = discord.Embed(title="", description="Please enter amount", color=discord.Colour.blurple(),
                               timestamp=datetime.datetime.utcnow())
            await ctx.respond(embed=em)
            return
        bal = await self.update_bank(ctx.author)
        amount = int(amount)
        if amount > bal[0]:
            em2 = discord.Embed(title="", description="You don't have that much money", color=discord.Colour.blurple(),
                               timestamp=datetime.datetime.utcnow())
            await ctx.respond(embed=em2)
            return
        if amount < 50:
            em3 = discord.Embed(title="", description="You must bet more than 50 <:currency_symbol:832506792767389716>", color=discord.Colour.blurple(),
                               timestamp=datetime.datetime.utcnow())
            await ctx.respond(embed=em3)
            return
        final = []
        for i in range(3):
            a = random.choice(["X", "O", "Q"])
            final.append(a)
        await ctx.respond(str(final))
        if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
            await self.update_bank(ctx.author, 2 * amount)
            em4 = discord.Embed(title="", description="You won", color=discord.Colour.blurple(),
                               timestamp=datetime.datetime.utcnow())
            await ctx.respond(embed=em4)
        else:
            await self.update_bank(ctx.author, -1 * amount)
            em5 = discord.Embed(title="", description="You lost", color=discord.Colour.blurple(),
                               timestamp=datetime.datetime.utcnow())
            await ctx.respond(embed=em5)

    @commands.slash_command(guild_ids=[689859328768999443])
    async def rob(self, ctx, person: discord.Member):
        """Wanna live a life of crime?"""
        await self.open_account(ctx.author)
        await self.open_account(person)
        user = ctx.author
        users = await self.get_bank_data()
        bal = await self.update_bank(person)
        bag = users[str(user.id)]["bag"]
        if bal[0] < 500:
            em = discord.Embed(title="", description="It's not worth it...", color=discord.Colour.blurple(),
                               timestamp=datetime.datetime.utcnow())
            await ctx.respond(embed=em)
            return
        for thing in bag:
            if thing["item"] == "tank":
                loot = random.randrange(-15, bal[0])
                lost1 = discord.Embed(title="Caught", description=f"You got caught robbing poor {person} and lost {loot}<:currency_symbol:832506792767389716>", color=discord.Colour.blurple())
                won1 = discord.Embed(title="Robbed", description=f"You robbed {loot}<:currency_symbol:832506792767389716>", color=discord.Colour.blurple())
                if loot < 0:
                    lost1.set_footer(text="+ Tank bonus")
                    await self.update_bank(ctx.author, loot)
                    await ctx.respond(embed=lost1)
                    break
                else:
                    won1.set_footer(text="+ Tank bonus")
                    await ctx.respond(embed=won1)
                    await self.update_bank(ctx.author, loot)
                    await self.update_bank(person, -1 * loot)
                    break
        loot = random.randrange(-1000, bal[0])
        lost = discord.Embed(title="Caught", description=f"You got caught robbing poor {person} and lost {loot}<:currency_symbol:832506792767389716>", color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
        won = discord.Embed(title="Robbed", description=f"You robbed {loot}<:currency_symbol:832506792767389716>", color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
        if loot < 0:
            await ctx.respond(embed=lost)
            await self.update_bank(ctx.author, loot)
        else:
            await ctx.respond(embed=won)
            await self.update_bank(ctx.author, loot)
            await self.update_bank(person, -1 * loot)

    @commands.slash_command(guild_ids=[689859328768999443])
    async def shop(self, ctx):
        """All the things you might want are here"""
        em = discord.Embed(title="Shop", color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
        for item in mainshop:
            name = item["name"]
            price = item["price"]
            desc = item["description"]
            em.add_field(name=name, value=f"{price} <:currency_symbol:832506792767389716> | {desc}")
        await ctx.respond(embed=em)

    @commands.slash_command(guild_ids=[689859328768999443])
    async def buy(self, ctx, item, amount=1):
        """Buy something you want from the shop"""
        res = await self.buy_this(ctx.author, item, amount)
        if not res[0]:
            if res[1] == 1:
                em = discord.Embed(title="", description="That Object isn't in the store", color=discord.Colour.blurple(),
                                   timestamp=datetime.datetime.utcnow())
                await ctx.respond(embed=em)
                return
            if res[1] == 2:
                em1 = discord.Embed(title="", description=f"You don't have enough money in your wallet to buy {amount}", color=discord.Colour.blurple(),
                                   timestamp=datetime.datetime.utcnow())
                await ctx.respond(embed=em1)
        if amount > 1:
            em2 = discord.Embed(title="", description=f"You just bought {amount} {item}`s", color=discord.Colour.blurple(),
                               timestamp=datetime.datetime.utcnow())
            await ctx.respond(embed=em2)
        else:
            em3 = discord.Embed(title="", description=f"You just bought {amount} {item}", color=discord.Colour.blurple(),
                               timestamp=datetime.datetime.utcnow())
            await ctx.respond(embed=em3)

    @commands.slash_command(guild_ids=[689859328768999443])
    async def inventory(self, ctx):
        """Check the items you have"""
        await self.open_account(ctx.author)
        user = ctx.author
        users = await self.get_bank_data()
        try:
            bag = users[str(user.id)]["bag"]
        except:
            bag = []
        em = discord.Embed(title=f"{ctx.author}'s Inventory", colour=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
        for item in bag:
            name = item["item"]
            amount = item["amount"]
            em.add_field(name=name, value=f"Amount: {amount}x")
        await ctx.respond(embed=em)

    @commands.slash_command(guild_ids=[689859328768999443])
    async def use(self, ctx, item):
        await self.open_account(ctx.author)
        user = ctx.author
        users = await self.get_bank_data()
        bag = users[str(user.id)]["bag"]
        amongus_option = "Among Us"
        bot_creator_option = "Message bot creators"
        video_option = "Watch videos"
        amogus = discord.Embed(title="You were the Impostor",
                               description="You got caught venting, you lose 1,000 <:currency_symbol:832506792767389716>, ye greedy man",
                               color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
        amogus1 = discord.Embed(title="You were the Impostor",
                                description="You killed all the crewmates, you win 1,000 <:currency_symbol:832506792767389716>, ye greedy man",
                                color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
        amogus2 = discord.Embed(title="You were a Crewmate",
                                description="You got killed, you lose 1,000 <:currency_symbol:832506792767389716>, ye greedy man",
                                color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
        amogus3 = discord.Embed(title="You were a Crewmate",
                                description="You caught the impostor venting and voted him out, you win 1,000 <:currency_symbol:832506792767389716>, ye greedy man",
                                color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
        chillpill_em = discord.Embed(title="Take a chillpill", description="Calm down bruv, take a chillpill and breathe...",
                                     color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
        catsy_trophy_em = discord.Embed(title="Flex God comin' in", description="Give way to the flex god, bois <:catsytrophy:903330264841859113>\
         <:catsytrophy:903330264841859113> <:catsytrophy:903330264841859113> <:catsytrophy:903330264841859113>", color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
        bread_em = discord.Embed(title="Here's a baguette", description="Yummy, huh?", color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
        if item == "phone":
            for thing in bag:
                if thing["item"] == "phone":
                    attempts = 1

                    def check(m):
                        return (m.author == ctx.author
                                and m.channel == ctx.channel)

                    while attempts > 0:
                        guess = ""
                        await ctx.respond(ctx.author.mention + ', what do you want to do?')
                        await ctx.respond('**Message Bot creators** `-` **Play Among Us** `-` **Watch videos**')
                        try:
                            msg = await self.client.wait_for('message', timeout=15, check=check)
                            guess = msg.content
                        except asyncio.TimeoutError:
                            await ctx.respond('Timeout exceed, quitting...')
                            return
                        except ValueError:
                            pass
                        quitwords = ('q', 'quit', 'exit')
                        if guess in quitwords:
                            await ctx.respond('Quitting...')
                            return
                        guess = str(guess)
                        if guess == amongus_option:
                            loot = 100
                            y = [amogus, amogus1, amogus2, amogus3]
                            game = random.choice(y)
                            if game == amogus1:
                                await self.update_bank(ctx.author, loot)
                                await ctx.respond(embed=amogus1)
                            if game == amogus3:
                                await self.update_bank(ctx.author, loot)
                                await ctx.respond(embed=amogus3)
                            if game == amogus:
                                await self.update_bank(ctx.author, -1 * loot)
                                await ctx.respond(embed=amogus)
                                attempts -= 1
                                break
                            elif game == amogus2:
                                await self.update_bank(ctx.author, -1 * loot)
                                await ctx.respond(embed=amogus2)
                                attempts -= 1
                                break
                            else:
                                break
                        elif guess == bot_creator_option:
                            message = await ctx.respond("**235baron's DMs** \n\
                                                      \n\
                            `typing...`")
                            await asyncio.sleep(5)
                            await message.respond(content="**235baron's DMs** \n\
                                                      \n\
                            Me: Why bot bad")
                            await asyncio.sleep(5)
                            await message.respond(content="**235baron's DMs** \n\
                                                      \n\
                            Me: Why bot bad \n\
                            `235baron is typing...`")
                            await asyncio.sleep(5)
                            await message.respond(content="**235baron's DMs** \n\
                                                      \n\
                            Me: Why bot bad \n\
                            235baron: It was as it was and it will be as it will be")
                            attempts -= 1
                            break
                        elif guess == video_option:
                            vids = ["https://www.youtube.com/watch?v=xC8TN6acxBE",
                                    "https://www.youtube.com/watch?v=V7gwKQqk1vg",
                                    "https://www.youtube.com/watch?v=x6WXwx1WrJY",
                                    "https://www.youtube.com/watch?v=v5K3Ox5L10o"]
                            await ctx.respond(random.choice(vids))
                            attempts -= 1
                            break
                        else:
                            end = discord.Embed(title="Huh",
                                                description="Where be your phone, huh? You need one to use this command...",
                                                color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
                            await ctx.respond(embed=end)
                            attempts -= 1
        elif item == "pc":
            for thing in bag:
                if thing["item"] == "pc":
                    attempts = 1

                    def check(m):
                        return (m.author == ctx.author
                                and m.channel == ctx.channel)

                    while attempts > 0:
                        guess = ""
                        await ctx.respond(ctx.author.mention + ', what do you want to do?')
                        await ctx.respond('**Play Minecraft** `-` **Play Among Us** `-` **Search Discord for nitro**')
                        try:
                            msg = await self.client.wait_for('message', timeout=15, check=check)
                            guess = msg.content
                        except asyncio.TimeoutError:
                            await ctx.respond('Timeout exceed, quitting...')
                            return
                        except ValueError:
                            pass
                        quitwords = ('q', 'quit', 'exit')
                        if guess in quitwords:
                            await ctx.respond('Quitting...')
                            return
                        guess = str(guess)
                        if guess == "minecraft":
                            loot = ["lose", "win"]
                            await ctx.respond(
                                "Want to cut down a tree (type `tree`) or go raid a village (type `village`)")
                            minecraftmsg = await self.client.wait_for('message', timeout=15, check=check)
                            answer = minecraftmsg.content
                            if answer == "tree":
                                end = random.choice(loot)
                                if end == "lose":
                                    await ctx.respond("You died to a skeleton hiding behind a tree. \n\
                                                   https://i.imgur.com/1A4KQSM.png")
                                    await self.update_bank(ctx.author, 100)
                                elif end == "win":
                                    await ctx.respond("You cut down a tree, mined, got diamonds and defeated the dragon \n\
                                    https://media.minecraftforum.net/attachments/222/628/636083543577837024.png")
                                    await self.update_bank(ctx.author, 1000)
                            elif answer == "village":
                                end = random.choice(loot)
                                if end == "lose":
                                    await ctx.respond("You died to the iron golem. \n\
                                                                       https://i.imgur.com/cfklWUp.jpg")
                                    await self.update_bank(ctx.author, 100)
                                elif end == "win":
                                    await ctx.respond("You looted a village, got diamonds from the blacksmith, mined a little and defeated the dragon \n\
                                                        https://media.minecraftforum.net/attachments/222/628/636083543577837024.png")
                                    await self.update_bank(ctx.author, 1000)
                            break
                        elif guess == "among us":
                            loot = 100
                            y = [amogus, amogus1, amogus2, amogus3]
                            game = random.choice(y)
                            if game == amogus1:
                                await self.update_bank(ctx.author, loot)
                                await ctx.respond(embed=amogus1)
                            if game == amogus3:
                                await self.update_bank(ctx.author, loot)
                                await ctx.respond(embed=amogus3)
                            if game == amogus:
                                await self.update_bank(ctx.author, -1 * loot)
                                await ctx.respond(embed=amogus)
                                attempts -= 1
                                break
                            elif game == amogus2:
                                await self.update_bank(ctx.author, -1 * loot)
                                await ctx.respond(embed=amogus2)
                                attempts -= 1
                                break
                            else:
                                break
                        elif guess == "nitro":
                            end = ["lose", "win"]
                            nitro = random.choice(end)
                            if nitro == "lose":
                                await ctx.respond("Ha, loser, no one gave you nitro")
                            elif nitro == "win":
                                await ctx.respond("Noice, someone gave you 1 month of free nitro")
                                await self.update_bank(ctx.author, 1000)
                            break
                        else:
                            end = discord.Embed(title="Huh",
                                                description="Where be your pc, huh? You need one to use this command...",
                                                color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
                            await ctx.respond(embed=end)
                            attempts -= 1
        elif item == "catsycoin":
            for thing in bag:
                if thing["item"] == "catsycoin":
                    amogus = discord.Embed(title="Daily Payment",
                                           description="Here ye go, 10,000 <:currency_symbol:832506792767389716>, ye greedy man",
                                           color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
                    loot = 10000
                    await self.update_bank(ctx.author, loot)
                    await ctx.respond(embed=amogus)
                    return
            amogus = discord.Embed(title="CatsyCoin needed", description="ye ain't rich enough, ye tramp", color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
            await ctx.respond(embed=amogus)
        elif item == "watch":
            for thing in bag:
                if thing["item"] == "watch":
                    amogus = discord.Embed(title="Time",
                                           description="",
                                           color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
                    amogus.timestamp = datetime.datetime.utcnow()
                    amogus.set_footer(text='\u200b')
                    await ctx.respond(embed=amogus)
                    return
            amogus1 = discord.Embed(title="Watch needed", description="Smh you don't even have a watch lol", color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
            await ctx.respond(embed=amogus1)
        elif item == "chillpill":
            try:
                index = 0
                t = None
                for thing in users[str(user.id)]["bag"]:
                    video_option = thing["item"]
                    if video_option == "chillpill":
                        old_amt = thing["amount"]
                        new_amt = old_amt - 1
                        if new_amt < 0:
                            return [False, 2]
                        users[str(user.id)]["bag"][index]["amount"] = new_amt
                        t = 1
                        break
                    index += 1
                if t is None:
                    return [False, 3]
            except:
                return [False, 3]

            with open("mainbank.json", "w") as f:
                json.dump(users, f)
            await ctx.respond(embed=chillpill_em)
        elif item == "bread":
            try:
                index = 0
                t = None
                for thing in users[str(user.id)]["bag"]:
                    video_option = thing["item"]
                    if video_option == "bread":
                        old_amt = thing["amount"]
                        new_amt = old_amt - 1
                        if new_amt < 0:
                            return [False, 2]
                        users[str(user.id)]["bag"][index]["amount"] = new_amt
                        t = 1
                        break
                    index += 1
                if t is None:
                    return [False, 3]
            except:
                return [False, 3]

            with open("mainbank.json", "w") as f:
                json.dump(users, f)
            await ctx.respond(embed=bread_em)
        elif item == "catsytrophy":
            await ctx.respond(embed=catsy_trophy_em)

    @commands.slash_command(guild_ids=[689859328768999443])
    async def race(self, ctx, user: discord.Member):
        """Who owns the fastest piece of metal in this town?"""
        choices = ['gas', 'throttle', 'nos', 'drift', 'crash', 'bam']
        gun = random.choice(choices)
        author = ctx.author
        users = await self.get_bank_data()
        bag = users[str(author.id)]["bag"]
        for thing in bag:
            if thing["item"] in ["bugatti", "ferrari"]:
                if ctx.message.author == user:
                    await ctx.respond("**You can't race yourself!**")
                else:
                    await ctx.respond(f"{user.mention} **Do you accept the challenge?** ``yes``** or** ``no``?")

                def check(m):
                    return m.channel == ctx.channel and m.author == user

                if ctx.message.author != user:
                    try:
                        response = await self.client.wait_for('message', check=check, timeout=15)
                    except:
                        await ctx.respond(f"**Looks like {user.mention} doesn't want to race :frowning:**")
                tr = random.randrange(5)

                if response.content.lower() == "yes":
                    await ctx.respond(f"{user.mention} **has accepted the challenge**  :slight_smile:")
                    await asyncio.sleep(2)
                    await ctx.respond("**Get Ready, it will start at any moment!**")
                    await asyncio.sleep(tr)
                    await ctx.respond(f"**Type** ``{gun}`` **now!**")

                if response.content.lower() == "no":
                    await ctx.respond(f"{user.mention} has declined your request :frowning:")

                user1 = ctx.author
                user2 = user

                def check(n):
                    return n.author == user1 or n.author == user2

                message = await self.client.wait_for("message", check=check)
                loot = 1000
                if message.author == user1:
                    if message.content == gun:
                        await self.update_bank(ctx.author, loot)
                        em = discord.Embed(title=f"Winner!",
                                           description=f"{user1.mention} has won this race and gets 1000 CatsyDollars. GG!", color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
                        await ctx.respond(embed=em)

                else:
                    if message.content == gun:
                        await self.update_bank(user, loot)
                        em1 = discord.Embed(title=f"Winner!",
                                            description=f"{user2.mention} has won this race and gets 1000 CatsyDollars. GG!", color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
                        await ctx.respond(embed=em1)
                return
        em = discord.Embed(title="Car needed", description="ye need a car. Bugatti is what ya need", color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
        await ctx.respond(embed=em)

    @commands.slash_command(guild_ids=[689859328768999443])
    async def leaderboard(self, ctx, x=10):
        users = await self.get_bank_data()
        leader_board = {}
        total = []
        for user in users:
            name = int(user)
            total_amount = users[user]["wallet"] + users[user]["bank"]
            leader_board[total_amount] = name
            total.append(total_amount)

        total = sorted(total, reverse=True)

        em = discord.Embed(title=f"Top {x} Richest People",
                           description="The money shown is both wallet amount and bank amount.",
                           color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
        index = 1
        for amt in total:
            id_ = leader_board[amt]
            mem = self.client.get_user(id_)
            name = mem.name
            em.add_field(name=f"{index}. {name}", value=f"{amt} <:currency_symbol:832506792767389716>", inline=False)
            if index == x:
                break
            else:
                index += 1

        await ctx.respond(embed=em)

    @commands.slash_command(guild_ids=[689859328768999443])
    @commands.has_permissions(administrator=True)
    async def add_money(self, ctx, person: discord.Member, amount):
        """Add money to a user"""
        await self.open_account(person)
        if amount is None:
            await ctx.respond("Please enter amount")
            return
        amount = int(amount)
        if amount < 0:
            await ctx.respond("Amount must be positive")
            return
        await self.update_bank(person, amount, "bank")
        await ctx.respond(f"Added {amount} <:currency_symbol:832506792767389716> to {person}")

    async def open_account(self, user):
        users = await self.get_bank_data()
        obj = {"item": "watch", "amount": 1}
        with open("mainbank.json", "r") as f:
            users = json.load(f)

        if str(user.id) in users:
            return False
        else:
            users[str(user.id)] = {}
            users[str(user.id)]["wallet"] = 0
            users[str(user.id)]["bank"] = 0
            users[str(user.id)]["bag"] = {}

        with open("mainbank.json", "w") as f:
            json.dump(users, f)
        return True

    async def get_bank_data(self):
        with open("mainbank.json", "r") as f:
            users = json.load(f)
        return users

    async def update_bank(self, user, change=0, mode="wallet"):
        users = await self.get_bank_data()
        users[str(user.id)][mode] += change
        with open("mainbank.json", "w") as f:
            json.dump(users, f)
            bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]
        return bal

    async def buy_this(self, user, item_name, amount):
        item_name = item_name.lower()
        name_ = None
        for item in mainshop:
            name = item["name"].lower()
            if name == item_name:
                name_ = name
                price = item["price"]
                break
        if name_ is None:
            return [False, 1]
        cost = price * amount
        users = await self.get_bank_data()
        bal = await self.update_bank(user)
        if bal[0] < cost:
            return [False, 2]
        try:
            index = 0
            t = None
            for thing in users[str(user.id)]["bag"]:
                n = thing["item"]
                if n == item_name:
                    old_amt = thing["amount"]
                    new_amt = old_amt + amount
                    users[str(user.id)]["bag"][index]["amount"] = new_amt
                    t = 1
                    break
                index += 1
            if t is None:
                obj = {"item": item_name, "amount": amount}
                users[str(user.id)]["bag"].append(obj)
        except:
            obj = {"item": item_name, "amount": amount}
            users[str(user.id)]["bag"] = [obj]
        with open("mainbank.json", "w") as f:
            json.dump(users, f)
        await self.update_bank(user, cost * -1, "wallet")
        return [True, "Worked"]

    async def sell_this(self, user, item_name, amount, price=None):
        item_name = item_name.lower()
        name_ = None
        for item in mainshop:
            name = item["name"].lower()
            if name == item_name:
                name_ = name
                if price is None:
                    price = item["value"]
                break

        if name_ is None:
            return [False, 1]

        cost = price * amount

        users = await self.get_bank_data()

        try:
            index = 0
            t = None
            for thing in users[str(user.id)]["bag"]:
                n = thing["item"]
                mybag = users[str(user.id)]["bag"]
                if n == item_name:
                    old_amt = thing["amount"]
                    new_amt = old_amt - amount
                    users[str(user.id)]["bag"][index]["amount"] = new_amt
                    if new_amt == 0:
                        element_to_remove = [x for x in mybag if x['item'] == item_name]
                        mybag.remove(element_to_remove[0])
                    t = 1
                    break
                index += 1
            if t is None:
                return [False, 3]
        except:
            return [False, 3]

        with open("mainbank.json", "w") as f:
            json.dump(users, f)

        await self.update_bank(user, cost, "wallet")

        return [True, "Worked"]


def setup(bot):
    bot.add_cog(Economy(bot))
