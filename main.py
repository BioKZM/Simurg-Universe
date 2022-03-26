"""
MIT License

Copyright (c) 2022 Berke Akbay

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

import discord
import os
import json
from discord.ext import commands
from discord_slash import SlashCommand
from keep_alive import keep_alive

TOKEN = os.environ["TOKEN"]

keep_alive()

client = commands.Bot(command_prefix=['!','-'], intents=discord.Intents.all(),help_command=None,case_insensitive=True)
intents = discord.Intents.all()
intents.members = True
guildID = [841307853629423656]
slash = SlashCommand(client,sync_commands=True)
path = "userFiles/levels"
embedColor = 0xf1612a


@client.event
async def on_ready():
	print("Simurg Rising!")
	await client.change_presence(status=discord.Status.online,activity=discord.Game("The most beautiful bird of the Simurg Universe."))


cogs = ["cogs.changeModifier","cogs.journal","cogs.journalControl","cogs.memberSituation","cogs.onMemberJoin","cogs.onMessage","cogs.saveUser","cogs.voiceLoop","cogs.rank","cogs.level"]

for cog in cogs:
    client.load_extension(cog)



client.run(TOKEN)