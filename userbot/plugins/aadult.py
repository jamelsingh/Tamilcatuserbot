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
    if x == 2:

        await event.edit(
            "உன் எழதுகோலால் கவிதை எழுதஆசைதான் எனக்கும் ...என்ன செய்வது உன் எழதுகோலை காலிடுக்கில் பதுக்கி வைத்துள்ளாயே கள்ளா...🍑"
        )

    if x == 3:

        await event.edit(
            "அழகிய மாங்கனிகள் அணைத்து அழுத்தி..விரைத்த காம்பின் வீணை மீட்டுகிறேன் என்னவளே🥰"
        )

    if x == 4:

        await event.edit(
            "ஆடிய கட்டிலை உடைத்தான். ஆனால் அவளின் மனதை வென்று விட்டான்😂"
        )
   
    if x == 5:
 
       await event.edit(
           "என்னவனின் இரு கரங்களும் என் இடுப்பை அணைக்க கண்மூடி அவன் தழுவலை அனுபவிக்கும் அந்நேரம். நாசிதனில் அவனின் வாசம் - மதுவுக்கும் இல்லை அந்த போதை அவன் அணைப்பே சுகம்🥰"
        )

    if x == 6:
     
       await event.edit(
           "இதழ் விரிந்து, இடை விரித்து கொடையாய் தருகிறாய் காமக் குழிதனை..தொப்புள் குழியை சொன்னேன்😂🥰"
       )






