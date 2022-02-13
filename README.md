<div align="center">
    <a href="https://discord.gg/xm9QX3Q"><img src="https://cdn.discordapp.com/attachments/831872376140070943/848225322640998400/polsu.png" alt="polsu logo" height="128" style="border-radius: 50%"></a>
    <h1>Discord Python Advanced Calculator</h1>
</div>
<div align="center">
        <a href="https://discord.gg/xm9QX3Q"><img src="https://img.shields.io/discord/761623845119328257?color=blue&label=Discord&logo=discord&style=for-the-badge" alt="Discord"></a>
        <a href="https://github.com/Polsulpicien/discord.py-advanced-calculator"><img src="https://img.shields.io/github/stars/Polsulpicien/discord.py-advanced-calculator?style=for-the-badge" alt="Stars"></a>
        <a href="https://github.com/Polsulpicien/discord.py-advanced-calculator"><img src="https://img.shields.io/github/v/release/polsulpicien/discord.py-advanced-calculator?color=red&label=Version&logo=github&style=for-the-badge" alt="Version"></a>
</div>
<p align="center">
    <h3>[UPDATED!] An Advanced Calculator maybe with Discord Buttons in python</h3>
</p>

  • [Introduction](https://github.com/Polsulpicien/discord.py-advanced-calculator/#introduction)  
  • [Screenshots](https://github.com/Polsulpicien/discord.py-advanced-calculator/#screenshots)  
  • [Setup](https://github.com/Polsulpicien/discord.py-advanced-calculator/#setup)  
  • [License](https://github.com/Polsulpicien/discord.py-advanced-calculator/#license) 

## Introduction
  
This was the first version of the calculator, made for my discord bot, **[Polsu](https://github.com/Polsu-Discord)** using discord-components.  

If you want to try the calculator or need help, join the **[support server](https://discord.gg/xm9QX3Q)**  
**Please don't change the footer text of the embeds.**  
**Don't forget to give a star if you like it :)**

## Screenshots

![Screenshot](https://media.discordapp.net/attachments/803308630404235264/942376137944883290/unknown.png)
![ScreenShot](https://media.discordapp.net/attachments/803308630404235264/942376182899413053/unknown.png)

## Setup

__Step 1:__
Install [Discord-Components](https://github.com/kiki7000/discord.py-components)
```pip install --upgrade discord-components ```
Install [TagScriptEngine](https://github.com/JonSnowbd/TagScript)
```pip install TagScriptEngine```

__Step 2:__
Choose if you want between the [Main.py](https://github.com/Polsulpicien/discord.py-advanced-calculator/blob/main/main.py) or the [Cog.py](https://github.com/Polsulpicien/discord.py-advanced-calculator/blob/main/calculator.py)

• For the Main.py File, you need to add your Discord Bot Token (which you can find **[HERE](https://discord.com/developers/applications)**), to the **[last line](https://github.com/Polsulpicien/discord.py-advanced-calculator/blob/main/main.py#L328)**:
```py
client.run("TOKEN")
```

• For the Cog.py, you just need to add the file to your Bot's Cogs File. You will also have to add this line to your `on_ready` event: `DiscordComponents(client)`, example:
```py
@client.event
async def on_ready():
    DiscordComponents(client)
```
and of course, don't forget to import discord_components in your main file: `from discord_components import DiscordComponents`!

**If you get: 'Interaction Failed'**  
Make sure to have `client = commands.Bot(command_prefix = "&", intents=discord.Intents.all()) ` (**intents=discord.Intents.all()**)
in your main.py file!

## License
This project is under the [MIT License](https://github.com/Polsulpicien/discord.py-advanced-calculator/blob/main/LICENSE).
