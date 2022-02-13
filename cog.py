"""
MIT License
Copyright (c) 2021 Polsulpicien
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

##############################################
#       Made by Polsulpicien#5020            #    
#                                            #
# DON'T CHANGE THE FOOTER TEXT OF THE EMBEDS #
############################################## 

import discord
from discord.ext import commands

from discord_components import DiscordComponents, Button, ButtonStyle
from math import pi, tau, e, sqrt
import asyncio
from TagScriptEngine import Interpreter, block

class Calculator(commands.Cog):
    def __init__(self, client):
        self.client = client
        blocks = [
            block.MathBlock(),
            block.RandomBlock(),
            block.RangeBlock(),
        ]
        self.engine = Interpreter(blocks)

        self.data = {
            "1":"¹",
            "2":"²",
            "3":"³",
            "4":"⁴",
            "5":"⁵",
            "6":"⁶",
            "7":"⁷",
            "8":"⁸",
            "9":"⁹"
        }

        self.normal_components = [
            [
                Button(style=ButtonStyle.grey, label="1", id="1"),
                Button(style=ButtonStyle.grey, label="2", id="2"),
                Button(style=ButtonStyle.grey, label="3", id="3"),
                Button(style=ButtonStyle.blue, label="×", id="*"),
                Button(style=ButtonStyle.red, label="Exit", id="Exit"),
            ],
            [
                Button(style=ButtonStyle.grey, label="4", id="4"),
                Button(style=ButtonStyle.grey, label="5", id="5"),
                Button(style=ButtonStyle.grey, label="6", id="6"),
                Button(style=ButtonStyle.blue, label="÷", id="/"),
                Button(style=ButtonStyle.red, label="⌫", id="⌫"),
            ],
            [
                Button(style=ButtonStyle.grey, label="7", id="7"),
                Button(style=ButtonStyle.grey, label="8", id="8"),
                Button(style=ButtonStyle.grey, label="9", id="9"),
                Button(style=ButtonStyle.blue, label="+", id="+"),
                Button(style=ButtonStyle.red, label="Clear", id="Clear"),
            ],
            [
                Button(style=ButtonStyle.grey, label="00", id="00"),
                Button(style=ButtonStyle.grey, label="0", id="0"),
                Button(style=ButtonStyle.grey, label=".", id="."),
                Button(style=ButtonStyle.blue, label="-", id="-"),
                Button(style=ButtonStyle.green, label="=", id="="),
            ],
            [
                Button(style=ButtonStyle.green, label="❮", id="❮"),
                Button(style=ButtonStyle.green, label="❯", id="❯"),
                Button(
                    style=ButtonStyle.grey,
                    label="Change to scientific mode",
                    emoji="\U0001f9d1\u200D\U0001f52c",
                    id="scientific_mode",
                ),
            ],
        ]

        self.scientific_components = [
            [
                Button(style=ButtonStyle.grey, label="(", id="("),
                Button(style=ButtonStyle.grey, label=")", id=")"),
                Button(style=ButtonStyle.grey, label="000", id="000"),
                Button(style=ButtonStyle.blue, label="×", id="*"),
                Button(style=ButtonStyle.red, label="Exit", id="Exit"),
            ],
            [
                Button(style=ButtonStyle.grey, label="X²"),
                Button(style=ButtonStyle.grey, label="X³"),
                Button(style=ButtonStyle.grey, label="Xˣ"),
                Button(style=ButtonStyle.blue, label="÷", id="/"),
                Button(style=ButtonStyle.red, label="⌫", id="⌫"),
            ],
            [
                Button(style=ButtonStyle.grey, label="e", id="e"),
                Button(style=ButtonStyle.grey, label="τ", id="τ"),
                Button(style=ButtonStyle.grey, label="π", id="π"),
                Button(style=ButtonStyle.blue, label="+", id="+"),
                Button(style=ButtonStyle.red, label="Clear", id="Clear"),
            ],
            [
                Button(style=ButtonStyle.grey, label=" ", disabled=True),
                Button(style=ButtonStyle.grey, label=" ", disabled=True),
                Button(style=ButtonStyle.grey, label=" ", disabled=True),
                Button(style=ButtonStyle.blue, label="-", id="-"),
                Button(style=ButtonStyle.green, label="=", id="="),
            ],
            [
                Button(style=ButtonStyle.green, label="❮", id="❮"),
                Button(style=ButtonStyle.green, label="❯", id="❯"),
                Button(
                    style=ButtonStyle.grey,
                    label="Change to normal modeㅤ",
                    emoji="\U0001f468\u200D\U0001f3eb",
                    id="normal_mode",
                ),
            ],
        ]
    
    def calculate(self, expression:str):
        result=''
        expression = expression.replace("π", str(pi))
        expression = expression.replace("τ", str(tau))
        expression = expression.replace("e", str(e))
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")

        for i in self.data:
            if self.data[i] in expression:
                expression = expression.replace(self.data[i], f"^{i}")

        result = self.engine.process("{m:"+expression+"}").body
        result = result.replace("{m:", "").replace("}", "")

        try:
            result = f"{float(result):,}"
        except:
            if result == expression:
                result = "∞"
            else:
                result = "Syntax Error!\nDon't forget the sign(s) ('×', '÷', ...).\nnot: 3(9+1) but 3×(9+1)"

        return result

    def input_formatter(self, original:str, label:str):
        if 'Syntax Error!' in original:
            original='|'
        lst=list(original)
        try:
            index=lst.index('|')
            lst.remove('|')
        except:
            index=0
        if label == 'X²':
            lst.insert(index, '²')
        elif label == 'X³':
            lst.insert(index, '³')
        elif label == 'Xˣ':
            lst.insert(index, '^')
        else:
            if len(lst)>1 and lst[index-1]=="^":
                try:
                    lst.insert(index, self.data[label])
                    lst.remove('^')
                    index-=1
                except:
                    lst.insert(index, label)
            else:
                lst.insert(index, label)
        lst.insert(index+1, '|')
        original=''.join(lst)
        return original

    def _get_embed(self, ctx, embed_description:str):
        embed = discord.Embed(
            title=f"{ctx.author}'s calculator",
            description=embed_description,
            color=0x2F3136,
        )
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text="https://github.com/Polsulpicien")
        return embed
    
    @commands.command(aliases=['calc', 'calculator'])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def calcu(self,ctx):
        affichage = "|"
        is_normal_mode = True
        embed = self._get_embed(ctx, f"```{affichage}```")
        expression = ""
        message = await ctx.send(
            components=self.normal_components, embed=embed
        )

        while True:
            try:
                interaction = await self.client.wait_for(
                    "button_click",
                    check=lambda inter: inter.author.id == ctx.author.id and inter.message.id == message.id,
                    timeout=60,
                )
            except asyncio.TimeoutError:
                return await message.edit(
                    embed = self._get_embed(ctx, f"```{affichage}```"),
                    components=[
                        row.disable_components()
                        for row in interaction.message.components
                    ],
                )

            if interaction.custom_id == "Exit":
                embed = self._get_embed(ctx, interaction.message.embeds[0].description)
                return await interaction.edit_origin(
                    embed=embed,
                    components=[
                        row.disable_components()
                        for row in interaction.message.components
                    ],
                )
            elif interaction.custom_id == "⌫":
                lst = list(interaction.message.embeds[0].description.replace("`", ""))
                if len(lst) > 1:
                    try:
                        index = lst.index("|")
                        x = index - 2
                        y = index + 1
                        if lst[x] == "×" and lst[y] == "×":
                            lst.pop(index - 1)
                            lst.pop(index - 2)
                        else:
                            lst.pop(index - 1)
                    except:
                        lst = ["|"]
                affichage = "".join(lst)
                expression = affichage
            elif interaction.custom_id == "Clear":
                expression = ""
                affichage = "|"
            elif interaction.custom_id == "=":
                if "Syntax Error!" in affichage or affichage == "|":
                    affichage = "|"
                else:
                    expression = expression.replace("|", "")
                    expression = self.calculate(expression)
                    affichage = f"{affichage.replace('|','')}={expression}"
                expression = ""
            elif interaction.custom_id == "❮":
                lst = list(interaction.message.embeds[0].description.replace("`", ""))
                if len(lst) > 1:
                    try:
                        index = lst.index("|")
                        lst.remove("|")
                        lst.insert(index - 1, "|")
                    except:
                        lst = ["|"]
                affichage = "".join(lst)
            elif interaction.custom_id == "❯":
                lst = list(interaction.message.embeds[0].description.replace("`", ""))
                if len(lst) > 1:
                    try:
                        index = lst.index("|")
                        lst.remove("|")
                        lst.insert(index + 1, "|")
                    except:
                        lst = ["|"]
                affichage = "".join(lst)
            elif interaction.custom_id == "scientific_mode":
                is_normal_mode = False
                await interaction.edit_origin(
                    embed = self._get_embed(ctx, f"```{affichage}```"),
                    components=self.scientific_components,
                )
            elif interaction.custom_id == "normal_mode":
                is_normal_mode = True
                await interaction.edit_origin(
                    embed = self._get_embed(ctx, f"```{affichage}```"),
                    components=self.normal_components,
                )
            else:
                if "=" in affichage:
                    affichage = ""
                expression = self.input_formatter(
                    original=affichage, label=interaction.component.label
                )
                affichage = expression

            if interaction.custom_id not in ["scientific_mode", "normal_mode"]:
                if is_normal_mode:
                    await interaction.edit_origin(
                        embed = self._get_embed(ctx, f"```{affichage}```"),
                        components=self.normal_components,
                    )
                else:
                    await interaction.edit_origin(
                        embed = self._get_embed(ctx, f"```{affichage}```"),
                        components=self.scientific_components,
                    )
                                   
def setup(client):
    client.add_cog(Calculator(client))
