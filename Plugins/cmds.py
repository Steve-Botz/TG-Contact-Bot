import os
import sys
import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import Message
from config import ADMIN

@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(client: Client, message: Message):
    user_id = message.from_user.id
    mention_user = message.from_user.mention
    start_text = f"""<blockquote><b><i>Hii, {mention_user} ✌

☆ HOW ARE YOU.. 
☆ THIS IS A CONTACT BOT.. 
☆ JUST SEND YOUR MESSAGE HERE.. 
☆ OWNER WILL REPLY SOON.. 
☆ YOU CAN CHAT WITH OWNER USING THIS BOT..
</i></b></blockquote>"""
    await client.send_photo(
        chat_id=message.chat.id,
        photo="https://telegra.ph/file/d46c99c49cb7e19d5df0c-2b2c7af88c6e67e838.jpg",
        caption=start_text,
        parse_mode=enums.ParseMode.HTML
    )

@Client.on_message(filters.command("restart") & filters.private & filters.user(ADMIN))
async def restart_bot(client: Client, message: Message):
    steve = await message.reply_text("**🔄 Restarting bot...**")
    await asyncio.sleep(3)
    await steve.edit("**✅ Bot restarted successfully**")
    os.execl(sys.executable, sys.executable, *sys.argv)
