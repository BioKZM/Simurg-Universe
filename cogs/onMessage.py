import datetime
import json
from discord.ext import commands
from main import path,client

class OnMessage(commands.Cog):
    def __init__(self):
        pass

    @commands.Cog.listener()
    async def on_message(self,message):
        channel = str(message.channel)
        if channel == f"{message.author.name}-{message.author.discriminator}":

            with open(path+f"/{message.author.id}.json") as file:
                data = json.load(file)
            data['time'] == datetime.datetime.now()
            with open(path+f"/{message.author.id}.json") as file:
                json.dump(data,file,indent=4)



        if channel == "kendini-tanıt":
            with open(path+f"/{message.author.id}.json") as file:
                data = json.load(file)
            if data['tanitimBool'] == True:
                data['XP'] += 250
                data['tanitimBool'] = False
                with open(path+f"/{message.author.id}.json","w") as file:
                    json.dump(data,file,indent=4)
                messageChannel = client.get_channel(937383578394832976)
                await messageChannel.send(f"Tebrikler {message.author.mention}! <#937105488557010994> kanalında kendinizi tanıttığınız için, 250 XP kazandınız!")

def setup(client):
    client.add_cog(OnMessage(client))