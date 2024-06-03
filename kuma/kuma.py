from discord.ext import commands, tasks
import aiohttp

HEARTBEAT_URI = "https://status.qservices.cc/api/push/EWy8sqTbrW?status=up&msg=OK&ping=" 

class Uptime_Status_Agent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.heartbeat.start()

    def cog_unload(self):
        self.heartbeat.cancel()

    @tasks.loop(seconds=30)
    async def heartbeat(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(HEARTBEAT_URI) as response:
                print("Heartbeat Sent")

    @heartbeat.before_loop
    async def before_heartbeat(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(Uptime_Status_Agent(bot))
