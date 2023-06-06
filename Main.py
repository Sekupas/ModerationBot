import nextcord
import sqlite3
from tabulate import tabulate #удобный модуль для рисования таблиц
from nextcord.ext import commands
from nextcord.ui import Button, View




intents = nextcord.Intents.all()
intents.members = True
intents.typing = True
intents.message_content = True
intents.presences = True

activity = nextcord.Activity(type=nextcord.ActivityType.listening, name="Музычку")


bot = commands.Bot(command_prefix='>>>', intents=intents, activity=activity, status=nextcord.Status.online)
@bot.event
async def on_ready():
    auth = f'Авторизован как {bot.user} (ID: {bot.user.id})'
    print(auth)
    print('-'*len(auth))

@bot.slash_command()
async def mute(ctx, user: nextcord.User, reason: str):
    mute_24h = Button(label='Mute for 24h', style=nextcord.ButtonStyle.red, emoji='🔇')
    mute_3d = Button(label='Mute for 3d', style=nextcord.ButtonStyle.red, emoji='🔇')
    mute_5d = Button(label='Mute for 5d', style=nextcord.ButtonStyle.red, emoji='🔇')
    mute_10d = Button(label='Mute for 10d', style=nextcord.ButtonStyle.red, emoji='🔇')
    cancel = Button(label='cancel', style=nextcord.ButtonStyle.red, emoji='❌')

    async def mute24h_callback(interaction):
        await interaction.response.edit_message(content=f'Successfully muted user {user.mention} for 24 hours with reason: {reason}', view=None)

    async def mute3d_callback(interaction):
        await interaction.response.edit_message(content=f'Successfully muted user {user.mention} for 3 days with reason: {reason}', view=None)

    async def mute5d_callback(interaction):
        await interaction.response.edit_message(content=f'Successfully muted user {user.mention} for 5 days with reason: {reason}', view=None)

    async def mute10d_callback(interaction):
        await interaction.response.edit_message(content=f'Successfully muted user {user.mention} for 10 days with reason: {reason}', view=None)

    async def cancel_callback(interaction):
        await interaction.response.edit_message(content='Successfully cancelled', view=None)

    mute_24h.callback = mute24h_callback
    mute_3d.callback = mute3d_callback
    mute_5d.callback = mute5d_callback
    mute_10d.callback = mute10d_callback
    cancel.callback = cancel_callback

    view = View()
    view.add_item(mute_24h)
    view.add_item(mute_3d)
    view.add_item(mute_5d)
    view.add_item(mute_10d)
    view.add_item(cancel)

    await ctx.send(f'The user {user.mention} was being muted with reason **{reason}** for what time?', view=view)



from config import TOKEN
bot.run(TOKEN)