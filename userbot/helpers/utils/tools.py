import json
import os
from json.decoder import JSONDecodeError
from typing import Optional, Tuple, Union

from moviepy.editor import VideoFileClip
from PIL import Image

from ...core.logger import logging
from ...core.managers import edit_or_reply
from ..tools import media_type
from .utils import runcmd

LOGS = logging.getLogger(__name__)


async def media_to_pic(event, reply, noedits=False):  # sourcery no-metrics
    mediatype = media_type(reply)
    if mediatype not in [
        "Photo",
        "Round Video",
        "Gif",
        "Sticker",
        "Video",
        "Voice",
        "Audio",
        "Document",
    ]:
        return event, None
    if not noedits:
        catevent = await edit_or_reply(
            event, "`Transfiguration Time! Converting to ....`"
        )

    else:
        catevent = event
    catmedia = None
    catfile = os.path.join("./temp/", "meme.png")
    if os.path.exists(catfile):
        os.remove(catfile)
    if mediatype == "Photo":
        catmedia = await reply.download_media(file="./temp")
        im = Image.open(catmedia)
        im.save(catfile)
    elif mediatype in ["Audio", "Voice"]:
        await event.client.download_media(reply, catfile, thumb=-1)
    elif mediatype == "Sticker":
        catmedia = await reply.download_media(file="./temp")
        if catmedia.endswith(".tgs"):
            catcmd = f"lottie_convert.py --frame 0 -if lottie -of png '{catmedia}' '{catfile}'"
            stdout, stderr = (await runcmd(catcmd))[:2]
            if stderr:
                LOGS.info(stdout + stderr)
        elif catmedia.endswith(".webp"):
            im = Image.open(catmedia)
            im.save(catfile)
    elif mediatype in ["Round Video", "Video", "Gif"]:
        await event.client.download_media(reply, catfile, thumb=-1)
        if not os.path.exists(catfile):
            catmedia = await reply.download_media(file="./temp")
            clip = VideoFileClip(media)
            try:
                clip = clip.save_frame(catfile, 0.1)
            except Exception:
                clip = clip.save_frame(catfile, 0)
    elif mediatype == "Document":
        mimetype = reply.document.mime_type
        mtype = mimetype.split("/")
        if mtype[0].lower() == "image":
            catmedia = await reply.download_media(file="./temp")
            im = Image.open(catmedia)
            im.save(catfile)
    if catmedia and os.path.lexists(catmedia):
        os.remove(catmedia)
    if os.path.lexists(catfile):
        return catevent, catfile, mediatype
    return catevent, None


async def take_screen_shot(
    video_file: str, duration: int, path: str = ""
) -> Optional[str]:
    thumb_image_path = path or os.path.join(
        "./temp/", f"{os.path.basename(video_file)}.jpg"
    )
    command = f"ffmpeg -ss {duration} -i '{video_file}' -vframes 1 '{thumb_image_path}'"
    err = (await runcmd(command))[1]
    if err:
        LOGS.error(err)
    return thumb_image_path if os.path.exists(thumb_image_path) else None


def get_c_m_message(message_link: str) -> Tuple[Union[str, int], int]:
    p_m_link = message_link.split("/")
    chat_id, message_id = None, None
    if len(p_m_link) == 6:
        # private link
        if p_m_link[3] == "c":
            # for supergroups / channels
            chat_id, message_id = int("-100" + p_m_link[4]), int(p_m_link[5])
        elif p_m_link[4] == "UniBorg":
            # for basic groups / private chats
            chat_id, message_id = int(p_m_link[4]), int(p_m_link[5])
    elif len(p_m_link) == 5:
        # public link
        chat_id, message_id = str("@" + p_m_link[3]), int(p_m_link[4])
    return chat_id, message_id


def json_parser(data, indent=None):
    parsed = {}
    try:
        if isinstance(data, str):
            parsed = json.loads(str(data))
            if indent:
                parsed = json.dumps(json.loads(str(data)), indent=indent)
        elif isinstance(data, dict):
            parsed = data
            if indent:
                parsed = json.dumps(data, indent=indent)
    except JSONDecodeError:
        parsed = eval(data)
    return parsed
