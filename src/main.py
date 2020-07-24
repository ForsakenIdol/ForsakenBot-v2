import discord, os
from src.botprints import welcome, commands_list, types
from src.admin import admin
from src.standard import standard

async def handleMessage(message):
  if (message.content.startswith(os.environ['BOTPREFIX'])):
    args = message.content[len(os.environ['BOTPREFIX']):].lower().split(' ')
    command_found = False
    for command in commands_list:
      if (args[0] == command["command"]):
        # Command found, we now shift execution to the corresponding function
        if (command["type"] == types[0]):
          command_found = True
          await admin(message, args)
        elif (command["type"] == types[2]):
          command_found = True
          await standard(message, args)
    if (not command_found):
      await message.channel.send("Command not recognized.")