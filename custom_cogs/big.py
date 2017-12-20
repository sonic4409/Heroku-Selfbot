import discord
from discord.ext import commands

'''Turn messages to Big Text.'''

translated = {
"a": "​:regional_indicator_a:",
"b": ":regional_indicator_b:",
"c": ":regional_indicator_c:",
"d": ":regional_indicator_d:",
"e": ":regional_indicator_e:",
"f": ":regional_indicator_f:",
"g": ":regional_indicator_g:",
"h": ":regional_indicator_h:",
"i": ":regional_indicator_i:",
"j": ":regional_indicator_j:",
"k": ":regional_indicator_k:",
"l": ":regional_indicator_l:",
"m": ":regional_indicator_m:",
"n": ":regional_indicator_n:",
"o": ":regional_indicator_o:",
"p": ":regional_indicator_p:",
"q": ":regional_indicator_q:",
"r": ":regional_indicator_r:",
"s": ":regional_indicator_s:",
"t": ":regional_indicator_t:",
"u": ":regional_indicator_u:",
"v": ":regional_indicator_v:",
"w": ":regional_indicator_w:",
"x": ":regional_indicator_x:",
"y": ":regional_indicator_y:",
"z": ":regional_indicator_z:",
"1": ":one:",
"2": ":two:",
"3": ":three:",
"4": ":four:",
"5": ":five:",
"6": ":six:",
"7": ":seven:",
"8": ":eight:",
"9": ":nine:",
"0": ":ten:",
"!": ":exclamation:",
"?": ":question:",
"*": ":heavy_multiplication_x:",
"/": ":heavy_division_sign:",
"-": ":heavy_minus_sign:",
"+": ":heavy_plus_sign:",
" ": "   ",
"`": ":cross:"
}

class Big:

    def __init__(self, bot):
        self.bot = bot
        self.enabled = False
  
    @commands.command(pass_context=True, aliases=["tb","big"])
    async def bigtext(self, ctx):
        """Turn every message into Big Text."""
        self.enabled = not self.enabled
        await ctx.send(self.bot.bot_prefix + "Big Text Toggled to {}!".format(self.enabled))

    async def on_message(self, message):
        result = ""
        
        if message.author == self.bot.user:
            if not message.embeds and self.enabled:
                result = message.content.lower().translate(str.maketrans(translated))
                await message.delete()
                await message.channel.send(content="", embed=discord.Embed(color=discord.Colour.blue(), description=result))
                
    @commands.command()
    async def b(self, ctx, *, msg):
        """Make your Text BIG.

        Usage:
        >b <message id>
            
        >b <Your String>
            
        >b
            Displays this.
        """

        if msg:
            if msg.isdigit():
                async for message in self.bot.logs_from(ctx.message.channel, 100):
                    if str(message.id) == msg:
                        msg = message.content
                        break
        else:
            switch = False
            async for message in self.bot.logs_from(ctx.message.channel, 2):
                if switch:
                    msg = message.content
                else:
                    switch = True

        result = ""

        result = msg.lower().translate(str.maketrans(translated))

        await ctx.message.delete()
        await ctx.send(result)

def setup(bot):
    bot.add_cog(Big(bot))
