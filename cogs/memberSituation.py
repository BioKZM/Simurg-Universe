import json
from discord.ext import commands
from main import path,client

class MemberSituation(commands.Cog):
    def __init__(self,client):
        self.client = client

    def memberSituation(self,prev,cur):
        if prev.channel and cur.channel:
            if cur.self_stream and cur.self_video:
                return "stream + cam"
            if cur.self_stream:
                return "stream"
            if cur.self_video:
                return "cam"
            elif not cur.self_stream and not cur.self_video:
                return ""        

    @commands.Cog.listener()
    async def on_voice_state_update(self,member,prev,cur):
        if not member.bot:	
            if self.memberSituation(prev,cur) == "stream":
                with open("userFiles/modifiers.json") as file:
                    modifiers = json.load(file)
                    modifier = modifiers['stream']
                with open(path+f"/{member.id}.json") as file:
                    data = json.load(file)
                data['modifier'] = modifier
            
            elif self.memberSituation(prev,cur) == "cam":
                with open("userFiles/modifiers.json") as file:
                    modifiers = json.load(file)
                    modifier = modifiers['cam']
                with open(path+f"/{member.id}.json") as file:
                    data = json.load(file)
                data['modifier'] = modifier
            
            elif self.memberSituation(prev,cur) == "stream + cam":
                with open("userFiles/modifiers.json") as file:
                    modifiers = json.load(file)
                    modifier = modifiers['stream'] + modifiers['cam']
                with open(path+f"/{member.id}.json") as file:
                    data = json.load(file)
                data['modifier'] = modifier   
                
            elif self.memberSituation(prev,cur) == "":
                with open("userFiles/modifiers.json") as file:
                    modifiers = json.load(file)
                    modifier = modifiers['default']
                with open(path+f"/{member.id}.json") as file:
                    data = json.load(file)
                data['modifier'] = modifier

def setup(client):
    client.add_cog(MemberSituation(client))