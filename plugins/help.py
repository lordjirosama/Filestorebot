import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from bot import Bot
from pyrogram.enums import ParseMode
from helper_func import get_next_image
from plugins.Unrated_Coder import is_admin
from config import OWNER_ID


HELP_TEXT = """<b>🥰 ᴋᴏɴ’ɴɪᴄʜɪᴡᴀ USER_MENTION_PLACEHOLDER! ~</b>
<blockquote expandable><b>⚔️ ɪ'ᴍ ɪꜱʜᴛᴀʀ, ᴛʜᴇ ɢᴏᴅᴅᴇꜱꜱ ᴏꜰ ꜰᴇʀᴛɪʟɪᴛʏ! 🎥
ᴏɴʟʏ ᴍʏ ᴄʜᴏꜱᴇɴ ᴅᴀʀʟɪɴɢꜱ ɢᴇᴛ ᴛᴏ ᴛᴏᴜᴄʜ ᴍʏ ꜱᴇᴄʀᴇᴛ ᴀɴɪᴍᴇ ᴀʀᴄʜɪᴠᴇꜱ. ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟꜱ, ᴏʀ ɴᴏ ᴛʀᴇᴀꜱᴜʀᴇꜱ ꜰᴏʀ ʏᴏᴜ! 🔓</b></blockquote>
<b>🪄 ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴍᴇ?</b>
<blockquote expandable><b>⚙️ ᴀʜʜʜ! ᴅᴏɴ'ᴛ ᴛᴇʟʟ ᴍᴇ ʏᴏᴜ'ʀᴇ ᴛʜᴀᴛ ʜᴇʟᴘʟᴇꜱꜱ ᴡɪᴛʜᴏᴜᴛ ᴍʏ ɢᴜɪᴅᴀɴᴄᴇ? ꜰɪɴᴇ, ɪ'ʟʟ ʟᴇᴛ ʏᴏᴜ ᴡᴀᴛᴄʜ ᴍʏ ꜱɪᴍᴘʟᴇ ᴛᴜᴛᴏʀɪᴀʟ! 😉</b>
👉 <b><a href="https://t.me/+0bPLOJYCDysxYTY1">ᴄʟɪᴄᴋ ʜᴇʀᴇ ꜰᴏʀ ᴛᴜᴛᴏʀɪᴀʟ 🎬</a></b></blockquote>
<b>» ᴄᴏᴍᴍᴀɴᴅꜱ:</b>
<blockquote expandable>‣ <b>/start</b> - ᴀᴡᴀᴋᴇɴ ᴍᴇ! 🟢
‣ <b>/help</b> – ʙᴇɢ ꜰᴏʀ ᴍʏ ɢᴜɪᴅᴇ 📜</blockquote>
<b>◈ ɴᴇᴇᴅ ᴀꜱꜱɪꜱᴛᴀɴᴄᴇ? ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴍᴀꜱᴛᴇʀ ʙᴇʟᴏᴡ ⚙️</b>"""


ADMIN_HELP_TEXT = """<b>👑 ᴏʜ? ʟᴏᴏᴋs ʟɪᴋᴇ ᴀ ᴡᴏʀᴛʜʏ ᴍᴀsᴛᴇʀ ʜᴀs ᴀʀʀɪᴠᴇᴅ! ~</b>
<blockquote expandable><b>✨ ʜᴇʀᴇ ᴀʀᴇ ʏᴏᴜʀ sᴇᴄʀᴇᴛ ᴄᴏɴᴛʀᴏʟs, ᴍʏ ᴅᴀʀʟɪɴɢ. ᴜsᴇ ᴛʜᴇᴍ ᴡɪsᴇʟʏ ᴀɴᴅ ᴅᴏɴ'ᴛ ᴍᴀsʜ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ᴛᴏᴏ ʜᴀʀᴅ! 😉</b></blockquote>
<b>» ᴀᴅᴍɪɴ ᴘᴏᴡᴇʀs:</b>
<blockquote expandable>• <b>/dlt_time</b> | <b>/check_dlt_time</b>
• <b>/dbroadcast</b> | <b>/pbroadcast</b>
• <b>/ban</b> | <b>/unban</b> | <b>/banlist</b>
• <b>/addchnl</b> | <b>/delchnl</b> | <b>/listchnl</b> | <b>/fsub_mode</b>
• <b>/add_admin</b> | <b>/deladmin</b> | <b>/admins</b></blockquote>
<b>🔙 ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴏ ʙᴀᴄᴋ!</b>"""


@Bot.on_message(filters.command("help") & filters.private)
async def help_command(client: Client, message: Message):
    user_mention = f"<a href='tg://user?id={message.from_user.id}'>➣ {message.from_user.first_name}</a>"

    loading = await message.reply_text("<b>ʟᴏᴀᴅɪɴɢ!</b>")
    for dots in ["!!", "!!!", "!!!!", "!!!!!"]:
        await asyncio.sleep(0.12)
        await client.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
        await loading.edit_text(f"<b>ʟᴏᴀᴅɪɴɢ{dots}</b>")

    await loading.delete()

    await client.send_photo(
        chat_id=message.chat.id,
        photo=get_next_image(message.chat.id),
        caption=HELP_TEXT.replace("USER_MENTION_PLACEHOLDER", user_mention),
        has_spoiler=True,
        parse_mode=ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅꜱ •", callback_data="admin_cmds", style="primary")
                ],
                [
                    InlineKeyboardButton("• ᴏᴡɴᴇʀ", url="https://t.me/UnknownBotz", style="success"),
                    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ •", url="https://t.me/UnknownBotz", style="success")
                ],
                [
                    InlineKeyboardButton("• ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ •", url="https://t.me/UnknownBotz", style="success")
                ],
            ]
        )
    )


@Bot.on_callback_query(filters.regex("^admin_cmds$"))
async def admin_cmds_callback(client: Client, callback_query):
    user_id = callback_query.from_user.id
    
    if not (user_id == OWNER_ID or await is_admin(user_id)):
        await callback_query.answer(
            text="ʜᴍᴘʜ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴛᴏ ᴠɪᴇᴡ ᴍʏ sᴇᴄʀᴇᴛ ʟɪsᴛ, ʏᴏᴜ ᴄʟᴜᴍsʏ ʜᴜᴍᴀɴ! ʙᴇɢᴏɴᴇ! ᴘᴘʜʜᴛᴛ~ 😜",
            show_alert=True
        )
        return

    await callback_query.answer()
    await callback_query.message.edit_media(
        media=InputMediaPhoto(
            media=get_next_image(callback_query.message.chat.id),
            caption=ADMIN_HELP_TEXT,
            has_spoiler=True
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ʙᴀᴄᴋ ᴛᴏ ʜᴇʟᴘ •", callback_data="back_to_help", style="success")
                ]
            ]
        )
    )


@Bot.on_callback_query(filters.regex("^back_to_help$"))
async def back_to_help_callback(client: Client, callback_query):
    await callback_query.answer()
    user_mention = f"<a href='tg://user?id={callback_query.from_user.id}'>➣ {callback_query.from_user.first_name}</a>"
    
    await callback_query.message.edit_media(
        media=InputMediaPhoto(
            media=get_next_image(callback_query.message.chat.id),
            caption=HELP_TEXT.replace("USER_MENTION_PLACEHOLDER", user_mention),
            has_spoiler=True
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅꜱ •", callback_data="admin_cmds", style="primary")
                ],
                [
                    InlineKeyboardButton("• ᴏᴡɴᴇʀ", url="https://t.me/UnknownBotz", style="success"),
                    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ •", url="https://t.me/UnknownBotz", style="success")
                ],
                [
                    InlineKeyboardButton("• ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ •", url="https://t.me/UnknownBotz", style="success")
                ],
            ]
        )
    )
