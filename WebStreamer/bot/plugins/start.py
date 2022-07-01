

from pyrogram import filters, emoji
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command(['start', 'help']))
async def start(_, m: Message):
    await m.reply(f'Hey..🖐✌ {m.from_user.mention(style="md")}, Send me any Movie📽,Web Series or any File to Get an Instant Streaming/Download Link🔥',
                
                  )
