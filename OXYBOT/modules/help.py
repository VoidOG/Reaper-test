from telethon import events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, CMD_HNDLR as hl


HELP_STRING = f"🏴‍☠️𝕽𝖊𝖆𝖕𝖊𝖗🏴‍☠️ ʜᴇʟᴘ ᴍᴇɴᴜ ★\n\n» **ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ꜰᴏʀ ʜᴇʟᴘ**\n» **ᴅᴇᴠᴇʟᴏᴘᴇʀ: @Cenzeo**"

HELP_BUTTON = [
    [
      Button.inline("ꜱᴘᴀᴍ", data="spam"),
      Button.inline("ʀᴀɪᴅ", data="raid")
    ],
    [
      Button.inline("ᴄᴏᴍᴍᴀɴᴅꜱ", data="extra")
    ],
    [
      Button.url("ᴏᴡɴᴇʀ", "https://t.me/cenzeo"),
      Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/Reaper_Support")
    ],
  [   
      Button.inline("ɴᴇᴡ ᴄᴏᴍᴍᴀɴᴅꜱ", data="yash")
      
  ]
]


@X1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
        try:
          await event.client.send_file(event.chat_id,
              "https://telegra.ph/file/b11e7d86e4622a3b3e54e.jpg",
              caption=HELP_STRING,
              buttons=HELP_BUTTON
              )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"An Exception Occured!\n\n**ERROR:** {str(e)}")


extra_msg = f"""
**» ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅs:**

ᴜsᴇʀ ʙᴏᴛ: **ᴜsᴇʀʙᴏᴛ ᴄᴍᴅs**
  1) {hl}ᴘɪɴɢ
  2) {hl}ʀᴇʙᴏᴏᴛ
  3) {hl}sᴜᴅᴏ <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ>  --> ᴏᴡɴᴇʀ ᴄᴍᴅ
  4) {hl}ʟᴏɢs --> ᴏᴡɴᴇʀ ᴄᴍᴅ

**ᴇᴄʜᴏ:** ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜsᴇʀ
  1) {hl}ᴇᴄʜᴏ <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ>
  2) {hl}ʀᴍᴇᴄʜᴏ <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ>

**ʟᴇᴀᴠᴇ:** ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ / ᴄʜᴀɴɴᴇʟ
  1) {hl}ʟᴇᴀᴠᴇ <ɢʀᴏᴜᴘ/ᴄʜᴀᴛ ɪᴅ>
  2) {hl}ʟᴇᴀᴠᴇ: ᴛʏᴘᴇ ɪɴ ᴛʜᴇɪʀ ɢʀᴏᴜᴘ ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ɢʀᴏᴜᴘ 

**ᴀʙᴜsᴇsᴘᴀᴍ:** ᴏɴᴇ ᴡᴏʀᴅ ʙɪɢ ɢᴀᴀʟɪ sᴘᴀᴍ
  1) {hl}ᴀʙᴜsᴇ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  
**© @Cenzeo **
"""



yash_msg = f"""
**» ɴᴇᴡ ᴄᴏᴍᴍᴀɴᴅs:**

**» ɢᴏᴏᴅ ᴀғᴛᴇʀɴᴏᴏɴ:**
**ᴀғᴛᴇʀ ɴᴏᴏɴ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜsᴇʀ ғᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ**
  1) {hl}ɢᴀ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}ɢᴀ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>

**ᴇᴍᴏᴊɪ:**
**ᴇᴍᴏᴊɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ᴇᴍᴏᴊɪ <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜsᴇʀ>
  2) {hl}ᴇᴍᴏᴊɪ <ᴜsᴇʀɴᴀᴍᴇ>

**ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ:**
**ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ɢᴍ <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜsᴇʀ>
  2) {hl}ɢᴍ <ᴜsᴇʀɴᴀᴍᴇ>

**ɢᴏᴏᴅ ɴɪɢʜᴛ:**
**ɢᴏᴏᴅ ɴɪɢʜᴛ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ɢɴ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}ɢɴ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>

**sʜʏʀɪ ʀᴀɪᴅ:**
**sʜʏʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}sʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <username>
  2) {hl}sʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>

**ғʟɪʀᴛɪɴɢ:**
**ғʟɪʀᴛ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ғʟɪʀᴛ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}ғʟɪʀᴛ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>

**ʙɪʀᴛʜᴅᴀʏ:**
**ғʟɪʀᴛ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ʙsᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}ʙsᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>


**© @Cenzeo **
"""

                 
raid_msg = f"""
**» ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅs:**
**ʀᴀɪᴅ:**
**ᴀᴄᴛɪᴠᴀᴛᴇs ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪvɪᴅᴜᴀʟ ᴜsᴇʀ ғᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ**
  1) {hl}ʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}ʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ>

**ʀᴇᴘʟʏʀᴀɪᴅ:**
**ᴀᴄᴛɪᴠᴀᴛᴇs ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ʀʀᴀɪᴅ <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜsᴇʀ>
  2) {hl}ʀʀᴀɪᴅ <ᴜsᴇʀɴᴀᴍᴇ>

**ᴅʀᴇᴘʟʏʀᴀɪᴅ:**
**ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇs ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ᴅʀʀᴀɪᴅ <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜsᴇʀ>
  2) {hl}ᴅʀʀʀᴀɪᴅ <ᴜsᴇʀɴᴀᴍᴇ>

**ᴍʀᴀɪᴅ:**
**ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ᴍʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}ᴍʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ>

**sʀᴀɪᴅ:**
**sʜᴀʏᴀʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}sʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}sʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ>

**ᴄʀᴀɪᴅ:**
**ᴀʙᴄᴅ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ᴄʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}ᴄʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ>
  
**© @Cenzeo **
"""

spam_msg = f"""
**» sᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅs:**

**sᴘᴀᴍ:**
**sᴘᴀᴍs ᴀ ᴍᴇssᴀɢᴇ**
  1) {hl}sᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ᴍᴇssᴀɢᴇ ᴛᴏ sᴘᴀᴍ> (yᴏᴜ ᴄᴀɴ ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇs sᴀɢᴇ ɪғ ᴜ ᴡᴀɴᴛ ᴛᴏ ʀᴇᴘʟʏ ᴛʜᴀᴛ ᴍᴇssᴀɢᴇ ᴀɴᴅ ᴅᴏ sᴘᴀᴍᴍɪɴɢ)
  2) {hl}sᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏɪɴɢ ᴀɴʏ ᴍᴇssᴀɢᴇ>

**pᴏʀɴsᴘᴀᴍ:**
**pᴏʀɴᴏɢʀᴀᴘʜʏ sᴘᴀᴍ**
  1) {hl}p sᴘᴀᴍ <ᴄᴏᴜɴᴛ>

**hᴀɴɢ:**
**sᴘᴀᴍs hᴀɴɢ ᴍᴇssᴀɢᴇ ғᴏʀ gɪᴠᴇɴ cᴏᴜɴᴛᴇʀs**
  1) {hl}hᴀɴɢ <ᴄᴏᴜɴᴛᴇʀ>


** © @Cenzeo**
"""                     
           
           
@X1.on(events.CallbackQuery(pattern=r"help_back"))
@X2.on(events.CallbackQuery(pattern=r"help_back"))
@X3.on(events.CallbackQuery(pattern=r"help_back"))
@X4.on(events.CallbackQuery(pattern=r"help_back"))
@X5.on(events.CallbackQuery(pattern=r"help_back"))
@X6.on(events.CallbackQuery(pattern=r"help_back"))
@X7.on(events.CallbackQuery(pattern=r"help_back"))
@X8.on(events.CallbackQuery(pattern=r"help_back"))
@X9.on(events.CallbackQuery(pattern=r"help_back"))
@X10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(
            HELP_STRING,
            buttons=[
              [
                Button.inline("ꜱᴘᴀᴍ", data="spam"),
                Button.inline("ʀᴀɪᴅ", data="raid"),
                Button.inline("ɴᴇᴡ ᴄᴏᴍᴍᴀɴᴅꜱ", data="yash")
              ],
              [
                Button.inline("ᴄᴏᴍᴍᴀɴᴅꜱ", data="extra")
              ],
              [
                Button.url("ᴏᴡɴᴇʀ", "https://t.me/Cenzeo"),
                Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/Reaper_Support")
              ]
            ]
          )
    else:
        await event.answer("" , cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"spam"))
@X2.on(events.CallbackQuery(pattern=r"spam"))
@X3.on(events.CallbackQuery(pattern=r"spam"))
@X4.on(events.CallbackQuery(pattern=r"spam"))
@X5.on(events.CallbackQuery(pattern=r"spam"))
@X6.on(events.CallbackQuery(pattern=r"spam"))
@X7.on(events.CallbackQuery(pattern=r"spam"))
@X8.on(events.CallbackQuery(pattern=r"spam"))
@X9.on(events.CallbackQuery(pattern=r"spam"))
@X10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(spam_msg,
              buttons=[[Button.inline("< Back", data="help_back"),],],
              ) 
    else:
        await event.answer("ᴊᴏɪɴ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ꜰᴏʀ ꜱᴜᴅᴏ ᴀɴᴅ ʙᴏᴛ ᴜᴘᴅᴀᴛᴇꜱ", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"raid"))
@X2.on(events.CallbackQuery(pattern=r"raid"))
@X3.on(events.CallbackQuery(pattern=r"raid"))
@X4.on(events.CallbackQuery(pattern=r"raid"))
@X5.on(events.CallbackQuery(pattern=r"raid"))
@X6.on(events.CallbackQuery(pattern=r"raid"))
@X7.on(events.CallbackQuery(pattern=r"raid"))
@X8.on(events.CallbackQuery(pattern=r"raid"))
@X9.on(events.CallbackQuery(pattern=r"raid"))
@X10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
          )
    else:
        await event.answer("ᴊᴏɪɴ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ꜰᴏʀ ꜱᴜᴅᴏ ᴀɴᴅ ʙᴏᴛ ᴜᴘᴅᴀᴛᴇꜱ", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"extra"))
@X2.on(events.CallbackQuery(pattern=r"extra"))
@X3.on(events.CallbackQuery(pattern=r"extra"))
@X4.on(events.CallbackQuery(pattern=r"extra"))
@X5.on(events.CallbackQuery(pattern=r"extra"))
@X6.on(events.CallbackQuery(pattern=r"extra"))
@X7.on(events.CallbackQuery(pattern=r"extra"))
@X8.on(events.CallbackQuery(pattern=r"extra"))
@X9.on(events.CallbackQuery(pattern=r"extra"))
@X10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            )
    else:
        await event.answer("ᴊᴏɪɴ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ꜰᴏʀ ꜱᴜᴅᴏ ᴀɴᴅ ʙᴏᴛ ᴜᴘᴅᴀᴛᴇꜱ", cache_time=0, alert=True)
        

@X1.on(events.CallbackQuery(pattern=r"yash"))
@X2.on(events.CallbackQuery(pattern=r"yash"))
@X3.on(events.CallbackQuery(pattern=r"yash"))
@X4.on(events.CallbackQuery(pattern=r"yash"))
@X5.on(events.CallbackQuery(pattern=r"yash"))
@X6.on(events.CallbackQuery(pattern=r"yash"))
@X7.on(events.CallbackQuery(pattern=r"yash"))
@X8.on(events.CallbackQuery(pattern=r"yash"))
@X9.on(events.CallbackQuery(pattern=r"yash"))
@X8.on(events.CallbackQuery(pattern=r"yash"))
async def help_yash(event):
     if event.query.user_id in SUDO_USERS:
         await event.edit(yash_msg,
             buttons=[[Button.inline("< Back", data="help_back"),],],
             )
     else:
         await event.answer("ᴊᴏɪɴ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ꜰᴏʀ ꜱᴜᴅᴏ ᴀɴᴅ ʙᴏᴛ ᴜᴘᴅᴀᴛᴇꜱ", cache_time=0, alert=True)

