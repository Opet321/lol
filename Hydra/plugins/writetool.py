from pyrogram import filters
from pyrogram.types import *
import requests
import Hydra.config


@Cleint.on_message(filters.user(config.OWNER_ID) & filters.command("write",prefixes=config.))
async def handwriting(_, message):
    if len(message.command) < 2:
        return await message.reply_text("» Give some text to write...")
    m = await message.reply_text("» I writing please wait...")
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    API = "https://apis.xditya.me/write?text=" + name
    url = requests.get(API).url
    await m.edit("» Uploading...")
    await m.delete()
    me = await Cleint.get_me()
    await message.reply_photo(url, caption=f"""**🥀 Made by {me.mention}**""")
