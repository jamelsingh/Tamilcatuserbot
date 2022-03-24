from telethon import events
from asyncio import sleep
import html
import os
import urllib
from urllib.parse import quote as urlencode

import aiohttp
import requests
from . import catub, edit_delete, edit_or_reply, eod, eor, reply_id

plugin_category = "extra"


@catub.cat_cmd(
    pattern="wspr(?: |$)(.*)",
    command=("wspr", plugin_category),
    info={
        "header": "You know what it is,!",
        "usage": "{tr}wspr",
        "examples": "{tr}wspr message @username",
    },
)

async def wspr(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    wwwspr = event.pattern_match.group(1)
    botusername = "@whisperBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr)
    await tap[0].click(event.chat_id)
    await event.delete()
