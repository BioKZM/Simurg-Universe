import discord
import time
import datetime
from discord.ext import commands
from functions.userClass import User,levelNames,experiences



class Level(commands.Cog):
    def __init__(self,client):
        self.client = client


    @commands.command(aliases=["level"])
    async def seviye(self,ctx,member:discord.Member=None):
        if member == None:
            member = ctx.author

        user = User(member.id)
        target = datetime.datetime.fromtimestamp(user.time)
        # day = str(target-datetime.datetime.now())[:-7]
        day = str(target-datetime.datetime.now())[:-10].split(":")
        day[0] = day[0].replace("days","gün")
        # day[0]+" saat",day[1]+" dakika"
        day[0] += " saat"
        day[1] += " dakika"
        embed = discord.Embed(title=f"{member.name}#{member.discriminator} adlı kullanıcının bilgileri",description="",color=0x8d42f5)
        embed.add_field(name="Mevcut değerler - 🏆 ",value="```Seviyesi = {}\nPuanı = {}\nRütbesi = {}\n```".format(user.level,user.XP,user.levelName,inline=False))
        
        if user.isMaxLevel():
            embed.add_field(name="Bir sonraki rütbe",value=f"```{levelNames[user.level]} rütbesi için kalan puan = {(experiences[user.level-1])-user.XP}```" if not user.isMaxLevel() else "```Maksimum seviyeye ulaştınız!```",inline=False)
            embed.add_field(name="Günlük Bilgileri",value = f"```diff\n-Haftalık zorunlu güncellemeye kalan süre = {day[0]} {day[1]}\n```" if not user.time == False else "Günlük bilgisi bulunamadı",inline = False)
        
        elif not user.isMaxLevel():
            if experiences[user.level] - user.XP <= 0:
                embed.add_field(name="Bir sonraki rütbe ",value=f"```{levelNames[user.level+1]} rütbesine ulaştın! Seviye atlamak için ses kanalına girebilirsin.```",inline=False)
                
                
            else:
                
                if user.level == 0:
                    embed.add_field(name="Bir sonraki rütbe ",value=f"```{levelNames[user.level]} rütbesi için kalan puan = {(experiences[user.level])-user.XP}```",inline=False)
                    embed.add_field(name="Günlük Bilgileri",value = f"```diff\n-Haftalık zorunlu güncellemeye kalan süre = {day[0]} {day[1]}\n```" if not user.time == False else "```Günlük bilgisi bulunamadı```",inline = False)
                
                else:
                    embed.add_field(name="Bir sonraki rütbe ",value=f"```{levelNames[user.level+1]} rütbesi için kalan puan = {(experiences[user.level])-user.XP}```",inline=False)
                    embed.add_field(name="Günlük Bilgileri",value = f"```diff\n-Haftalık zorunlu güncellemeye kalan süre = {day[0]} {day[1]}\n```" if not user.time == False else "```Günlük bilgisi bulunamadı```",inline = False)

        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Level(client))