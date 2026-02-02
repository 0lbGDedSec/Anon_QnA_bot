from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import time
import signal
import sys
import logging
import os
import json



BOT_TOKEN = ""     #  <--- Write here your Bot API Key.
ADMIN_ID =  1234567890   #  <--- Write here your Telegram User ID. Writed Admin ID is just an example.

BANS_FILE = os.path.join(os.path.expanduser("~"), "banned_users.json")

BANNED_USERS = set()

def load_bans():
    global BANNED_USERS
    if os.path.exists(BANS_FILE):
        try:
            with open(BANS_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                BANNED_USERS = set(data.get('banned', []))
                print(f"✅ Loaded {len(BANNED_USERS)} banned users")
        except Exception as e:
            print(f"⚠️ Error of uploading banned users: {e}")
            BANNED_USERS = set()
    else:
        BANNED_USERS = set()

def save_bans():
    try:
        data = {'banned': list(BANNED_USERS)}
        with open(BANS_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        logging.error(f"Error of saving banned users: {e}")

load_bans()

# ===== Starting =====

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text(
        "👋 Hi! Write me some messages, and I'll sent it to an owner.\n"
        "Commands: /help (Only for admins)"
    )
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"New user! \n"
    )

# ===== Command list =====

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = """
📋 Commands:
/ban ID - Ban
/unban ID - Unban
/reply ID text - reply with text
/banned - List of banned users
"""
    await update.message.reply_text(help_text)

# ===== Message processing =====

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    user_id = user.id
    
    if user_id in BANNED_USERS:
        await update.message.reply_text("❌ You are banned!")
        return
    
    text = update.message.text
    msg_anon = f"New message! \n\n" \
        f"🆔 ID: {user_id}\n\n" \
        f"💬 {text} " 

    await context.bot.send_message(chat_id=ADMIN_ID, text=msg_anon)
    await update.message.reply_text("✅ Sent!")


async def forward_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    user_id = user.id
    
    if user_id in BANNED_USERS:
        await update.message.reply_text("❌ You are banned!")
        return
    
    photo = update.message.photo[-1]  
    caption = update.message.caption or "📸 Photo from user."
    
    msg_anon = f"New message! \n\n" \
        f"🆔 ID: {user_id}\n\n" \
        f"📸 Photo " 
    
    await context.bot.send_photo(
        chat_id=ADMIN_ID,
        photo=photo.file_id,
        caption=msg_anon if not caption else f"{msg_anon}\n\n💭 {caption}"
    )
    await update.message.reply_text("✅ Photo was sent!")



async def forward_video(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    user_id = user.id
    
    if user_id in BANNED_USERS:
        await update.message.reply_text("❌ You are banned!")
        return
    
    video = update.message.video
    caption = update.message.caption or "🎥 Video from user."
    
    msg_anon = f"New message! \n\n" \
        f"🆔 ID: {user_id}\n\n" \
        f"🎥 Video "
    
    await context.bot.send_video(
        chat_id=ADMIN_ID,
        video=video.file_id,
        caption=msg_anon if not caption else f"{msg_anon}\n\n💭 {caption}"
    )
    await update.message.reply_text("✅ Video was sent!")



async def forward_voice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    user_id = user.id
    
    if user_id in BANNED_USERS:
        await update.message.reply_text("❌ You are banned!")
        return
    
    voice = update.message.voice
    

    msg_anon = f"New message! \n\n" \
        f"🆔 ID: {user_id}\n\n" \
        f"🎤 Voice message " 
    
    await context.bot.send_voice(
        chat_id=ADMIN_ID,
        voice=voice.file_id,
        caption=msg_anon
    )

    await update.message.reply_text("✅ Voice message was sent!")



async def forward_video_note(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    user_id = user.id
    
    if user_id in BANNED_USERS:
        await update.message.reply_text("❌ You are banned!")
        return
    
    video_note = update.message.video_note

    msg_anon = f"New message! \n\n" \
        f"🆔 ID: {user_id}\n\n" \
        f"🎬 Video message "
    
    await context.bot.send_video_note(
        chat_id=ADMIN_ID,
        video_note=video_note.file_id
    )

    await context.bot.send_message(chat_id=ADMIN_ID, text=msg_anon)
    await update.message.reply_text("✅ Video message was sent!")





# ===== Admin commands =====

async def admin_ban(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user.id != ADMIN_ID:
        return
    try:
        user_id = int(context.args[0])
        BANNED_USERS.add(user_id)
        save_bans()
        await update.message.reply_text(f"✅ Was banned: {user_id}")
    except:
        await update.message.reply_text("❌ /ban 123456")

async def admin_unban(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user.id != ADMIN_ID:
        return
    
    try:
        user_id = int(context.args[0])
        BANNED_USERS.discard(user_id)
        save_bans()
        await update.message.reply_text(f"✅ Was unbanned: {user_id}")
    except:
        await update.message.reply_text("❌ /unban 123456")

async def admin_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user.id != ADMIN_ID:
        return
    
    try:
        user_id = int(context.args[0])
        response = " ".join(context.args[1:])
        await context.bot.send_message(chat_id=user_id, text=f"💬 Reply:\n{response}")
        await update.message.reply_text(f"✅ Reply was sent: {user_id}")
    except:
        await update.message.reply_text("❌ /reply 123456 текст")


async def admin_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user.id != ADMIN_ID:
        return
    
    if not BANNED_USERS:
        await update.message.reply_text("✅ No banned users.")
    else:
        lst = "\n".join([str(uid) for uid in sorted(BANNED_USERS)])
        await update.message.reply_text(f"🚫 Banned Users ({len(BANNED_USERS)}):\n{lst}")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def signal_handler(sig, frame):
    logging.info('Got command to log out. Rebooting...')
    sys.exit(0)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    # ===== Command Processing =====
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("ban", admin_ban))
    app.add_handler(CommandHandler("unban", admin_unban))
    app.add_handler(CommandHandler("reply", admin_reply))
    app.add_handler(CommandHandler("banned", admin_list))
    
    # ===== Message Processing =====
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))
    app.add_handler(MessageHandler(filters.PHOTO, forward_photo))
    app.add_handler(MessageHandler(filters.VIDEO & ~filters.ANIMATION, forward_video))
    app.add_handler(MessageHandler(filters.VOICE, forward_voice))
    app.add_handler(MessageHandler(filters.VIDEO_NOTE, forward_video_note))
    
    print("🚀The bot is running!")
    app.run_polling()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    while True:
        try:
            main()
        except Exception as e:
            logging.error(f'The bot crashed with an error: {e}. Restart of the bot in 5 seconds...')
            time.sleep(5)
