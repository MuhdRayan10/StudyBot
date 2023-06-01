from discord import app_commands, SelectOption as opt
from discord.ext import commands
from discord.ui import Select, View
import discord
import sqlite3

class DumbleDore(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='register', description="Start managing your studies!")
    async def register(self, interaction:discord.Interaction, grade:int):
        
        await interaction.response.defer()
        
        db = sqlite3.connect("./data/users.db")
        c = db.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, grade INTEGER, subjects TEXT, strengths TEXT, weaknesses TEXT, breaks TEXT, holidays TEXT)")
        db.commit()

        grades = Select(min_values=1, options=[opt(label="IX", description="Grade 9"), opt(label="X", description="Grade 10")])
        grades.callback = self.grade_clicked

        view = View()
        view.add_item(grades)
        
        await interaction.followup.send("Choose your grade!", view=view)

    async def grade_clicked(self, interaction):
        await interaction.response.send_message("grade")



async def setup(bot):
    await bot.add_cog(DumbleDore(bot))