welcome = """**Welcome to ForsakenBot v2!** My command prefix is `{}`.
This is a complete rewrite of a previous bot I made at the start of 2020.
To see the full commands list, type `{}commands`."""

types = ["admin", "auth", "standard"]

# We don't store the bot's prefix as this is customizable.
commands_list = [
  {
    "command": "commands",
    "function": "Displays this list of commands.",
    "type": types[2]
  },
  {
    "command": "hello",
    "function": "Prints \"Hello World!\" to the channel.",
    "type": types[2]
  },
  {
    "command": "help",
    "function": "Displays the welcome message and commands.",
    "type": types[2]
  },
  {
    "command": "prefix",
    "function": "Changes the bot's prefix.",
    "type": types[0]
  },
  {
    "command": "uptime",
    "function": "Prints the bot's uptime, i.e. how long the bot has been active since the last restart.",
    "type": types[0]
  }
]