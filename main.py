from pyrogram import Client, filters, idle
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped
import yt_dlp

API_ID = 24288289
API_HASH = "f07ca787bf3a9e9b622f6b61e2bc2cd2"
BOT_TOKEN = "8608788625:AAG8JhjGyNzGEN7KiGJ_DCY5xOTy_5eYvCg"

app = Client("skmusicbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
vc = PyTgCalls(app)

@app.on_message(filters.command("start"))
async def start(_, m):
    await m.reply("🎵 SK Music Bot Ready!\nUse /play song name")

@app.on_message(filters.command("play"))
async def play(_, m):
    if len(m.command) < 2:
        return await m.reply("❌ Usage: /play song name")

    query = " ".join(m.command[1:])
    await m.reply("🔎 Searching...")

    ydl_opts = {"format": "bestaudio"}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=False)["entries"][0]
        url = info["url"]
        title = info["title"]

    await vc.join_group_call(
        m.chat.id,
        AudioPiped(url)
    )

    await m.reply(f"▶️ Playing: {title}")

@app.on_message(filters.command("stop"))
async def stop(_, m):
    await vc.leave_group_call(m.chat.id)
    await m.reply("⏹ Stopped")

app.start()
vc.start()
print("Bot Started")
idle()
# restart
