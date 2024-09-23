import asyncio
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from datetime import datetime
from telethon import events
import psutil 

LOG_GROUP_ID = -1002183841044 

@X1.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
async def logs(legend):
    if legend.sender_id == OWNER_ID:
        start = datetime.now()
        fetch = await legend.reply("__Fetching Bot and VPS Status...__")

        bot_uptime = datetime.now() - start
        cpu_usage = psutil.cpu_percent()
        memory_info = psutil.virtual_memory()
        
        log_content = f"**Bot Uptime:** {bot_uptime}\n"
        log_content += f"**CPU Usage:** {cpu_usage}%\n"
        log_content += f"**Memory Usage:** {memory_info.percent}%\n\n"
        
        log_content += "**SUDO Users:**\n"
        for user_id in SUDO_USERS:
            user_profile_link = f"https://t.me/{user_id}"
            log_content += f"• [{user_id}]({user_profile_link})\n"

        try:
            await X1.send_message(LOG_GROUP_ID, log_content)
            await fetch.edit(f"Logs sent to the log group successfully.")
        except Exception as e:
            await fetch.edit(f"An Exception Occurred!\n\n**ERROR:** {str(e)}")

    elif legend.sender_id in SUDO_USERS:
        await legend.reply("» ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")

# @Cenzeo
