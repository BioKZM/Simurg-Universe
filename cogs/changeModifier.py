from discord.ext import commands
import discord
import json
from main import guildID,embedColor
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash import SlashContext,cog_ext
class ChangeModifier(commands.Cog):
    def __init__(self):
        pass


    @cog_ext.cog_slash(
    name = "çarpan-değiştir",
    description = "Seviye sistemi için gerekli olan çarpanların miktarlarını değiştir.",
    guild_ids = guildID,
    options = [
        create_option(
            name = "çarpan_türü",
            description = "Çarpan türünü seç",
            option_type = 3,
            required = True,
            choices = [
                create_choice(
                    name = "Default",
                    value = "default"
                ),
                create_choice(
                    name = "Stream",
                    value = "stream",
                ),
                create_choice(
                    name = "Cam",
                    value = "cam"
                )
            ]
        ),
        create_option(
            name = "çarpan",
            description = "Çarpan değerini gir.",
            option_type = 4,
            required = True
        ),
    ]
)
    async def çarpanDeğiştir(self,ctx,çarpan,çarpan_türü):
        if not ctx.author.id == 639156004596219924 or ctx.author.id == 373457193271558145:
            embed = discord.Embed(
                title = "Hata!",
                description = "Bu komutu kullanmaya iznin yok!",
                color = embedColor
            )
            await ctx.send(embed=embed)
        else:
            with open("files/modifiers.json") as file:
                data = json.load(file)
            with open("files/modifiers.json","w") as file:
                data['çarpan_türü'] = çarpan

            embed = discord.Embed(
                title = "Çarpan değiştirildi!",
                description = f"{çarpan_türü} adlı çarpanın değeri şu değere değiştirildi : {çarpan}",
                color = embedColor
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(ChangeModifier(client))