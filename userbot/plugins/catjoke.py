""" Userbot module for having some fun with people. """
import asyncio
import random

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from userbot import catub

from . import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SurCat"
SURID = bot.uid

plugin_category = "fun"


JOKE_STRINGS = [
   "Which is the only dancing animal? \n Yosinga! \n Theriyalaya? \n AADU..!",
   "500 rupees note la Ghandhi yen sirichitte irukkar ? A: Yenna Alutha nanainjudume !!!",
   "Bus mela nee earinaalum sari, un mela bus earinaalum sari, ticket vaanga poradhu nee dhan!",
   "Tea master evvalavu dhan lighta tea pottalum,adhula irundhu velicham adikkadhu.",
   "Ennadhan naaykku naalu kaal irundhalum, adhala kaal mela kaal pottu ukkara mudiyuma?",
   "Yaanai mela naama ukkandhu pona  Safari. , andha yaanai namma mela ukkandhu 'Oppari'.",
   "Kadal mela kappal pona Jolly, Kappal mela kadal pona Gaali.",
   "Oruthan evalavu dhan gunda irundhalum,avana thuppakki kulla poda mudiyaau.",
   "America naattu janadhipadhiyavae irundhalum, barber'ukku munnadi thala guninjhu dhan ukkaranum.",
   "Kaal evvaluvudhan vegama odunaalum, kaikkudhan prize kadaikkum",
   "Sirpi Kalla Uliyaala Adicha adhu “Kalai” Sirpiya Uliyaala Adicha adhu Kolai",
   "Mandaiya Potta Die \n Mandaila Potta Dye",
   "Bun mela thanni oothina enna aagum? \n Panneer agum!",
   "Sigathai paarthu payapadhada miriguam edhu? \n Innoru Singam!",
]

@catub.cat_cmd(pattern="joke$", command=("joke", plugin_category))
async def joke(e):
    txt = random.choice(JOKE_STRINGS)
    await edit_or_reply(e, txt)
