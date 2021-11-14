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
from math import *
import asyncio

client = commands.Bot(command_prefix = "&", intents=discord.Intents.all())

def calculate(exp:str):
    result=''
    o=exp
    o=o.replace('π', str(pi))
    o=o.replace('τ', str(tau))
    o=o.replace('e', str(e))
    o=o.replace('×', '*')
    o=o.replace('÷', '/')
    o=o.replace('^2', '**2')
    o=o.replace('^3', '**3')
    o=o.replace('^', '**')
    o=o.replace('√', 'sqrt')
    try:
        result = eval(o, {'sqrt': sqrt})
    except:
        result=f"Syntax Error!\nDon't forget the sign(s) ('×', '÷', ...).\nnot: 3(9+1) but 3×(9+1)"
    return result

def input_formatter(original:str, new:str):
    if 'Syntax Error!' in original:
        original='|'
    lst=list(original)
    try:
        index=lst.index('|')
        lst.remove('|')
    except:
        index=0
    if new == '1':
        lst.insert(index, '1')
    elif new == '2':
        lst.insert(index, '2')
    elif new == '3':
        lst.insert(index, '3')
    elif new == '4':
        lst.insert(index, '4')
    elif new == '5':
        lst.insert(index, '5')
    elif new == '6':
        lst.insert(index, '6')
    elif new == '7':
        lst.insert(index, '7')
    elif new == '8':
        lst.insert(index, '8')
    elif new == '9':
        lst.insert(index, '9')
    elif new == '10':
        lst.insert(index, '10')
    elif new == '0':
        lst.insert(index, '0')
    elif new == '00':
        lst.insert(index, '00')
    elif new == '+':
        lst.insert(index, '+')
    elif new == '÷':
        lst.insert(index, '÷')
    elif new == '-':
        lst.insert(index, '-')
    elif new == '×':
        i=index-1
        try:
            if lst[i]=='×':
                lst.insert(index+1, '|')
                original=''.join(lst)
                return original
        except:
            lst.insert(index+1, '|')
            original=''.join(lst)
            return original
        try:
            if lst[index]=='×':
                lst.insert(index, '|')
                original=''.join(lst)
                return original
            else:
                lst.insert(index, '×')
        except:
            lst.insert(index, '×')
    elif new == '.':
        lst.insert(index, '.')
    elif new == '(':
        lst.insert(index, '(')
    elif new == ')':
        lst.insert(index, ')')
    elif new == 'π':
        lst.insert(index, 'π')
    elif new == 'X²':
        if '^' in lst:
            pass
        else:
            lst.insert(index, '^2')
    elif new == 'X³':
        if '^' in lst:
            pass
        else:
            lst.insert(index, '^3')
    elif new == 'Xˣ':
        if '^' in lst:
            pass
        else:
            lst.insert(index, '^')
    elif new == 'e':
        lst.insert(index, 'e')
    elif new == 'τ':
        lst.insert(index, 'τ')
    elif new == '000':
        lst.insert(index, '000')
    elif new == '√':
        lst.insert(index, '√()')
    lst.insert(index+1, '|')
    original=''.join(lst)
    return original
  
buttons_one = [
        [
            Button(style=ButtonStyle.grey, label='1', id='1'),
            Button(style=ButtonStyle.grey, label='2', id='2'),
            Button(style=ButtonStyle.grey, label='3', id='3'),
            Button(style=ButtonStyle.blue, label='×', id='×'),
            Button(style=ButtonStyle.red, label='Exit', id='Exit')
        ],
        [
            Button(style=ButtonStyle.grey, label='4', id='4'),
            Button(style=ButtonStyle.grey, label='5', id='5'),
            Button(style=ButtonStyle.grey, label='6', id='6'),
            Button(style=ButtonStyle.blue, label='÷', id='÷'),
            Button(style=ButtonStyle.red, label='⌫', id='⌫')
        ],
        [
            Button(style=ButtonStyle.grey, label='7', id='7'),
            Button(style=ButtonStyle.grey, label='8', id='8'),
            Button(style=ButtonStyle.grey, label='9', id='9'),
            Button(style=ButtonStyle.blue, label='+', id='+'),
            Button(style=ButtonStyle.red, label='Clear', id='Clear')
        ],
        [
            Button(style=ButtonStyle.grey, label='00', id='00'),
            Button(style=ButtonStyle.grey, label='0', id='0'),
            Button(style=ButtonStyle.grey, label='.', id='.'),
            Button(style=ButtonStyle.blue, label='-', id='-'),
            Button(style=ButtonStyle.green, label='=', id='=')
        ],
        [
            Button(style=ButtonStyle.green, label='❮', id='❮'),
            Button(style=ButtonStyle.green, label='❯', id='❯'),
            Button(style=ButtonStyle.grey, label='Change to scientific mode', emoji='\U0001f9d1\u200D\U0001f52c', id='400')
        ],
    ]
buttons_two = [
        [
            Button(style=ButtonStyle.grey, label='(', id='('),
            Button(style=ButtonStyle.grey, label=')', id=')'),
            Button(style=ButtonStyle.grey, label='π', id='π'),
            Button(style=ButtonStyle.blue, label='×', id='×'),
            Button(style=ButtonStyle.red, label='Exit', id='Exit')
        ],
        [
            Button(style=ButtonStyle.grey, label='X²', disabled=True),
            Button(style=ButtonStyle.grey, label='X³', disabled=True),
            Button(style=ButtonStyle.grey, label='Xˣ', disabled=True),
            Button(style=ButtonStyle.blue, label='÷', id='÷'),
            Button(style=ButtonStyle.red, label='⌫', id='⌫')
        ],
        [
            Button(style=ButtonStyle.grey, label='e', id='e'),
            Button(style=ButtonStyle.grey, label='τ', id='τ'),
            Button(style=ButtonStyle.grey, label='000', id='000'),
            Button(style=ButtonStyle.blue, label='+', id='+'),
            Button(style=ButtonStyle.red, label='Clear', id='Clear')
        ],
        [
            Button(style=ButtonStyle.grey, label='√', id='√'),
            Button(style=ButtonStyle.grey, label=' ', disabled=True),
            Button(style=ButtonStyle.grey, label=' ', disabled=True),
            Button(style=ButtonStyle.blue, label='-', id='-'),
            Button(style=ButtonStyle.green, label='=', id='=')
        ],
        [
            Button(style=ButtonStyle.green, label='❮', id='❮'),
            Button(style=ButtonStyle.green, label='❯', id='❯'),
            Button(style=ButtonStyle.grey, label='Change to normal modeㅤ', emoji='\U0001f468\u200D\U0001f3eb', id='401')
        ],
    ]
    
@client.event
async def on_ready():#loading bot and status
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print('Made by Polsulpicien#5020 | https://github.com/Polsulpicien')
    DiscordComponents(client)
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(name="github.com/Polsulpicien", type=discord.ActivityType.watching))
       
@client.command(aliases=['calc', 'calculator'])
@commands.max_concurrency(1, per=commands.BucketType.user)
async def calcu(ctx):
    affichage='|'
    id=1
    e = discord.Embed(title=f'{ctx.author}\'s calculator', description=f'```{affichage}```', color=int("2f3136", 16))
    e.set_footer(text=f"https://github.com/Polsulpicien")
    expression=''
    m = await ctx.send(components=buttons_one, embed=e)

    def checkUp(res):
        return res.user.id == ctx.author.id and res.channel.id == ctx.channel.id and res.message.id==m.id

    while True:
        try:
            res = await client.wait_for('button_click', check=checkUp, timeout=60) 
        except asyncio.TimeoutError:
            a = discord.Embed(title=f'{ctx.author}\'s calculator', description=f'```{affichage}```', color=int("2f3136", 16))
            a.set_footer(text=f"https://github.com/Polsulpicien")
            return await m.edit(embed=a)
        else:
            if str(res.author) == str(res.message.embeds[0].title.split("'s calculator")[0]):
                if res.component.id == 'Exit':
                    q = discord.Embed(title=f'{ctx.author}\'s calculator', description=f'{res.message.embeds[0].description}', color=int("2f3136", 16))
                    q.set_footer(text=f"https://github.com/Polsulpicien")
                    return await res.respond(embed=q, components=[], type=7)
                elif res.component.id == '⌫':
                    lst=list(res.message.embeds[0].description.replace('`',''))
                    if len(lst)>1:
                        try:
                            index=lst.index('|')
                            x=index-2
                            y=index+1
                            if lst[x]=='×' and lst[y]=='×':
                                lst.pop(index-1)
                                lst.pop(index-2)
                            else:
                                lst.pop(index-1)
                        except:
                            lst=['|']
                    affichage=''.join(lst)
                    expression=affichage
                elif res.component.id == 'Clear':
                    expression=''
                    affichage='|'
                elif res.component.id == '=':
                    if 'Syntax Error!' in affichage or affichage=='|':
                        expression=''
                        affichage='|'
                    else:
                        expression=expression.replace('|','')
                        expression = calculate(expression)
                        affichage=f"{affichage.replace('|','')}={expression}"
                        expression=''
                elif res.component.id == '❮':
                    lst=list(res.message.embeds[0].description.replace('`',''))
                    if len(lst)>1:
                        try:
                            index=lst.index('|')
                            lst.remove('|')
                            lst.insert(index-1, '|')
                        except:
                            lst=['|']
                    affichage=''.join(lst)
                elif res.component.id == '❯':
                    lst=list(res.message.embeds[0].description.replace('`',''))
                    if len(lst)>1:
                        try:
                            index=lst.index('|')
                            lst.remove('|')
                            lst.insert(index+1, '|')
                        except:
                            lst=['|']
                    affichage=''.join(lst)
                elif res.component.id == '400':
                    id=2
                    e = discord.Embed(title=f'{ctx.author}\'s calculator', description=f'```{affichage}```', color=int("2f3136", 16))
                    e.set_footer(text=f"https://github.com/Polsulpicien")
                    await res.respond(embed=e, components=buttons_two, type=7)
                elif res.component.id == '401':
                    id=1
                    e = discord.Embed(title=f'{ctx.author}\'s calculator', description=f'```{affichage}```', color=int("2f3136", 16))
                    e.set_footer(text=f"https://github.com/Polsulpicien")
                    await res.respond(embed=e, components=buttons_one, type=7)
                else:
                    if '=' in affichage:
                        affichage=''
                    expression = input_formatter(original=affichage, new=res.component.label)
                    affichage=expression
                if res.component.id != '400' and res.component.id!='401':
                    e = discord.Embed(title=f'{ctx.author}\'s calculator', description=f'```{affichage}```', color=int("2f3136", 16))
                    e.set_footer(text=f"https://github.com/Polsulpicien")
                    if id==1:
                        await res.respond(embed=e, components=buttons_one, type=7)
                    else:
                        await res.respond(embed=e, components=buttons_two, type=7)
                            
client.run("BOT TOKEN HERE") 
