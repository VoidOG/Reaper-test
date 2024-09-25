import sys
import logging
from os import execl, getenv
from datetime import datetime

from telethon import events
from telethon import TelegramClient
from OXYBOT.data import OXYGEN

from config import API_ID, API_HASH, CMD_HNDLR as hl, OWNER_ID, SUDO_USERS

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

# Initialize clients
X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=getenv("BOT_TOKEN", default="YOUR_BOT_TOKEN"))
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=getenv("BOT_TOKEN2", default="YOUR_BOT_TOKEN2"))
X3 = TelegramClient('X3', API_ID, API_HASH).start(bot_token=getenv("BOT_TOKEN3", default="YOUR_BOT_TOKEN3"))
X4 = TelegramClient('X4', API_ID, API_HASH).start(bot_token=getenv("BOT_TOKEN4", default="YOUR_BOT_TOKEN4"))
X5 = TelegramClient('X5', API_ID, API_HASH).start(bot_token=getenv("BOT_TOKEN5", default="YOUR_BOT_TOKEN5"))
X6 = TelegramClient('X6', API_ID, API_HASH).start(bot_token=getenv("BOT_TOKEN6", default="YOUR_BOT_TOKEN6"))
X7 = TelegramClient('X7', API_ID, API_HASH).start(bot_token=getenv("BOT_TOKEN7", default="YOUR_BOT_TOKEN7"))
X8 = TelegramClient('X8', API_ID, API_HASH).start(bot_token=getenv("BOT_TOKEN8", default="YOUR_BOT_TOKEN8"))
X9 = TelegramClient('X9', API_ID, API_HASH).start(bot_token=getenv("BOT_TOKEN9", default="YOUR_BOT_TOKEN9"))
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=getenv("BOT_TOKEN10", default="YOUR_BOT_TOKEN10"))

# Ping Command
@X1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        jarvis = await e.reply(f"ʀᴇᴀᴘᴇʀ ɪꜱ ʀᴇᴀᴅʏ ᴛᴏ ʀᴇᴀᴘ ᴇᴠᴇʀʏᴏɴᴇ")
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await jarvis.edit(f"[ʀᴇᴀᴘᴇʀ ɪꜱ ʀᴇᴀᴅʏ ᴛᴏ ʀᴇᴀᴘ ᴇᴠᴇʀʏᴏɴᴇ 👾](https://t.me/Reaper_Support)\n» `{mp} ᴍꜱ`")

# Restart Command
@X1.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        await e.reply(f"Reaper is starting...")
        try:
            await X1.disconnect()
        except Exception:
            pass
        try:
            await X2.disconnect()
        except Exception:
            pass
        try:
            await X3.disconnect()
        except Exception:
            pass
        try:
            await X4.disconnect()
        except Exception:
            pass
        try:
            await X5.disconnect()
        except Exception:
            pass
        try:
            await X6.disconnect()
        except Exception:
            pass
        try:
            await X7.disconnect()
        except Exception:
            pass
        try:
            await X8.disconnect()
        except Exception:
            pass
        try:
            await X9.disconnect()
        except Exception:
            pass
        try:
            await X10.disconnect()
        except Exception:
            pass

        execl(sys.executable, sys.executable, *sys.argv)

# Add Sudo Command
@X1.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def add_sudo(event):
    if event.sender_id == OWNER_ID:
        target = ""
        if event.reply_to_msg_id:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        else:
            await event.reply("Reply to a user to add them as sudo.")
            return
        
        if target in SUDO_USERS:
            await event.reply(f"User is already a sudo: {target}")
            return
        
        SUDO_USERS.append(target)
        await event.reply(f"User {target} added as sudo.")
        # You can save SUDO_USERS to a file or database here

# Remove Sudo Command
@X1.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
async def remove_sudo(event):
    if event.sender_id == OWNER_ID:
        target = ""
        if event.reply_to_msg_id:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        else:
            await event.reply("Reply to a user to remove them from sudo.")
            return

        if target not in SUDO_USERS:
            await event.reply(f"User {target} is not in the sudo list.")
            return
        
        SUDO_USERS.remove(target)
        await event.reply(f"User {target} removed from sudo.")
        # You can save SUDO_USERS to a file or database here

# List Sudo Command
@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
async def show_sudo_users(event):
    if event.sender_id == OWNER_ID:
        sudo_users_list = "Current Sudo Users:\n"
        for user_id in SUDO_USERS:
            sudo_users_list += f"- {user_id}\n"
        await event.reply(sudo_users_list)
    else:
        await event.reply("Only the owner can view the sudo users list.")
