# Telegram Support Service Bot #
## Background ##
This is my first Python program that was written by me while learning to program in Python.

## How To Run This Bot ##
This bot is written with Python 3.11.0. I hope this program will work correctly on any version of Python 3.

1. Create your telegram bot using [Botfather](https://t.me/BotFather) and copy your new telegram bot token.
2. Download my file and put your new telegram bot token here:

        API_TOKEN = ''  # put your telegram bot token here

3. Instal Aiorgam on your computer. Here is the link to an origimnal [Installation Guide](https://docs.aiogram.dev/en/latest/install.html).

        pip install aiogram

5. Run bot wia your terminal:

        python path/index.py
        or
        python3 path/index.py
        
4. Create a new group telegram chat. It will be your support team chat. And add your telegram bot in this chat wia Add Member button.
5. Run the bot in your chat by typing this message: `/start`. And you will get the bot hello message.    
6. Get you chat id by typing this message: `/chatid`. And bot will send you chat id. It sould start from '-'.
7. Put your chat id into bot`s code:

        admin_chat_id = ''  # put your support team chat id here
        
8. Send your telegram bot link to any telegram user. He should start bot by typing `/start` message.

## The Main Function ##

The main task of this bot is to organize the messaging of the user on the one hand and the whole group of operators on the other hand. When a user sends a message to the bot, that message is forwarded to the group. And all group members can see this message. Any member of the group can reply to this message and this message will be sent to the user as a bot response. For the user it will look just like a messaging with a bot, while on the other side there may be a whole team that responds to his messages.

You can even simulate the work of artificial intelligence. If the user does not know that the bot is forwarding messages to the group and there are real people responding to him, he may think that he is communicating with the program.

The user can also send emojis and stickers. And chat admins can send emojis and stickers back to him.

## Limitations ##

This bot cannot work with other data types:
- audio messages
- audio files
- video messages
- video files
- photos
- other files
- geolocation
