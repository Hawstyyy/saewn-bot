import discord
import random
from dc_token import token
x = 1

lista = [':face_with_raised_eyebrow: https://imgur.com/a/n6m4ZMf', 'Me deixa irmão', 'Vai se fude', 'gaming']
class MyClient(discord.Client):
  async def on_ready(self):
    print(f'Logado como {self.user}!')
    if x == 0:
      await client.get_channel(660139338025140248).send('<@787798697140289597>', file=discord.File(r'./awaken.mp4'))

  async def on_message(self, message):
    if message.content.startswith('saewn'):
      escolha = random.choice(lista)
      await message.channel.send(escolha)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
channel = client.get_channel(660139338025140248)
client.run(token)
