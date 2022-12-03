# Telegram Support Service Bot #
## Background ##
This is my first Python program that was written by me while learning to program in Python.

## How To Run This Bot ##
This bot is written with Python 3.11.0. I hope this program will work correctly on any version of Python 3.

1. Create your telegram bot using [Botfather](https://t.me/BotFather) and copy your new telegram bot token.
2. Download my file and put your new telegram bot token here:

        API_TOKEN = ''  # Put your telegram bot token here

3. Instal Aiorgam on your computer. Here is the link to an origimnal [Installation Guide](https://docs.aiogram.dev/en/latest/install.html).

        pip install aiogram

5. Run bot wia your terminal:

        python path/index.py
        or
        python3 path/index.py
        
4. Create a new group telegram chat. It will be your support team chat. And add your telegram bot in this chat wia Add Member button.
5. Run the bot in your chat by typing this message: `/start`. And you will get the bot hello message.

![](https://drive.google.com/uc?export=download&id=1UTzM_98dCq4ckqxbuURSZqiHpZrITvAw)

6. Get you chat id by typing this message: `/chatid`. And bot will send you chat id. It sould start from '-'.

![](https://drive.google.com/uc?export=download&id=1nRexDfeDYLCBmGUg4tRHw2kmqZrFjJfb)

8. Put your chat id into bot`s code:

        admin_chat_id = ''  # Put your support team chat id here
        
8. Send your telegram bot link to any telegram user. He should start bot by typing `/start` message.

## The Main Function ##

The main function of this bot is to organize messaging of users on the one hand and the whole group of operators on the other hand. When a user sends a message to the bot, that message is forwarded to the support team group. And all group members can see this message. Any member of the group can reply to this message and this message will be sent to the user as a bot response. For the user it will look just like a messaging with a bot, while on the other end there may be the whole team that responds to his messages.

User sends his message to the bot.

![](https://drive.google.com/uc?export=download&id=1TDcL4T4g9CyPntxKYeaFIeLNMkyMtqSN)

The bot forwards a user's message to the support team chat.

![](https://drive.google.com/uc?export=download&id=1dJ64YniIZHSOBUk4l9lLXvSR5Sfx5BSw)

Support team member writes a response.

![](https://drive.google.com/uc?export=download&id=1u2ay8NWA9Ztg4wzpKKirtXO3nM1WYaHt)

The bot forwards message to the user.

![](https://drive.google.com/uc?export=download&id=1dJ3R-8ukCBdk6qM7o5zKFKha7DgKeO7z)

You can even simulate the work of artificial intelligence. If the user does not know that the bot is forwarding messages to the group and there are real people responding to him, he may think that he is communicating with the program.

The user can also send emojis and stickers. And chat admins can send emojis and stickers back to him.

The user sends sticker.

![](https://drive.google.com/uc?export=download&id=15r5mRvXModNw8adbrHu5RV5jKtkJx34n)

The bot forwards a user's sticker to the support team chat.

![](https://drive.google.com/uc?export=download&id=1AOn95h6ogF__cqrDrnQ91TcuYoLhin5L)

Support Team sends a sticher in responce.

![](https://drive.google.com/uc?export=download&id=1H1NJ_Z4Cd46HiQk0o7q3E22D2tkK8uon)


## Limitations ##

This bot cannot work with other data types:
- Audio messages
- Audio files
- Video messages
- Video files
- Photos
- Other files
- Geolocation
