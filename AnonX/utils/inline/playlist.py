from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴩᴇʀsᴏɴᴀʟ",
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(
                text="ɢʟᴏʙᴀʟ", callback_data="get_top_playlists"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ اغلاق ✯", callback_data="اغلاق"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴛᴏᴘ 10 ᴘʟᴀʏʟɪsᴛs", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴘᴇʀsᴏɴᴀʟ", callback_data="SERVERTOP user"
            )
        ],
        [
            InlineKeyboardButton(
                text="ɢʟᴏʙᴀʟ", callback_data="SERVERTOP global"
            ),
            InlineKeyboardButton(
                text="ɢʀᴏᴜᴘ's", callback_data="SERVERTOP chat"
            )
        ],
        [
            InlineKeyboardButton(
                text="رجوع", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="اغلاق", callback_data="اغلاق"
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴜᴅɪᴏ", callback_data="play_playlist a"
            ),
            InlineKeyboardButton(
                text="ᴠɪᴅᴇᴏ", callback_data="play_playlist v"
            ),
        ],
        [
            InlineKeyboardButton(
                text="رجوع", callback_data="home_play"
            ),
            InlineKeyboardButton(
                text="اغلاق", callback_data="اغلاق"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴛᴏᴘ 10 ᴘʟᴀʏʟɪsᴛs", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴘᴇʀsᴏɴᴀʟ", callback_data="SERVERTOP Personal"
            )
        ],
        [
            InlineKeyboardButton(
                text="ɢʟᴏʙᴀʟ", callback_data="SERVERTOP Global"
            ),
            InlineKeyboardButton(
                text="ɢʀᴏᴜᴘ's", callback_data="SERVERTOP Group"
            )
        ],
        [
            InlineKeyboardButton(
                text="رجوع", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="اغلاق", callback_data="اغلاق"
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="رجوع",
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(
                text="اغلاق", callback_data="اغلاق"
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ᴅᴇʟᴇᴛᴇ",
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="رجوع",
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text="اغلاق",
                    callback_data="اغلاق",
                ),
            ],
        ]
    )
    return upl


def اغلاق_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="✯ اغلاق ✯",
                    callback_data="اغلاق",
                ),
            ]
        ]
    )
    return upl
