from pyrogram import Client

API_ID = 24288289
API_HASH = "f07ca787bf3a9e9b622f6b61e2bc2cd2"
BOT_TOKEN = 8608788625:AAG8JhjGyNzGEN7KiGJ_DCY5xOTy_5eYvCg

app = Client(
    "skmusicbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message()
async def start(_, msg):
    if msg.text == "/start":
        await msg.reply("🎵 SK Music Bot Running Successfully!")

app.run()
