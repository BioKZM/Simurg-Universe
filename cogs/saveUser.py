import discord
import json
from discord.ext import commands
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash import SlashContext,cog_ext
from main import guildID,embedColor,path


class SaveUser(commands.Cog):
    def __init__(self):
        pass

    @cog_ext.cog_slash(
	name = "kullanıcı-kaydet",
	description = "Kullanıcının ismini ve soyismini girerek, hesabını onayla",
	guild_ids = guildID,
	options = [
		create_option(
			name = "kullanıcı",
			description = "Kullanıcıyı seç.",
			option_type=6,
			required=True,
		),
		create_option(
			name = "isim",
			description = "İsmini gir.",
			option_type = 3,
			required=True,
	),
		create_option(
			name = "soyisim",
			description = "Soyismini gir.",
			option_type = 3,
			required=False
	)]
)
    async def kullanıcıKaydet(self,ctx,kullanıcı,isim,soyisim=None):
        if not ctx.author.id == 639156004596219924 or ctx.author.id == 373457193271558145:
            embed = discord.Embed(
                title = "Hata!",
                description = "Bu komutu kullanmaya iznin yok!",
                color = embedColor
            )
            await ctx.send(embed=embed)
        else:
            if soyisim == None:
                soyisim = ""
            await kullanıcı.edit(nick = isim+" "+soyisim)
            with open(path+f"/{kullanıcı.id}.json") as file:
                data = json.load(file)

            data['isim'] = isim
            data['soyisim'] = soyisim
            
            with open(path+f"/{kullanıcı.id}.json","w") as file:
                json.dump(data,file,indent = 4)

            embed = discord.Embed(title = "Kullanıcı Adı",description =f"Kullanıcı adı şuna değiştirildi: **{isim} {soyisim}**", color = embedColor)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(SaveUser(client))


