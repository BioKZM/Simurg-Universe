import discord
import time
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
        embed = discord.Embed(title=f"{member.name}#{member.discriminator} adlı kullanıcının bilgileri",description="",color=0x8d42f5)
        embed.add_field(name="Mevcut değerler - 🏆 ",value="Seviyesi = **{}**\n Puanı = **{}**\n Rütbesi = **{}**\n".format(user.level,user.XP,user.levelName,inline=False))
        
        if user.isMaxLevel():
            embed.add_field(name="Bir sonraki rütbe",value=f"**{levelNames[user.level]}** rütbesi için kalan puan = **{(experiences[user.level-1])-user.XP}**" if not user.isMaxLevel() else "Maksimum seviyeye ulaştınız!",inline=False)
            embed.add_field(name="Günlük Bilgileri",description = f"Haftalık zorunlu gnücellemeye kalan süre = **{user.time-time.time()}**" if not user.time == False else "Günlük bilgisi bulunamadı")
        
        elif not user.isMaxLevel():
            if experiences[user.level] - user.XP <= 0:
                embed.add_field(name="Bir sonraki rütbe ",value=f"**{levelNames[user.level+1]}** rütbesine ulaştın! Seviye atlamak için ses kanalına girebilirsin.",inline=False)
                
            else:
                if user.level == 0:
                    embed.add_field(name="Bir sonraki rütbe ",value=f"**{levelNames[user.level]}** rütbesi için kalan puan = **{(experiences[user.level])-user.XP}**",inline=False)
                else:
                    embed.add_field(name="Bir sonraki rütbe ",value=f"**{levelNames[user.level+1]}** rütbesi için kalan puan = **{(experiences[user.level])-user.XP}**",inline=False)

        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Level(client))