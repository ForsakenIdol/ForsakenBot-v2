import discord, os
from datetime import datetime
from src.main import handleMessage
from dotenv import load_dotenv

client = discord.Client()

@client.event
async def on_connect():
  now = str(datetime.now())
  os.environ['BOTCONNECTIME'] = now
  print("[{}] ForsakenBot has connected.".format(now))

@client.event
async def on_ready():
  now = str(datetime.now())
  os.environ['BOTJOINTIME'] = now
  formats = [now, client.user]
  print("[{}] ForsakenBot has logged in as {}.".format(*formats))

@client.event
async def on_disconnect():
  now = str(datetime.now())
  os.environ['BOTDISCONNECTTIME'] = now
  print("[{}] ForsakenBot has been disconnected.".format(now))

@client.event
async def on_message(message):
  # Prefix could potentially be an external specification
  if (message.author != client.user):
    await handleMessage(message)

# Group function types into their own files under "src/".

load_dotenv("config.env")
client.run(os.environ['BOTTOKEN'])