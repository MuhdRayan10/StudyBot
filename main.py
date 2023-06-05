from discord import app_commands
from discord.ext import commands
import os


class StudyBot(commands.Bot):
    async def __init__(self):
        pass

    async def on_ready(self):
        print(f"Connectec as {self.user.name}")


bot = StudyBot()
bot.run(os.getenv("TOKEN"))
