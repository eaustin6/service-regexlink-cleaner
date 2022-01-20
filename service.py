import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, User, Message

Client = Client(
    "Song Downloader Bot",
    bot_token = os.environ["5176057450:AAHQYEJyAIsx10jnncqCS1jZldEl8_llHCU"],
    api_id = int(os.environ["8148690"]),
    api_hash = os.environ["0c0124510151aa918fc562b5baccc1ef"]
)

START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('SOURCE CODE', url="https://github.com/SpamShield/PyroGramBot")
        ]]
    ) 

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, message):
    await message.reply_sticker("CAACAgUAAxkBAAEBcr1hsLH3Nu0-qQpwwWQ7FkF58xnwSgACpAMAAjieoFU-Q-udLfwBUx4E")
    await message.reply_text(
        f""" Hai {message.from_user.mention} am Service Message, command and link deleter bot.""", 
        disable_web_page_preview=True,
        reply_markup=START_BUTTON
    )
@Client.on_message(filters.regex("http") | filters.regex("t.me") | filters.regex("/" ) | filters.service)
async def delete(bot,message):
 await message.delete()

Client.run()
