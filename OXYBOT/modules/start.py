from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("ᴄᴏᴍᴍᴀɴᴅꜱ", data="help_back")
    ],
    [
        Button.url("ᴏᴡɴᴇʀ", "https://t.me/cenzeo"),
        Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/Reaper_Support")
    ],
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ [{bot_name}](tg://user?id={bot_id}) , ᴛʜᴇ ᴜʟᴛɪᴍᴀᴛᴇ ᴡᴇᴀᴘᴏɴ ꜰᴏʀ ᴄʜᴀᴏs ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ! ᴀs ᴛʜᴇ ᴍᴏsᴛ ᴘᴏᴡᴇʀꜰᴜʟ sᴘᴀᴍ ʙᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ, ʀᴇᴀᴘᴇʀ ᴄᴀɴ ᴜɴʟᴇᴀsʜ ʀᴇʟᴇɴᴛʟᴇss ᴡᴀᴠᴇs ᴏf ᴍᴇssᴀɢᴇs ᴀɴᴅ ʟᴀᴜɴᴄʜ ʀᴀɪᴅs ᴏɴ ᴜsᴇʀs ᴡɪᴛʜ ᴘʀᴇᴄɪsɪᴏɴ. ᴅᴇsɪɢɴᴇᴅ ꜰᴏʀ ᴛʜᴏsᴇ ᴡʜᴏ ᴅᴀʀᴇ ᴛᴏ ᴘᴜsʜ ʙᴏᴜɴᴅᴀʀɪᴇs, ᴛʜɪs ʙᴏᴛ ᴏғғᴇʀs ᴜɴᴘᴀʀᴀʟʟᴇʟᴇᴅ ᴄᴀᴘᴀʙɪʟɪᴛɪᴇs ꜰᴏʀ sᴘᴀᴍᴍɪɴɢ ᴀɴᴅ ᴜsᴇʀ ᴇɴɢᴀɢᴇᴍᴇɴᴛ. ᴇᴍʙʀᴀᴄᴇ ᴛʜᴇ ᴘᴏᴡᴇʀ ᴏf ʀᴇᴀᴘᴇʀ ᴀɴᴅ ᴛᴀᴋᴇ ᴄᴏɴᴛʀᴏʟ ᴏf ᴛʜᴇ ᴅɪɢɪᴛᴀʟ ʙᴀᴛᴛʟᴇfɪᴇʟᴅ!**\n"
        await event.client.send_file(
            event.chat_id,
            "https://telegra.ph/file/b11e7d86e4622a3b3e54e.jpg",
            caption=TEXT,
            buttons=START_BUTTON
        )
