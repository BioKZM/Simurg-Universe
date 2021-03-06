import discord
import json
import time
import datetime
from discord.ext import commands
from discord.utils import get
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash import SlashContext,cog_ext
from main import guildID,path,embedColor


class Journal(commands.Cog):
    def __init__(self,client):
        self.client = client

    @cog_ext.cog_slash(
	name = "günlük",
	description = "Kendi gelişmelerini, diğer kullanıcılarla paylaşabileceğin odayı oluştur.",
	guild_ids = guildID,
)
    async def günlük(self,ctx):
        with open(path+f"/{ctx.author.id}.json") as file:
            data = json.load(file)

        if data['time']:
            embed = discord.Embed(
                title = "Hata!",
                description = "Zaten bir kanala sahipsin!",
                color = embedColor
            )
            await ctx.send(embed=embed)

        else:
            date_ = datetime.datetime.timestamp(datetime.datetime.now() + datetime.timedelta(days=15))
            data['time'] = date_
            with open(path+f"/{ctx.author.id}.json","w") as file:
                json.dump(data,file,indent=4)
        

            misafir = get(ctx.guild.roles,name="Misafir")
            overwrites = {
                ctx.guild.default_role : discord.PermissionOverwrite(
                    add_reactions = False,
                    attach_files = False,
                    embed_links = False,
                    external_emojis = False,
                    read_message_history = False,
                    read_messages = False,
                    send_messages = False,
                    view_channel = False,
                ),
                misafir : discord.PermissionOverwrite(
                    add_reactions = True,
                    attach_files = False,
                    embed_links = False,
                    external_emojis = True,
                    read_message_history = True,
                    read_messages = True,
                    send_messages = False,
                    view_channel = True,
                ),
                ctx.author : discord.PermissionOverwrite(
                    add_reactions = True,
                    attach_files = True,
                    embed_links = True,
                    external_emojis = True,
                    read_message_history = True,
                    read_messages = True,
                    send_messages = True,
                    view_channel = True,
                    
                )
            }
            category = get(ctx.guild.channels,name = "Günlük")
            channel = await ctx.guild.create_text_channel(name = f"{ctx.author.display_name}-{ctx.author.discriminator}",category = category, overwrites=overwrites)
            embed = discord.Embed(
                title = "İşlem başarılı!",
                description = f"{channel.mention} başarıyla oluşturuldu!",
                color = embedColor
            )
            await ctx.send(embed=embed)
            embed = discord.Embed(
                title = "Yardım",
                description = f"Selam {ctx.author.mention}! Kendi odanı oluşturup bizimle tecrübeni paylaşmak istediğin için teşekkürler. \n\nBu kanalla ilgili unutmaman gereken tek bir şey var, eğer bir hafta boyunca herhangi bir paylaşım yapmazsan, kanal kendi kendini imha edecektir. \n\nKanalın silinmeden önce ne kadar zamanı kaldığını `!level` komutu ile öğrenebilirsin. \n\nTekrardan teşekkürler ve başarılar!",
                color = embedColor
            )
            message = await channel.send(embed=embed)
            await message.pin()

def setup(client):
    client.add_cog(Journal(client))