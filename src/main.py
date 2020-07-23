import discord, os
from datetime import datetime
from src.botstrings import welcome

async def handleMessage(message):
  if (message.content.startswith('-')):
    args = message.content[1:].lower().split(' ')
    if (args[0] == "hello" and len(args) == 1):
      await message.channel.send("Hello World!")
    elif (args[0] == "uptime" and len(args) == 1):
      # Add embed functionality if (len(args) == 2 and args[1] == "embed")
      uptime = datetime.now() - datetime.strptime(os.environ['BOTJOINTIME'], "%Y-%m-%d %H:%M:%S.%f")
      hours, rem = divmod(int(uptime.total_seconds()), 3600)
      mins, secs = divmod(rem, 60)
      await message.channel.send("ForsakenBot has been online for {}:{}:{} since the last restart."
                                  .format(hours if hours > 10 else "0" + str(hours), mins if mins > 10 else "0" + str(mins), secs if secs > 10 else "0" + str(secs)))
    elif (args[0] == "help"):
      if (len(args) == 1):
        # Send the default help message
        await message.channel.send(welcome)
      elif (len(args) == 2):
        print ("Command help unimplemented.")
        await message.channel.send("Multihelp not implemented.")
      else:
        await message.channel.send("Too many arguments for help command.")
    else:
      await message.channel.send("Command not recognized.")