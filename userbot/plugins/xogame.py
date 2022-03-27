import html
import os
import urllib
from urllib.parse import quote as urlencode
import re
import random
from userbot import bot
from userbot.utils import admin_cmd
import aiohttp
import requests
from telethon.errors.rpcerrorlist import YouBlockedUserError

from ..helpers.functions import age_verification
from . import catub, edit_delete, edit_or_reply, eod, eor, reply_id

session = aiohttp.ClientSession()
plugin_category = "fun"


IF_EMOJI = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+"
)


def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(IF_EMOJI, "", inputString)
@catub.cat_cmd(
    pattern="xo ([\s\S]*)",
    command=("xo", plugin_category),
    info={
        "header": "To play xo game.",
        "examples": "{tr}xo",
    },
)
async def nope(doit):
    ok = doit.pattern_match.group(1)
    if not ok:
        if doit.is_reply:
            (await doit.get_reply_message()).message

            return
    xoxoxo = await bot.inline_query("xobot", f"{(deEmojify(ok))}")
    await xoxoxo[0].click(
        doit.chat_id,
        reply_to=doit.reply_to_msg_id,
        silent=True if doit.is_reply else False,
        hide_via=True,
    )
    await doit.delete()
