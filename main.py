# Codes by: @A_l_i_y_e_v_d_i

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import time
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
KANAL_ID = os.getenv("KANAL_ID")

IT = Client(
	"Etiraf Bot",
	api_id=API_ID,
	api_hash=API_HASH,
	bot_token=BOT_TOKEN,
        kanal_id=KANAL_ID,
	)

CHL = -1001617550080

PM = 2066118611

@IT.on_message(
	filters.command("start")
	& filters.private
	)
async def start(client: IT, message: Message):
	await message.reply_text(f"<b> {message.from_user.mention} Xoş Gəldiniz,Mən @A_l_i_y_e_v_d_i tərəfindən hazırlanan bir etiraf botuyam.\nEtiraflarınızı @Nexus_Etiraf_Kanal kanalında paylaşılacq.\n\nSəndə bir etiraf etmək istəyirsən'sə komutlar;\nGizli Etiraf🙈: /ano mesaj\nAçıq Etiraf😋: /etiraf mesaj</b>")

@IT.on_message(
	filters.command("ano")
	& filters.private
	)
async def ano(client: IT, message: Message):
	text = " ".join(message.command[1:])
	if text == "":
		await message.reply_text("Xahiş Olunur Bir Etiraf yazıb yenidən cəhd edin😕.")
	else:
		await IT.send_message(chat_id=CHL, text=f"Göndərilən: GİZLİ\nEtiraf🙈: {text}")
		time.sleep(0.5)
		await IT.send_message(chat_id=PM, text=f"Göndərilən: {message.from_user.mention}\nEtiraf😋: {text}")
		time.sleep(0.5)
		await message.reply_text("Etirafnız Adminə Göndərildi təstiq etdikdən sonra @Nexus_Etiraf_Kanal kanalında paylaşılacaq🤓.")

@IT.on_message(
	filters.command("etiraf")
	& filters.private
	)
async def etf(client: IT, message: Message):
	t = " ".join(message.command[1:])
	if t == "":
		await message.reply_text("Xahiş olunur bir etiraf yazıb təkrar cəhd edin😕.")
	else:
		await IT.send_message(chat_id=CHL, text=f"Göndərilən: {message.from_user.mention}\nEtiraf😋: {t}")
		time.sleep(0.5)
		await message.reply_text("Etiraflarınıx Adminə Göndərildi təsdiq etdikdən sonra @Nexus_Etiraf_Kanal kanalında paylaşılacaq🤓.")

IT.run()
