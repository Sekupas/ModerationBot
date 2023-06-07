import nextcord
import sqlite3
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
    print('+', '-' * len(auth), '+')
    print('|', auth, '|')
    print('+', '-'*len(auth), '+')


def view_items(list, timeout=180):
    view = View(timeout=timeout)
    for item in list:
        view.add_item(item)
    return view

class Buttons(Button):
    time_mins = 0
    def __init__(self, label, style, emoji, msg, time_m):
        super().__init__(label=label, style=style, emoji=emoji)
        self.msg = msg
        self.time_m = time_m
    async def callback(self, interaction):
        await interaction.response.edit_message(content=self.msg, view=None)
        time_m = self.time_m
        if time_m[-1] == 'h':
            time_mins = int(time_m[:-1])*60
        elif time_m[-1] == 'd':
            time_mins = int(time_m[:-1]) * 60 * 24
        elif time_m == 0:
            pass
        print(time_mins)

@bot.slash_command(name='mute', description='Mute user')
async def mute(ctx, user: nextcord.User, reason: str):
    mute_24h = Buttons(label='Mute for 24h', style=nextcord.ButtonStyle.red, emoji='🔇', msg=f'Successfully muted user {user.mention} for **24h** with reason: **{reason}**', time_m = '24h')
    mute_3d = Buttons(label='Mute for 3d', style=nextcord.ButtonStyle.red, emoji='🔇', msg=f'Successfully muted user {user.mention} for **3d** with reason: **{reason}**', time_m = '3d')
    mute_5d = Buttons(label='Mute for 5d', style=nextcord.ButtonStyle.red, emoji='🔇', msg=f'Successfully muted user {user.mention} for **5d** with reason: **{reason}**', time_m = '5d')
    mute_10d = Buttons(label='Mute for 10d', style=nextcord.ButtonStyle.red, emoji='🔇', msg=f'Successfully muted user {user.mention} for **10d** with reason: **{reason}**', time_m = '10d')
    cancel = Buttons(label='Cancel', style=nextcord.ButtonStyle.red, emoji='❌', msg=f'Successfully cancelled', time_m=0)

    view = view_items([mute_24h, mute_3d, mute_5d, mute_10d, cancel], timeout=30)

    await ctx.send(f'The user {user.mention} was being muted with reason **{reason}** for what time?', view=view)



from config import TOKEN
bot.run(TOKEN)