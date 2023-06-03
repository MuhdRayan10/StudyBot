from database import get_subjects, get_user
from discord import app_commands
from discord.ext import commands



class Mom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="today", description="Describe today and plan the day")
    async def today(self, interaction):

        user = get_user(interaction.user.id)

        def check(m, mode:int=1):
            if m.author.id == interaction.author.id and m.channel.id == interaction.channel.id:
                match mode:
                    case 1: return m.content.lower() in ('y', 'n', 'yes', 'no')
        
        await interaction.response.send_message("Hello! Do you want to study today? (y/n)")
        confirmation = await self.bot.wait_for("message", check=lambda m:check(m))

        if not confirmation.conten.lower() in ('y', 'yes'):
            await confirmation.reply("Oh well, enjoy your day then!")
            return
        
        subjects = get_subjects()
        await confirmation.reply("Alright, which all subjects did you do today?")
        

async def setup(self, bot):
    await bot.add_cog(Mom(bot))