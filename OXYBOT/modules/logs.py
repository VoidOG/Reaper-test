import asyncio
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl

from datetime import datetime
from telethon import events

# Function to generate the profile link from user id
def generate_profile_link(user_id):
    return f"https://t.me/{user_id}"

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
        fetch = await legend.reply(f"__Fetching SUDO User Details...__")

        # Creating the log content with SUDO user profile links
        log_content = "ʀᴇᴀᴘᴇʀ [ SUDO Users ]\n\n"
        log_content += "SUDO Users:\n"
        for user_id in SUDO_USERS:
            user_profile_link = generate_profile_link(user_id)
            log_content += f"• [{user_id}]({user_profile_link})\n"

        # Save the SUDO user details in a file named after the first sudo user
        sudo_user_filename = f"SUDO_{SUDO_USERS[0]}_Details.txt"
        with open(sudo_user_filename, "w") as logfile:
            logfile.write(log_content)

        end = datetime.now()
        ms = (end-start).seconds
        await asyncio.sleep(1)

        try:
            await X1.send_file(legend.chat_id, sudo_user_filename, caption=f"⚡ **SUDO USER DETAILS** ⚡\n  » **ᴛɪᴍᴇ ᴛᴀᴋᴇɴ:** `{ms} ꜱᴇᴄᴏɴᴅꜱ`")
            await fetch.delete()
        except Exception as e:
            await fetch.edit(f"An Exception Occurred!\n\n**ERROR:** {str(e)}")

    elif legend.sender_id in SUDO_USERS:
        await legend.reply("» ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")
