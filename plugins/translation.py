#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

class Translation(object):

    START_MSG = """
<b>👋Hi {},</b>

<code>🤖 I am a Simple Bot For Finding IDs in Telegram. 🔍 🆔</code>

<b>👉 Click the Help Button or Hits /help for more Information. ℹ️</b>
"""

    HELP_MSG = """
<b><u> The Following is the Recovery Method</u></b>

▷Click the Telegram ID Button Or Hits /id Below to Pick your ID.

▷Click the Telegram Info Button Or Hits /info Below to Pick your Telegram information.

▷If you send a message [using the forward tag] from your [Public or Private] group you will receive the ID of that Group.

▷If you send a message [using the forward tag] from your [Public or Private] channel you will receive the ID of that Channel.

▷If you need the ID of any Bots, Send Bot Message here from that bot [With forward Tag]

▷If you need a Telegram User Id, Forward a Message to them here [With forward Tag]

▷If you give your reply /Json ang [Messages, Files, Media, Stickers] you will get the Json files of those Files.
  
▷If you need to get an I'D of Sticker pack just send the sticker and reply with /stickerid command you would get its ID.
"""

    ABOUT_MSG = """
<b><u>🤖 My name</u> : <a href='https://t.me/{}'>idsRobot</a> 
  
<u>📝 Language</u> : <a href='https://www.python.org/'>𝐏𝐲𝐭𝐡𝐨𝐧3</a>

<u>🧰 Frame Work</u> : <a href='https://github.com/pyrogram/pyrogram'>𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦</a>

<u>👨‍💻 Developer</u> : <a href='t.me/{}'>@ZauteKm</a>

<u>👥 Group</u> :   <a href='t.me/{}'>Contact here</a>
 
<u>📢 Channel</u> : <a href='t.me/{}'>TGBotsProJect</a>

<u>❣️ YouTube</u> : <a href='https://youtube.com/channel/ZauteKm'>Subscribe Now</a>

<u>🔘 Source Code</u> : <a href='{}'>Click me</a></b>
"""

    JOIN_TEXT = """
📢 Join my Updates Channel 📢
"""
 
    TRY_TEXT = """
🔃 ReStart Now 🔃
"""

    FSUB_TEXT = """
📢 Join My Update Channel Then Use This Bot 📢
"""

    ID_TEXT = """
🆔 Your Telegram ID is :- <code>{}</code>
"""

    INFO_TEXT = """
<u>ℹ️ Your Information</u>

 🙋🏻‍♂️ First Name : <b>{}</b>

 🧖‍♂️ Last Name : <b>{}</b>

 🧑🏻‍🎓 User Name : <b>@{}</b>

 🆔 Telegram ID : <code>{}</code>

 🌌 Profile Link : <b>{}</b>

 🌍 DC : <b>{}</b>

 🎤 Language : <b>{}</b>

 🤠 Status : <b>{}</b>
"""
