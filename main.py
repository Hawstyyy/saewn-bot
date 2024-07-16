import discord
from dc_token import token

class MyClient(discord.Client):
  async def on_ready(self):
    print(f'Logado como {self.user}!')

  async def on_message(self, message):
    if message.content.startswith('saewon'):
      await message.channel.send('gaming')
      await channel.send(file=discord.File(r'./awaken.mp4'))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
channel = client.get_channel(855508166573948958)
client.run(token)
