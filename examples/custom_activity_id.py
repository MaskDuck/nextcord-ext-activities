# kinda useless since nextcord allow you to directly pass the id, but heck yeah.
import nextcord
from nextcord.ext import activities, commands

bot = commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
    print(f"Logged in as {str(bot.user)} (ID {bot.user.id})")


@bot.command()
async def custom(ctx, channel: nextcord.VoiceChannel):
    activity_id = 1234567890  # this is a fake one, put a real id there.
    invite_link = await channel.create_activity_invite(
        activities.Activity.custom, activity_id=activity_id
    )
    await ctx.send(invite_link.url)


bot.run("token here")
