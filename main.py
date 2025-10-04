import discord
from discord.ext import commands
import os

TOKEN = "YOUR_BOT_TOKEN_HERE"
OWNER_ID = 229508905582067712
PREFIX = "+"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.check
async def owner_only(ctx):
    if ctx.author.id != OWNER_ID:
        await ctx.send("🚫 You aren’t cool enough to use this command. Get better. 😎")
        return False
    return True

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    print("🧠 Jishaku loaded successfully (owner only).")

@bot.event
async def setup_hook():
    try:
        await bot.load_extension("jishaku")
        print("⚙️ Jishaku extension loaded successfully.")
    except Exception as e:
        print(f"❌ Failed to load Jishaku: {e}")

if __name__ == "__main__":
    try:
        bot.run(TOKEN)
    except Exception as e:
        print(f"💥 Error while running the bot: {e}")
