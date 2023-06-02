from discord import app_commands, SelectOption as opt
from discord.ext import commands
from discord.ui import Select, View
import discord
import sqlite3

class DumbleDore(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='register', description="Start managing your studies!")
    async def register(self, interaction:discord.Interaction):
        
        db = sqlite3.connect("./data/users.db")
        c = db.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, grade INTEGER, subjects TEXT, strengths TEXT, weaknesses TEXT, breaks TEXT, holidays TEXT)")
        db.commit()

        grades = Select(min_values=1, options=[opt(label="IX", description="Grade 9"), opt(label="X", description="Grade 10")])
        grades.callback = grade_clicked

        async def grade_clicked(interaction):
           await interaction.response.defer()

           await interaction.followup.send("Great! What shall I call you?")

           def check(m, mode:int):
            if m.author.id == interaction.user.id and m.channel.id == interaction.channel.id :
                match mode:
                  case 1: return True
                  case 2: return m.content.isdigit()
                  case 3: return ',' in m.content
            
            
           
           name = await self.bot.wait_for("message", check=lambda m: check(m, 1), timeout=15)
           await name.reply(f"That's nice to hear, {name.content.title()}!\nAre there any days where you can't learn? (1 for Sun, 2 for Mon etc.)")
           
           holidays = await self.bot.wait_for("message", check=lambda m: check(m, 2))
           await holidays.reply("Alright, that's great to hear!\nHow many hours (1 for 1 hr, 2 for 2 hrs etc.) do you wish to dedicate to studying (+ homework) each day?")

           hours = await self.bot.wait_for("message", check=lambda m: check(m, 2))
           await hours.reply("Which subjects do you feel weak in / need to concentrate more on?")

           weak_subj = await self.bot.wait_for("message", check=lambda m:check(m, 1))
           await weak_subj.reply("Which subjects are your strengths / need to concentrate less on?")

           strong_subj = await self.bot.wait_for("message", check=lambda m:check(m, 1))
           await strong_subj.reply("How many breaks do you want in an hour? How long?\nGive your response as integers separated by a comma\n(For eg: `2, 5`)")

           breaks = await self.bot.wait_for("message", check=lambda m:check(m, 1))
           await breaks.reply("Perfect! Now you're officially a ~~nerd~~ studious person!\n(Or at least, you've taken your first steps!)") 


        view = View()
        view.add_item(grades)
    
    
    
        




async def setup(bot):
    await bot.add_cog(DumbleDore(bot))