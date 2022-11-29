#
# Copyright (C) 2021-2022 by MissCutie@Github, < https://github.com/MissCutie >.
#
# This file is part of < https://github.com/MissCutie/MissCutie > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/MissCutie/MissCutie/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import InlineKeyboardButton


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="📚 All Commands", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text="Dev", url="https://t.me/Xd_Nitric"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="Updates", url="https://t.me/StormUpdates"
            ),
            InlineKeyboardButton(
                text="Support", url="https://t.me/StormSupportChat"
            ),                       
        ],        
        [
            InlineKeyboardButton(
                text="🔗 Deploy your own bot", url="https://github.com/MissCutie/MissCutie"
            ),                                  
        ]
    ]
    return buttons


def private_panel(_, BOT_USERNAME):
    buttons = [
        [
            InlineKeyboardButton(
                text="Add me to your group ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Help", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="Updates", url=f"https://t.me/StormUpdates"),
            InlineKeyboardButton(
                text="Support", url=f"https://t.me/StormSupportChat"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="🏳️‍🌈 Language", callback_data="LG"
                )
        ],
        [
            InlineKeyboardButton(
                text="🔗 Deploy your own bot", url="https://github.com/MissCutie/MissCutie"
            )
        ]
     ]
    return buttons
