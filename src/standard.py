import discord, os
from src.botprints import commands_list, welcome

async def standard(message, args):
  if (args[0] == "hello" and len(args) == 1):
      await message.channel.send("Hello World!")
  elif (args[0] == "help"):
    await message.channel.send(welcome.format(os.environ['BOTPREFIX'], os.environ['BOTPREFIX']))
  elif (args[0] == "commands"):
    if (len(args) == 1):
      # Send the default commands list
      commands = "**The following is a comprehensive list of commands supported by ForsakenBot.**\n"
      for command in commands_list:
        commands += "`{}{}` - {}".format(os.environ['BOTPREFIX'], command['command'], command['function'])
        if command['type'] == "admin":
          commands += " **Admin Privileges Required!**\n"
        else:
          commands += "\n"
      await message.channel.send(commands)
    elif (len(args) == 2):
      print ("Command help unimplemented.")
      await message.channel.send("Multihelp not implemented.")
    else:
      await message.channel.send("Too many arguments for help command.")