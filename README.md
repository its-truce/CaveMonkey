# Cave Monkey 🎈
Cave Monkey is a discord bot made to help BTD6 players: it provides a lot of useful info that can be utilized in your gameplay, while also being easily understandable and noob friendly. It's written in [`Python`](https://www.python.org/)   using the [`discord.py`](https://github.com/Rapptz/discord.py) library. Any incorrect information should be reported to [me](https://discord.com/users/626333424965386240) on discord.

# Installing & Running 🤖
I would prefer it if you don't run an instance of my bot. It can be invited using this [link](https://discord.com/api/oauth2/authorize?client_id=1069569059257077840&permissions=517543938112&scope=bot). If you still want to run an instance of my bot, however, here's how you can do it:
* Make a bot from the discord developer portal. Here's a [tutorial](https://discordpy.readthedocs.io/en/latest/discord.html) on setting up your bot.
* Make sure you have the latest stable version of [`Python`](https://www.python.org/) installed.
* Make a venv. In your root folder, run this command:
  ```py
  # Making a venv:
  python3 -m venv venv
  ```
* Installing the requirements. This is simply:
  ```py
  # Installing dependencies:
  pip install -U -r requirements.txt
  ```
* Enter your bot's token in the [`bot.py`](https://github.com/its-truce/CaveMonkey/blob/main/main/bot.py) file. The variable is on line 8.
