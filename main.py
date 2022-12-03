import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = ''  # put your telegram bot token here
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

admin_chat_id = ''  # Put your support team chat id here


# Hello Message
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hello!")  # Put your hello message here


# This block allows you to find out the chat id for you team group chat
@dp.message_handler(commands='chatid')
async def send_welcome(message: types.Message):
    await message.reply("Your chat id: " + str(message.chat.id))


# This block is responsible for sending messages from the user to the team chat and back
@dp.message_handler()
async def forward_message(message: types.Message):  # If the support team member sends a message
    if str(message.chat.id) == str(admin_chat_id):
        await bot.send_message(message.reply_to_message.text.split(' ')[-1], message.text)
    else:  # If the user sends a message
        message_from_user_text = f'<b>{str(message.from_user.first_name)} {str(message.from_user.last_name)}</b> ({str(message.from_user.username)})\nMessage id – {str(message.chat.id)}'
        await bot.send_message(admin_chat_id, str(message.text) + '\n' + message_from_user_text, parse_mode="html")


# This block is responsible for sending stickers from the user to the team chat and back
@dp.message_handler(content_types=['sticker'])
async def forward_sticker(message: types.Message):  # If the support team member sends a message
    if str(message.chat.id) == str(admin_chat_id):
        await bot.send_sticker(message.reply_to_message.text.split(' ')[-1], message.sticker.file_id)
    else: # If the user sends a message
        await bot.send_sticker(admin_chat_id, message.sticker.file_id)
        message_from_user_text = f'<b>{str(message.from_user.first_name)} {str(message.from_user.last_name)}</b> ({str(message.from_user.username)})\nMessage id – {str(message.chat.id)}'
        await bot.send_message(admin_chat_id, 'Sticker from \n' + message_from_user_text, parse_mode="html")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
