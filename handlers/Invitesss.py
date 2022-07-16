from pyrogram import Client, filters 
from pyrogram.types import Message
from config import SUDO_USERS
import asyncio

@Client.on_message(filters.command(["inviteall", "kidnapall"], [".", "!", "/"]) & filters.user(SUDO_USERS))
async def inviteall(client: Client, message: Message):
    zaid = await message.reply_text("⚡ Gime Title also\n ex: /inviteall @testing")
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await client.get_chat(queryy)
    tgchat = message.chat
    await zaid.edit_text(f"inviting users from {chat.username}")
    async for member in client.iter_chat_members(chat.id):
        user= member.user
        zxb= ["online", "offline" , "recently", "within_week"]
        if user.status in zxb:
           try:
            await client.add_chat_members(tgchat.id, user.id)
           except Exception as e:
            mg= await client.send_message("me", f"error-   {e}")
            await asyncio.sleep(0.3)
            await mg.delete()
