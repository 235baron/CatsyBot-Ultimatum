from discord.ext import commands
import asyncio


class Tutorials(commands.Cog):
    """This category is for tutorials for stuff"""
    def __init__(self, client):
        self.guild = None
        self.author = None
        self.client = client

    @commands.command()
    async def tutorial1(self, ctx: commands.Context):
        """How to make a website"""
        attempts = 30
        startpage = 'Write the number of the page you want to see'
        await ctx.send(f'{startpage}')

        def check(m):
            return (m.author == ctx.author
                    and m.channel == ctx.channel)

        while attempts > 0:
            answer = ''

            while not answer == 'quit':
                try:
                    msg = await self.client.wait_for('message', timeout=15, check=check)
                    something = msg.content
                except asyncio.TimeoutError:
                    await ctx.send('Timeout exceed, quitting...')
                    return

                page = int(something)

                if page == 1:
                    await ctx.send('https://media.discordapp.net/attachments/798927006658068551/824703881350610994/unknown.png?width=1350&height=705')
                elif page == 1:
                    await ctx.send('https://media.discordapp.net/attachments/798927006658068551/824705970009276476/unknown.png?width=1350&height=700')
                elif page == 2:
                    await ctx.send('https://media.discordapp.net/attachments/798927006658068551/824706153987440650/unknown.png?width=1350&height=703')
                elif page == 3:
                    await ctx.send('https://media.discordapp.net/attachments/798927006658068551/824706366773788682/unknown.png?width=1350&height=703')
                elif page == 4:
                    await ctx.send('https://media.discordapp.net/attachments/798927006658068551/824706706172805160/unknown.png?width=1350&height=704')
                elif page == 5:
                    await ctx.send('https://media.discordapp.net/attachments/798927006658068551/824706945117585408/unknown.png?width=1350&height=703')
                elif page == 0:
                    await ctx.send('https://media.discordapp.net/attachments/798927006658068551/824700895312871454/unknown.png?width=1350&height=703')

                attempts -= 1

    @commands.command()
    async def add(self, ctx, a: int, b: int):
        """plus"""
        await ctx.send(a + b)

    @commands.command()
    async def sub(self, ctx, a: int, b: int):
        """minus"""
        await ctx.send(a - b)

    @commands.command()
    async def multiply(self, ctx, a: int, b: int):
        """multiply"""
        await ctx.send(a * b)

    @commands.command()
    async def divide(self, ctx, a: int, b: int):
        """divide"""
        await ctx.send(a / b)


def setup(bot):
    bot.add_cog(Tutorials(bot))
