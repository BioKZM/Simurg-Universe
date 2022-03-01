import json
import os
from discord.ext import commands
from discord.utils import get
from main import path,client
class OnMemberJoin(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = client.get_channel(937332237362401301)
        role = get(member.guild.roles,name = "Misafir")
        if not os.path.exists(path+f"/{member.id}.json"):
            data = {
                'isim' : '',
                'soyisim' : '',
                'XP' : 0,
                'level' : 0,
                'modifier' : 1,
                'maximumXP' : 249,
                'tanitimBool' : True,
                'time' : 0,
            }
            with open(path+f"/{member.id}.json","w") as file:
                json.dump(data,file,indent=4)

        await member.edit(nick = "👀 Simurg Visitor") 
        await member.add_roles(role)
        await channel.send(f"**{member.name}** ({member.mention}) sunucuya katıldı! Simurg Evrenine hoşgeldin.")

def setup(client):
    client.add_cog(OnMemberJoin(client))