import random
from discord.ext import commands
import asyncio
import discord
import aiohttp
import datetime


all_fun_facts = ["Banging your head against a wall for one hour burns 150 calories.",
                 "Snakes can help predict earthquakes.",
                 "7% of American adults believe that chocolate milk comes from brown cows.",
                 "If you lift a kangaroo’s tail off the ground it can’t hop.",
                 "Bananas are curved because they grow towards the sun."]
hm = all_fun_facts.copy()

errortxt = ('That is not formatted properly or valid positive integers weren\'t used, ',
            'the proper format is:\n`[Prefix]minesweeper <columns> <rows> <bombs>`\n\n',
            'You can give me nothing for random columns, rows, and bombs.')
errortxt = ''.join(errortxt)


class Fun(commands.Cog):
    """This category is about... well... Fun"""
    def __init__(self, client):
        self.guild = None
        self.author = None
        self.client = client
        self.show = True

    @commands.slash_command(description="Ask for words of wisdom", guild_ids=[689859328768999443])
    async def _8ball(self, ctx, *, question):
        responses = ['As I see it, yes.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     'Don’t count on it.',
                     'It is certain.',
                     'It is decidedly so.',
                     'Most likely.',
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Outlook good.',
                     'Reply hazy, try again.',
                     'Signs point to yes.',
                     'Very doubtful.',
                     'Without a doubt.',
                     'Yes.',
                     'Yes – definitely.',
                     'You may rely on it.'
                     ]
        q = ("Question: " + question)
        answer = ("Answer: " + random.choice(responses))
        embed = discord.Embed(
            title=q,
            description=answer,
            colour=discord.Colour.blue()
        )
        await ctx.respond(embed=embed)

    @commands.slash_command(description="Talk to the great guy", guild_ids=[689859328768999443])
    async def asktrump(self, ctx, *, message):
        a = [
            "ABC",
            "AFGHANISTAN",
            "ALIENS",
            "AMERICA",
            "BAN",
            "BETSY",
            "BIASED",
            "BIGLY",
            "BUSH",
            "CBS",
            "CHINA",
            "CHRISTIANS",
            "CIA",
            "CLIMATE CHANGE",
            "CLINTON",
            "CNN",
            "COMPLICATED",
            "DEMOCRAT",
            "DISGRACE",
            "DOING POORLY",
            "EMBARRASSING",
            "EXACTLY",
            "FAILING",
            "FAKE MEDIA",
            "FAKE NEWS",
            "FBI",
            "FOX",
            "GERMANY",
            "GREAT",
            "HOAX",
            "HUGE",
            "IDIOTS",
            "ILLEGAL",
            "IMMIGRANTS",
            "INCOMPETENT",
            "IRAN",
            "IRAQ",
            "ISIS",
            "IVANKA",
            "JOBS",
            "KKK",
            "LAW",
            "LEAKERS",
            "LIAR",
            "LIES",
            "MELANIA",
            "MESS",
            "MEXICANS",
            "MEXICO",
            "MISS UNIVERSE",
            "MUSLIMS",
            "NATIONAL",
            "NBC",
            "NO",
            "NORTH KOREA",
            "NOT GUILTY",
            "NOT",
            "NSA",
            "NUCLEAR",
            "NUKE",
            "OBAMA",
            "OBNOXIOUS",
            "OIL",
            "ORDER",
            "PATHETIC",
            "PATRIOTS",
            "PEDOPHILE",
            "PEOPLE",
            "PRESIDENT",
            "PRISON",
            "PUTIN",
            "REAL",
            "REFUGEES",
            "REPUBLICAN",
            "RIGGED",
            "RUSSIA",
            "SECURITY",
            "STUPID",
            "SUCCESS",
            "SWEDEN",
            "SYRIA",
            "TACO",
            "TAXES",
            "TERRIBLE",
            "TERROR",
            "TERRORISM",
            "TEXAS",
            "THE BEST",
            "THE GREATEST",
            "THE HUGEST",
            "THE REALEST",
            "UKRAINE",
            "UNFAIR",
            "VERY WELL",
            "VICTORY",
            "WALL",
            "WOMEN",
            "WRONG"
        ]
        b = [
            "http://www.slate.com/content/dam/slate/articles/news_and_politics/politics/2016/04/160422_POL_Donald-Trump-Act.jpg.CROP.promo-xlarge2.jpg",
            "https://pixel.nymag.com/imgs/daily/intelligencer/2017/01/24/24-trump-unhinged.w710.h473.jpg",
            "https://blogs-images.forbes.com/robertwood/files/2016/02/Trump1.jpg",
            "http://static6.businessinsider.com/image/55918b77ecad04a3465a0a63/nbc-fires-donald-trump-after-he-calls-mexicans-rapists-and-drug-runners.jpg",
            "http://www.slate.com/content/dam/slate/blogs/the_slatest/2017/04/17/trump_recommended_a_book_on_twitter_today_it_has_no_words/660291014-president-donald-trump-speaks-during-an-event.jpg.CROP.promo-xlarge2.jpg",
            "http://ichef.bbci.co.uk/news/1024/cpsprodpb/1BC2/production/_88160170_trump-promo.jpg",
            "http://www.slate.com/content/dam/slate/articles/news_and_politics/politics/2017/01/170112_POL_trump.jpg.CROP.promo-xlarge2.jpg"
        ]
        em = discord.Embed(title="Ask Trump", description="", colour=discord.Colour.blue())
        em.set_thumbnail(url=random.choice(b))
        em.add_field(name=f"{ctx.author}:", value=message, inline=False)
        em.add_field(name="Donald Trump:", value=random.choice(a), inline=False)
        await ctx.respond(embed=em)

    @commands.slash_command(description="Wanna bet?", guild_ids=[689859328768999443], pass_context=True)
    async def coinflip(self, ctx):
        """Wanna bet? Flip a coin!"""
        flip = random.choice([
            f'https://upload.wikimedia.org/wikipedia/de/thumb/8/80/2_euro_coin_Eu_serie_1.png/220px-2_euro_coin_Eu_serie_1.png',
            f'https://www.zwei-euro.com/wp-content/uploads/2019/02/DE-2002.gif'])
        flipcoin = discord.Embed(color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
        flipcoin.colour = 0x12423
        flipcoin.set_thumbnail(
            url="https://media1.tenor.com/images/938e1fc4fcf2e136855fd0e83b1e8a5f/tenor.gif?itemid=5017733")
        await ctx.respond(embed=flipcoin)
        coin = discord.Embed(color=discord.Colour.blurple(), timestamp=datetime.datetime.utcnow())
        coin.set_thumbnail(url=f'{flip}')
        await asyncio.sleep(2)
        await ctx.respond(embed=coin)

    @commands.slash_command(description="Your daily dose of Brooklyn 99", guild_ids=[689859328768999443])
    async def brooklyn_99(self, ctx):
        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            'The English Language Can Not Fully Capture The Depth And Complexity Of My Thoughts, So I’m Incorporating Emojis Into My Speech To Better Express Myself. Winky Face.',
            'Be Myself, What Kind Of Garbage Advice Is That?',
            'True Strength Comes From The Pelvis, Not The Mouth.',
            'Captain Wuntch. Good To See You. But If You’re Here, Who’s Guarding Hades?',
            'Okay, No Hard Feelings, But I Hate You. Not Joking. Bye.',
            'Sarge, With All Due Respect, I Am Gonna Completely Ignore Everything You Just Said.',
            'Fine. But In Protest, Im Walking Over There Extremely Slowly!',
            'Hello, Unsolved Case. Do You Bring Me Joy? No, Because Youre Boring And Youre Too Hard. See Ya.',
            'Well, No One Asked You. Its A Self-Evaluation.',
            'I Ate One String Bean. It Tasted Like Fish Vomit. That Was It For Me.',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
        ]
        em = discord.Embed(
            title="",
            description=random.choice(brooklyn_99_quotes),
            color=discord.Colour.blurple(),
            timestamp=datetime.datetime.utcnow()
        )
        await ctx.respond(embed=em)

    all_fun_facts = [
        "Banging your head against a wall for one hour burns 150 calories.",
        "Snakes can help predict earthquakes.",
        "7% of American adults believe that chocolate milk comes from brown cows.",
        "If you lift a kangaroo’s tail off the ground it can’t hop.",
        "Bananas are curved because they grow towards the sun.",
        "What other planets have volcanic activity? Extraterrestrial Volcanoes - Mercury, Venus, Earth's Moon, Mars, Io, Saturn. Volcanism has played a major part in shaping not only planet Earth, but other places in our universe. Though other planets show signs of volcanic eruptions, most seemed to have erupted in the distant past and are inactive now.",
        "North Korea and Cuba are the only places you can’t buy Coca-Cola.",
        "The entire world’s population could fit inside Los Angeles.",
        "The hottest chili pepper in the world is so hot it could kill you.",
        "The world’s most densely populated island is the size of two soccer fields.",
        "The Canary Islands are named after dogs, not birds.",
        "Indonesia is home to some of the shortest people in the world.",
        "The world’s quietest room is located at Microsoft's headquarters in Washington state.",
        "The longest place name on the planet is 85 letters long.",
        "Four babies are born every second.",
        "The coldest temperature ever recorded was -144 degrees Fahrenheit.",
        "There are around 4 quadrillion quadrillion bacteria on Earth.",
        "Only two countries use purple in their national flags.",
        "The most expensive coin in the world was sold for more than $7 million.",
        "A record-breaking 92 countries competed in the 2018 Winter Olympics.",
        "More than 52 percent of the world’s population is under 30 years old.",
        "People 60 years and older make up 12.3 percent of the global population.",
        "There are 43 countries that still have a royal family.",
        "The red-billed quelea is the most common bird on Earth.",
        "Around one in every 200 men are direct descendants of Genghis Khan.",
        "There are 41 countries that recognize sign language as an official language.",
        "Facebook has more users than the population of the U.S., China, and Brazil combined.",
        "There are only two countries with names that begin with “The.”",
        "All the ants on Earth weigh about as much as all the humans.",
        "The oceans contain almost 200,000 different kinds of viruses.",
        "New Zealanders have more pets per household than any other country.",
        "Tokyo is the world’s largest city with 37 million inhabitants.",
        "Nearly two people die each second.",
        ""
    ]

    @commands.slash_command(description="The more you know!", guild_ids=[689859328768999443])
    async def funfact(self, ctx):
        em = discord.Embed(title="", description=random.choice(all_fun_facts), color=discord.Colour.blurple(),
                           timestamp=datetime.datetime.utcnow())
        await ctx.respond(embed=em)

    # @commands.command()
    # async def hack(self, ctx, member: discord.Member):
    #     random_id = ['20390940',
    #                  '20930948',
    #                  '09479398',
    #                  '03984988',
    #                  '94883099',
    #                  '98477490',
    #                  '37729902',
    #                  '98765421',
    #                  '93893893',
    #                  '08589498',
    #                  '88489920',
    #                  '84990201',
    #                  '94789435',
    #                  '98839897',
    #                  '49732974',
    #                  '97398394',
    #                  '80489033',
    #                  '98479883',
    #                  '97878820',
    #                  '08839004',
    #                  '98308934',
    #                  '09029389',
    #                  '98308483',
    #                  '84083887',
    #                  '08480388',
    #                  '98408036',
    #                  '39729993',
    #                  '39383479',
    #                  '47859789',
    #                  '48749749',
    #                  '70909585']
    #     passwords = ['Hisj09',
    #                  'o093y*gh',
    #                  'Im43fpiN10&',
    #                  '3i9eiih8',
    #                  'sok30wok',
    #                  '39iwi9i',
    #                  '3kw903ewo',
    #                  'ekw0kw0',
    #                  'wokkwooks',
    #                  'k0okwok',
    #                  'ko8928',
    #                  '30ij9i7',
    #                  '49ie990ko',
    #                  '30ke0eo',
    #                  '3003eokeo',
    #                  '30ek9eki9',
    #                  '3oke0emiddj',
    #                  '30e0w0lks8',
    #                  '48jeijsiji8',
    #                  '49kred8',
    #                  '82u2waji',
    #                  '22ll0la',
    #                  '30ks0so0',
    #                  '55omf09',
    #                  '30309oe',
    #                  '10009',
    #                  '10993k',
    #                  '10020oski',
    #                  '20keosoo20',
    #                  'bd489475998',
    #                  '4u8dhig7t',
    #                  'o4j9uerri8',
    #                  '4eud9i4u',
    #                  '4ue9re9'
    #                  ]
    #     y = passwords
    #     x = random_id
    #     await ctx.respond(content=f"🔄 Hacking {member}")
    #     await asyncio.sleep(5)
    #     await ctx.respond(content="❌ Firewall blocking access")
    #     await asyncio.sleep(5)
    #     await ctx.respond(content="✅ Firewall hacked")
    #     await asyncio.sleep(5)
    #     await ctx.respond(content=f"💸 Apple Account password is {random.choice(y)}")
    #     await asyncio.sleep(5)
    #     await ctx.respond(content=f"〽 Credit Card ID is {random.choice(x)}")
    #     await asyncio.sleep(5)
    #     await ctx.respond(content=f"💫 Discord ID is {random.choice(x)}")
    #     await asyncio.sleep(5)
    #     await ctx.respond(content=f"🔄 Google Account password is {random.choice(y)}")
    #     await asyncio.sleep(5)
    #     await ctx.respond(content=f"🔄 Microsoft Account password is {random.choice(y)}")
    #     await asyncio.sleep(5)
    #     await ctx.respond(content=f"🔄 Bank Lock Code is {random.choice(x)}")
    #     await asyncio.sleep(5)
    #     await ctx.respond(content="🔄 Covering all traces")
    #     await asyncio.sleep(5)
    #     await ctx.respond(content="🔄 Destroying browser memory")
    #     await asyncio.sleep(5)
    #     await ctx.respond(content=f"✅ Finished hacking {member}")

    @commands.slash_command(description="Imitate the bot", guild_ids=[689859328768999443])
    async def say(self, ctx, message):
        """Makes the bot say something"""
        em = discord.Embed(title="", description=message, color=discord.Colour.blurple(),
                           timestamp=datetime.datetime.utcnow())
        await ctx.respond(embed=em)

    # @commands.command(aliases=["facepalm"])
    # async def fp(self, ctx):
    #     """Idiotic memes to laugh at"""
    #     async with aiohttp.ClientSession() as session:
    #         async with session.get(f"https://www.reddit.com/r/facepalm/top.json") as response:
    #             j = await response.json()
    #
    #     data = j["data"]["children"][random.randint(0, 25)]["data"]
    #     image_url = data["url"]
    #     title = data["title"]
    #     em = discord.Embed(description=f"[**{title}**]({image_url})", colour=discord.Colour.blurple())
    #     em.set_image(url=image_url)
    #     em.set_footer(text=f"Requested by {ctx.author}")
    #     await ctx.send(embed=em)

    @commands.slash_command(description="Let's laugh together", guild_ids=[689859328768999443], aliases=["maymay", "memes"])
    async def meme(self, ctx):
        """Em... well... memes?"""

        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.reddit.com/r/cleanmemes/top.json") as response:
                j = await response.json()

        data = j["data"]["children"][random.randint(0, 10)]["data"]
        image_url = data["url"]
        title = data["title"]
        em = discord.Embed(description=f"[**{title}**]({image_url})", colour=discord.Colour.blurple())
        em.set_image(url=image_url)
        em.set_footer(text=f"Requested by {ctx.author}")
        await ctx.respond(embed=em)

    @commands.slash_command(description="Some Star Wars memes", guild_ids=[689859328768999443], aliases=["prequelmeme", "pre"])
    async def prequel(self, ctx):
        """Star Wars memes"""

        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.reddit.com/r/PrequelMemes/top.json") as response:
                j = await response.json()

        data = j["data"]["children"][random.randint(0, 25)]["data"]
        image_url = data["url"]
        title = data["title"]
        em = discord.Embed(description=f"[**{title}**]({image_url})", colour=discord.Colour.blurple())
        em.set_image(url=image_url)
        em.set_footer(text=f"Requested by {ctx.author}")
        await ctx.respond(embed=em)

    @commands.slash_command(description="Knock out the person you hate", guild_ids=[689859328768999443], aliases=['knockout'])
    async def ko(self, ctx, member):
        """Punch the person you hate"""

        gifslist = ['https://media.tenor.com/images/e302b70e805f045816c100a92325b824/tenor.gif',
                    'https://media1.tenor.com/images/3da22c373b5506939514773ad496b170/tenor.gif?itemid=11751811',
                    'https://media1.tenor.com/images/b3dddda27a439a9951fdd0de5a0644e6/tenor.gif?itemid=15872871',
                    'https://media1.tenor.com/images/3b0d7cc04fb09adb1ccc96a23b98dd86/tenor.gif?itemid=6032176',
                    'https://media1.tenor.com/images/97248cf32942f467c4a049acbae8981e/tenor.gif?itemid=3555140',
                    'https://media1.tenor.com/images/c7dece5cdd4cee237e232e0c5d955042/tenor.gif?itemid=4902914']
        gifs = random.choice(gifslist)

        embed = discord.Embed(
            description=f"{member} Has been Knocked Out!",
            colour=discord.Colour.blurple(),
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_image(url=gifs)
        await ctx.respond(embed=embed)

    # @commands.command(name='..')
    # async def command(self, ctx):
    #     """Indeed..."""
    #     await ctx.send("Indeed...")

    @commands.slash_command(guild_ids=[689859328768999443],
                            description='For when you wanna settle the score some other way')
    async def choose(self, ctx, choice1: str, choice2: str):
        """Chooses between multiple choices."""
        numberchoice = random.randint(1, 100)
        if numberchoice <= 50:
            em = discord.Embed(title="", description=choice1, color=discord.Colour.blurple(),
                               timestamp=datetime.datetime.utcnow())
            await ctx.respond(embed=em)
            pass
        elif numberchoice >= 50:
            em = discord.Embed(title="", description=choice2, color=discord.Colour.blurple(),
                               timestamp=datetime.datetime.utcnow())
            await ctx.respond(embed=em)
            pass

    @commands.slash_command(description="A rock, some paper or scissors. Choose", guild_ids=[689859328768999443])
    async def rsp(self, ctx, choice):
        ssp_choice = ['scissor', 'rock', 'paper']
        genchoice = random.choice(ssp_choice)

        if choice == 'scissor' and genchoice == 'scissor':
            s = discord.Embed(title='✂ Scissors', description='Draw 🙄', color=discord.Colour.blurple(),
                              timestamp=datetime.datetime.utcnow())
            s.set_author(name='')
            await ctx.respond(embed=s)
        elif choice == 'scissor' and genchoice == 'rock':
            s = discord.Embed(title='✂ Rock', description='You lose 😂', color=discord.Colour.blurple(),
                              timestamp=datetime.datetime.utcnow())
            s.set_author(name='')
            await ctx.respond(embed=s)
        elif choice == 'scissor' and genchoice == 'paper':
            s = discord.Embed(title='✂ Paper', description='You win 🎉', color=discord.Colour.blurple(),
                              timestamp=datetime.datetime.utcnow())
            s.set_author(name='')
            await ctx.respond(embed=s)

        elif choice == 'rock' and genchoice == 'scissor':
            s = discord.Embed(title='Scissors', description='You win 🎉', color=discord.Colour.blurple(),
                              timestamp=datetime.datetime.utcnow())
            s.set_author(name='')
            await ctx.respond(embed=s)
        elif choice == 'rock' and genchoice == 'rock':
            s = discord.Embed(title='Rock', description='Draw 🙄', color=discord.Colour.blurple(),
                              timestamp=datetime.datetime.utcnow())
            s.set_author(name='')
            await ctx.respond(embed=s)
        elif choice == 'rock' and genchoice == 'paper':
            s = discord.Embed(title='Paper', description='You lose 😂', color=discord.Colour.blurple(),
                              timestamp=datetime.datetime.utcnow())
            s.set_author(name='')
            await ctx.respond(embed=s)

        elif choice == 'paper' and genchoice == 'scissor':
            s = discord.Embed(title='📜 Scissors', description='You lose 😂', color=discord.Colour.blurple(),
                              timestamp=datetime.datetime.utcnow())
            s.set_author(name='')
            await ctx.respond(embed=s)
        elif choice == 'paper' and genchoice == 'rock':
            s = discord.Embed(title='📜 Rock', description='You win 🎉', color=discord.Colour.blurple(),
                              timestamp=datetime.datetime.utcnow())
            s.set_author(name='')
            await ctx.respond(embed=s)
        elif choice == 'paper' and genchoice == 'paper':
            s = discord.Embed(title='📜 Paper', description='Draw 🙄', color=discord.Colour.blurple(),
                              timestamp=datetime.datetime.utcnow())
            s.set_author(name='')
            await ctx.respond(embed=s)

        else:
            n = discord.Embed(title='Dont try to cheat', description='Invalid choice', color=discord.Colour.red())
            n.set_author(name='')
            await ctx.respond(embed=n)

    @commands.slash_command(description="Don't hit the bomb!", guild_ids=[689859328768999443])
    async def minesweeper(self, ctx, columns=None, rows=None, bombs=None):
        if columns is None or rows is None and bombs is None:
            if columns is not None or rows is not None or bombs is not None:
                await ctx.respond(errortxt)
                return
            else:
                columns = random.randint(4, 13)
                rows = random.randint(4, 13)
                bombs = columns * rows - 1
                bombs = bombs / 2.5
                bombs = round(random.randint(5, round(bombs)))
        try:
            columns = int(columns)
            rows = int(rows)
            bombs = int(bombs)
        except ValueError:
            await ctx.respond(errortxt)
            return
        if columns > 13 or rows > 13:
            await ctx.respond('The limit for the columns and rows are 13 due to discord limits...')
            return
        if columns < 1 or rows < 1 or bombs < 1:
            await ctx.respond('The provided numbers cannot be zero or negative...')
            return
        if bombs + 1 > columns * rows:
            await ctx.respond(
                ':boom:**BOOM**, you have more bombs than spaces on the grid or you attempted to make all of the spaces bombs!')
            return

        # Creates a list within a list and fills them with 0s, this is our makeshift grid
        grid = [[0 for num in range(columns)] for num in range(rows)]

        # Loops for the amount of bombs there will be
        loop_count = 0
        while loop_count < bombs:
            x = random.randint(0, columns - 1)
            y = random.randint(0, rows - 1)
            # We use B as a variable to represent a Bomb (this will be replaced with emotes later)
            if grid[y][x] == 0:
                grid[y][x] = 'B'
                loop_count = loop_count + 1
            # It will loop again if a bomb is already selected at a random point
            if grid[y][x] == 'B':
                pass

        # The while loop will go though every point though our makeshift grid
        pos_x = 0
        pos_y = 0
        while pos_x * pos_y < columns * rows and pos_y < rows:
            # We need to predefine this for later
            adj_sum = 0
            # Checks the surrounding points of our "grid"
            for (adj_y, adj_x) in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                # There will be index errors, we can just simply ignore them by using a try and exception block
                try:
                    if grid[adj_y + pos_y][adj_x + pos_x] == 'B' and adj_y + pos_y > -1 and adj_x + pos_x > -1:
                        # adj_sum will go up by 1 if a surrounding point has a bomb
                        adj_sum = adj_sum + 1
                except Exception as error:
                    pass
            # Since we don't want to change the Bomb variable into a number,
            # the point that the loop is in will only change if it isn't "B"
            if grid[pos_y][pos_x] != 'B':
                grid[pos_y][pos_x] = adj_sum
            # Increases the X values until it is more than the columns
            # If the while loop does not have "pos_y < rows" will index error
            if pos_x == columns - 1:
                pos_x = 0
                pos_y = pos_y + 1
            else:
                pos_x = pos_x + 1

        # Builds the string to be Discord-ready
        string_builder = []
        for the_rows in grid:
            string_builder.append(''.join(map(str, the_rows)))
        string_builder = '\n'.join(string_builder)
        # Replaces the numbers and B for the respective emotes and spoiler tags
        string_builder = string_builder.replace('0', '||:zero:||')
        string_builder = string_builder.replace('1', '||:one:||')
        string_builder = string_builder.replace('2', '||:two:||')
        string_builder = string_builder.replace('3', '||:three:||')
        string_builder = string_builder.replace('4', '||:four:||')
        string_builder = string_builder.replace('5', '||:five:||')
        string_builder = string_builder.replace('6', '||:six:||')
        string_builder = string_builder.replace('7', '||:seven:||')
        string_builder = string_builder.replace('8', '||:eight:||')
        final = string_builder.replace('B', '||:bomb:||')

        percentage = columns * rows
        percentage = bombs / percentage
        percentage = 100 * percentage
        percentage = round(percentage, 2)
        embed = discord.Embed(title='\U0001F642 Minesweeper \U0001F635', color=discord.Colour.blurple())
        embed.add_field(name='Columns:', value=columns, inline=True)
        embed.add_field(name='Rows:', value=rows, inline=True)
        embed.add_field(name='Total Spaces:', value=columns * rows, inline=True)
        embed.add_field(name='\U0001F4A3 Count:', value=bombs, inline=True)
        embed.add_field(name='\U0001F4A3 Percentage:', value=f'{percentage}%', inline=True)
        embed.add_field(name='Requested by:', value=ctx.author.display_name, inline=True)
        await ctx.respond(content=f'\U0000FEFF\n{final}', embed=embed)


def setup(bot):
    bot.add_cog(Fun(bot))
