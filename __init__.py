from datetime import datetime, timedelta
import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import random
from nextcord.ui import button

daily_claims={}
coins = 890000
bank = 0
banksize = 890000
skinfragments = 0
fishtokens = 10
gems = 100

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", help_command=None, intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    activity = nextcord.Streaming(
        name="[/] Shick Memer | Twitch Stream",
        url="https://twitch.tv/shickmemer"
    )
    await bot.change_presence(activity=activity)


@bot.slash_command(name="coinflip", description="Flip a Coin! Ofcourse this does not have any bet.", guild_ids=[1471733353060499486])
async def coinflip(interaction: Interaction):
    num = random.randint(1, 2)

    result = "Heads" if num == 1 else "Tails"

    embed = nextcord.Embed(
        title="<:coin:1471335781300834450> Coin Flip",
        description=f"**{interaction.user.mention} flipped a coin and got **{result}**!",
        color=0x00ff00
    )

    await interaction.response.send_message(embed=embed)


@bot.slash_command(name="balance", description="Check their Bank Amount, Coins, and more!", guild_ids=[1471733353060499486])
async def balance(interaction: Interaction):
    global coins
    global bank
    global banksize
    global skinfragments
    global fishtokens
    global gems
    balanceembed = nextcord.Embed(
        title=" ",
        description=f"### {interaction.user.name}'s Balance\n<:coin:1471335781300834450> {coins}\n<:bank:1471459170774683833> {bank} / {banksize}\n<:skinfragments:1471462149204344903> {skinfragments}\n<:fishtokens:1471466426983252154> {fishtokens}\n<a:gemsanimated:1471478598622908416> {gems}"
    )
    await interaction.response.send_message(embed=balanceembed)
@bot.slash_command(name="invite", description="Get an invite for the bot or to the support server. Also some extra common links to use!", guild_ids=[1471733353060499486])
async def invite(interaction: Interaction):
    inviteembed = nextcord.Embed(
        title=""
    )
    inviteembed.add_field(name="Add Shick Memer", value="[Here](https://discord.com/oauth2/authorize?client_id=1471138459522433267&permissions=4012085718015040&integration_type=0&scope=bot+applications.commands)")
    inviteembed.add_field(name="Shick Memer Support", value="[Here](https://discord.gg/D9r8WkJrBG)")
    await interaction.response.send_message(embed=inviteembed)
@bot.slash_command(name="daily", description="Get Daily Rewards! And get some Streaks!", guild_ids=[1471733353060499486])
async def daily(interaction: Interaction):
    global coins
    user_id = interaction.user.id
    now = datetime.now()

    cooldown = timedelta(hours=24)

    if user_id in daily_claims:
        last_claim = daily_claims[user_id]
        time_left = cooldown - (now - last_claim)

        if time_left.total_seconds() > 0:
            hours, remainder = divmod(int(time_left.total_seconds()), 3600)
            minutes, seconds = divmod(remainder, 60)

            embed = nextcord.Embed(
                title="⏳ Daily Cooldown",
                description=f"You already claimed your daily!\nCome back in **{hours}h {minutes}m {seconds}s**",
                color=0xff0000
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
    coins=112960+coins
    daily_claims[user_id] = now
    dembed=nextcord.Embed(
        title=" ",
        description="<:coin:1471335781300834450> 112,960 was given to you"
    )
    await interaction.response.send_message(embed=dembed)
bot.run("YOUR_DISCORD_BOT_TOKEN")
