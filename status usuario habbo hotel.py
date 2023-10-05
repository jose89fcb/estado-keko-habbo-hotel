import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
import requests
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash import SlashCommand, SlashContext

bot = commands.Bot(command_prefix='!')
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print(f'Conectado como {bot.user.name}')

@slash.slash(
    name="estado", description="Keko habbo Hotel",
    options=[
        create_option(
            name="keko",
            description="Escribe el keko",
            option_type=3,
            required=True
        ),
        create_option(
            name="hotel",
            description="Elige él hotel",
            option_type=3,
            required=True,
            choices=[
                create_choice(
                    name="ES - Hotel España",
                    value="es"
                ),
                create_choice(
                    name="BR - Hotel Brasil",
                    value="com.br"
                ),
                create_choice(
                    name="COM - Hotel Estados unidos",
                    value="com"
                ),
                create_choice(
                    name="DE - Hotel Aleman",
                    value="de"
                ),
                create_choice(
                    name="FR - Hotel Frances",
                    value="fr"
                ),
                create_choice(
                    name="FI - Hotel Finalandia",
                    value="fi"
                ),
                create_choice(
                    name="IT - Hotel Italiano",
                    value="it"
                ),
                create_choice(
                    name="TR - Hotel Turquia",
                    value="com.tr"
                ),
                create_choice(
                    name="NL - Hotel Holandés",
                    value="nl"
                )
            ]
        )
    ])
async def _estado(ctx: SlashContext, keko: str, hotel: str):
    # Hacer una solicitud a la API de Habbo
    data = requests.get(f"https://www.habbo.{hotel}/api/public/users?name={keko}")

    try:
        estado = data.json().get("online", False)

        es = {
            False: "desconectad@",
            True: "online"
        }

        # Convertir el valor booleano en un nombre representativo del estado
        estado = es.get(estado, "Desconocido")

    except TypeError:
        estado = "Desconocido"

    embed = discord.Embed()

    file_path = f"estados/{estado}.gif"
    file = discord.File(file_path, filename="imagen.gif")
    embed.set_author(name=f"{estado}", icon_url="attachment://imagen.gif")
    embed.set_thumbnail(
        url=f"https://www.habbo.es/habbo-imaging/avatarimage?direction=4&head_direction=3&action=wav&gesture=sml&size=m&user={keko}")
    embed.set_footer(text=f"habbo[{hotel.upper()}]", icon_url="https://i.imgur.com/6ePWlHz.png")
    await ctx.send(file=file, embed=embed)


  

   

bot.run('TU TOKEN AQUI')
