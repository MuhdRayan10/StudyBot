from discord import app_commands, SelectOption as opt
from database import get_subjects, register_user
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

        grades = Select(min_values=1, options=[opt(label="IX", description="Grade 9", value=9), opt(label="X", description="Grade 10", value=10)])
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

            subjects = [opt(label=sub[0], description=len(sub[1])) for sub in get_subjects(grades.values[0])]
            subj = Select(min_values=1, options=subjects)

            # TO DO SUBJECTS, STRONG & WEAK SUBJ
            weak, strong = None, None

            breaks = await self.bot.wait_for("message", check=lambda m:check(m, 3))
            await breaks.reply("Almost done! How good / fast are you at studies?\n(This will determine your skill level, so the higher the difficulty the faster you are expected to complete stuff)\nType 1 if you're super good, 2 if you're decent, and 1 if you're average")

            speed = await self.bot.wait_for("message", check=lambda m:check(m, 2))
            await speed.reply("Perfect! Now you're officially a ~~nerd~~ studious person!\n(Or at least, you've taken your first steps!)") 

            breaks = [int(x.strip()) for x in breaks.content.split(',')]

            register_user(name.content, interaction.user.id, grades.values[0], subj.values, weak.values, strong.values, breaks[0], breaks[1], int(hours.content), speed)

            del name, grades, weak, weak_subj, strong, strong_subj, breaks, hours, speed

        view = View()
        view.add_item(grades)





async def setup(bot):
    await bot.add_cog(DumbleDore(bot))