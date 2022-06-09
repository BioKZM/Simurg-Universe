import datetime
import json
from discord.utils import get
from discord.ext import commands,tasks
from cogs.journal import Journal
from main import path,client

class JournalControl(commands.Cog):
    def __init__(self,client):
        self.client = client

    @tasks.loop(minutes=1)
    async def günlükControl():
        guild = client.guilds[0]
        for member in client.get_all_members():
            with open(path+f"/{member.id}.json") as file:
                data = json.load(file)

            target = data['time']
            today = datetime.datetime.timestamp(datetime.datetime.now())
            if target-today <= 0:
                channel = get(guild.channels,name = f"{member.display_name.lower()}-{member.discriminator}")
				
                try:
                    await channel.delete()
                    data['time'] = False
                    with open(path+f"/{member.id}.json","w") as file:
                        json.dump(data,file,indent=4)
                except Exception:
                    pass

    @günlükControl.before_loop
    async def before_günlükControl():
        await client.wait_until_ready()
        print("Günlük Control Loop OK!")
    günlükControl.start()



def setup(client):
    client.add_cog(JournalControl(client))