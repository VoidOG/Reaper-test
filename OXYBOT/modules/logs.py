import asyncio
import psutil
from datetime import datetime
from config import X1, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from telethon import events  

LOG_GROUP_ID = -1002183841044  # Log group ID for bot logs

@X1.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
async def logs(legend):
    if legend.sender_id == OWNER_ID:
        start = datetime.now()
        fetch = await legend.reply("__Fetching Bot and VPS Status...__")

        # Fetching bot and VPS status
        cpu_usage = psutil.cpu_percent()
        memory_info = psutil.virtual_memory()
        disk_usage = psutil.disk_usage('/')
        bot_uptime = datetime.now() - start

        # Format uptime into hours, minutes, seconds
        uptime_seconds = int(bot_uptime.total_seconds())
        hours, remainder = divmod(uptime_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Fetching bot statistics
        total_chats = len(await X1.get_dialogs())
        total_users = len(SUDO_USERS)  # Assuming all SUDO_USERS are unique

        log_content = "● **Bot & VPS Status** 🔧\n\n"
        log_content += f"● **Bot Uptime:** `{hours}h {minutes}m {seconds}s`\n"
        log_content += f"● **CPU Usage:** `{cpu_usage}%`\n"
        log_content += f"● **Memory Usage:** `{memory_info.percent}%`\n"
        log_content += f"● **Disk Usage:** `{disk_usage.percent}%`\n"
        log_content += f"● **Number of Chats:** `{total_chats}`\n"
        log_content += f"● **Number of Users Using the Bot:** `{total_users}`\n"
        log_content += f"● **Number of SUDO Users:** `{len(SUDO_USERS)}`\n\n"

        # Add current timestamp
        log_content += f"● **Timestamp:** `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`\n\n"

        # Adding SUDO Users with profile links
        log_content += "**🔹 SUDO Users:**\n"
        for user_id in SUDO_USERS:
            user_profile_link = f"https://t.me/{user_id}"
            log_content += f"• [{user_id}]({user_profile_link})\n"

        # Send the logs to the log group
        try:
            await X1.send_message(LOG_GROUP_ID, log_content)
            await fetch.edit("✅ **Logs sent to the log group successfully!**")
        except Exception as e:
            await fetch.edit(f"❌ **An Exception Occurred!**\n\n**ERROR:** {str(e)}")

    elif legend.sender_id in SUDO_USERS:
        await legend.reply("🚫 » ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")
