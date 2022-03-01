import datetime
import json
from discord.utils import get
from discord.ext import commands,tasks
from cogs.journal import Journal
from main import path,client

class JournalControl(commands.Cog):
    def __init__(self,client):
        self.client = client

    @tasks.loop(hours=24)
    async def günlükControl():
        guild = client.guilds[0]
        for member in client.get_all_members():
            with open(path+f"/{member.id}.json") as file:
                data = json.load(file)

            target = datetime.datetime.fromtimestamp(data['time']) + datetime.timedelta(days=7)
            if datetime.datetime.now() == target:
                channel = get(guild.channels,name = f"{member.name}-{member.discriminator}")
                await channel.delete()

    @günlükControl.before_loop
    async def before_günlükControl():
        await client.wait_until_ready()
        print("Günlük Control Loop OK!")
    günlükControl.start()



def setup(client):
    client.add_cog(JournalControl(client))