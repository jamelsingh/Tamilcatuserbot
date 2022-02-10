import asyncio
import random
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from userbot import catub
from . import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "tacat"
SURID = bot.uid

plugin_category = "fun"

@catub.cat_cmd(pattern="adpoyem$", command=("adpoem", plugin_category))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "Adult Poem 🥰...")
    await asyncio.sleep(2)
    x = random.randrange(1, 33)
    if x == 1:

        await event.edit(
            "பெண் என்பவள் ஒவ்வொரு பக்கமும் ரசித்துப் படிக்கும் சிறந்த புத்தகம்.!💔🚶🚶"
        )
    if x == 1:
        await event.edit(
            "உன் எழதுகோலால் கவிதை எழுதஆசைதான் எனக்கும் ...என்ன செய்வது உன் எழதுகோலை காலிடுக்கில் பதுக்கி வைத்துள்ளாயே கள்ளா...🍑"
       )
