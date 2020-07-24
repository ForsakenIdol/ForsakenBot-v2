import discord, os
from datetime import datetime

async def admin(message, args):
  if (message.author.permissions_in(message.channel).administrator):
    # Enumerate through all admin commands
    if (args[0] == "prefix"):
      if (len(args) == 2 and 0 < len(args[1]) <= 2):
        os.environ['BOTPREFIX'] = args[1]
        await message.channel.send("ForsakenBot's prefix has been updated to `{}`.".format(os.environ['BOTPREFIX']))
      else:
        await message.channel.send("Incorrect usage of `{}prefix` command. Expected `{}prefix <new>` where `<new>` represents the new bot prefix."
        .format(os.environ['BOTPREFIX'], os.environ['BOTPREFIX']))
    elif (args[0] == "uptime" and len(args) == 1):
      if (message.author.permissions_in(message.channel).administrator):
        # Add embed functionality if (len(args) == 2 and args[1] == "embed")
        uptime = datetime.now() - datetime.strptime(os.environ['BOTJOINTIME'], "%Y-%m-%d %H:%M:%S.%f")
        hours, rem = divmod(int(uptime.total_seconds()), 3600)
        mins, secs = divmod(rem, 60)
        await message.channel.send("ForsakenBot has been online for {}:{}:{} since the last restart."
                                    .format(hours if hours > 10 else "0" + str(hours), mins if mins > 10 else "0" + str(mins), secs if secs > 10 else "0" + str(secs)))
  else:
    await message.channel.send("You don't have permission to use this command!")