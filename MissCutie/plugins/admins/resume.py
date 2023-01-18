#
# Copyright (C) 2021-2022 by MissCutie@Github, < https://github.com/MissCutie >.
#
# This file is part of < https://github.com/MissCutie/MissCutie > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/MissCutie/MissCutie/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from MissCutie import app
from MissCutie.core.call import MissCutie
from MissCutie.utils.database import is_music_playing, music_on
from MissCutie.utils.decorators import AdminRightsCheck

# Commands
RESUME_COMMAND = get_command("RESUME_COMMAND")


@app.on_message(
    filters.command(RESUME_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if len(message.command) != 1:
        return await message.reply_text(_["general_2"])
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    await MissCutie.resume_stream(chat_id)
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention)
    )
