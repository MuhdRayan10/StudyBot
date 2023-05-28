from discord import app_commands
from discord.ext import commands
import discord
import sqlite3

class DumbleDore:
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='register', description="Start managing your studies!")
    async def register(self, interaction:discord.Interaction, grade:int):
        db = sqlite3.connect("./data/users.db")
        c = db.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, grade INTEGER, subjects TEXT, strengths TEXT, weaknesses TEXT, breaks TEXT, holidays TEXT)")
        db.commit()

        await interaction.response.send_message("Great!")

async def setup(bot):
    await bot.add_cog(DumbleDore(bot))