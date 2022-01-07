import discord
from discord.ext import commands
from datetime import datetime

token = "Токен бота"
bot = commands.Bot(command_prefix='*')
now = datetime.now().time()



@bot.event
async def on_message(msg):
  #if msg.channel.id != айди логируемого канала:
  #     return
    log = open('logging.txt', 'a')
    log.write(f"Канал: '{msg.channel.name}', Отправитель: '{msg.author.name}', Время: '{now}', Сообщение: '{msg.content}'\n")
    log.close()  
    await bot.process_commands(msg)



bot.run(token)
