#
# Copyright (C) 2021-2022 by MissCutie@Github, < https://github.com/MissCutie >.
#
# This file is part of < https://github.com/MissCutie/MissCutie > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/MissCutie/MissCutie/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message

from config import BANNED_USERS
from strings import get_command
from MissCutie import app
from MissCutie.utils.database import (get_playmode, get_playtype,
                                       is_nonadmin_chat)
from MissCutie.utils.decorators import language
from MissCutie.utils.inline.settings import playmode_users_markup

### Commands
PLAYMODE_COMMAND = get_command("PLAYMODE_COMMAND")


@app.on_message(
    filters.command(PLAYMODE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def playmode_(client, message: Message, _):
    playmode = await get_playmode(message.chat.id)
    Direct = True if playmode == "Direct" else None
    is_non_admin = await is_nonadmin_chat(message.chat.id)
    Group = None if is_non_admin else True
    playty = await get_playtype(message.chat.id)
    Playtype = None if playty == "Everyone" else True
    buttons = playmode_users_markup(_, Direct, Group, Playtype)
    response = await message.reply_text(
        _["playmode_1"].format(message.chat.title),
        reply_markup=InlineKeyboardMarkup(buttons),
    )
