#6765317557:AAHvuR9iD52G2HaXabZcOBNzlk7vTVYyl2U 봇 토큰
#6732022602 봇 id
#-4025133744 그룹방 id
from telegram import Update, InlineKeyboardMarkup,InlineKeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, ChatMemberHandler,CommandHandler

TOKEN = '6765317557:AAHvuR9iD52G2HaXabZcOBNzlk7vTVYyl2U'  # 텔레그램 봇 API
chat_member_count = {}
chat_id = -4025133744 # 테스트 상수
async def start(update : Update, context: ContextTypes.DEFAULT_TYPE) :
    user = update.message.from_user # 봇 탐지를 위해 생성
    message = update.message.new_chat_members # 테스트 메시지
    update.message.new_chat_members
    for member in update.message.new_chat_members:
        if member.is_bot:
            context.bot.kick_chat_member(chat_id=update.effective_chat.id, user_id=member.id)
            context.bot.send_message(chat_id=update.effective_chat.id, text="Bots are not allowed here. Removed bot.")
    #if(user.is_bot):
        #await update.message.reply_text("봇으로 탐지되었습니다.")
        #await context.bot.kick_chat_member(chat_id=update.effective_chat.id, user_id=user.id)
        #return 
    #elif(user.is_bot == False):
        #await update.message.reply_text("환영합니다")
    send_msg = "🎄Welcome to the vibrant world of Renewlabs🎄\n🎄          on our official Telegram channel!            🎄" #버튼 상단 메시지 
    btn1 = InlineKeyboardButton(text = "Facebook🪴",url="https://www.facebook.com/renewlabs.official/") # 버튼 설정
    btn2 = InlineKeyboardButton(text = "Instagram🌵",url="https://www.instagram.com/renewlabs.official/")
    btn3 = InlineKeyboardButton(text="X🍃",url="https://twitter.com/renew_labs")
    btn4 = InlineKeyboardButton(text="Discord🎋",url="https://discord.gg/DuVbZHEXpm")
    btn5 = InlineKeyboardButton(text="Link Tree🌲",url="https://linktr.ee/renewlabs")
    mu = InlineKeyboardMarkup(inline_keyboard = [[btn1, btn2],[btn3,btn4],[btn5]]) # 버튼 배치 설정
    await context.bot.send_message(chat_id=update._effective_chat.id, reply_markup=mu,text=send_msg) #비동기식 버튼 전송
async def new_chat_members(update: Update, context: ContextTypes.DEFAULT_TYPE):
        current_chat_id = update.effective_chat.id
        current_chat_members = await context.bot.get_chat_members_count(current_chat_id)
        for member in update.message.new_chat_members:
            if member.is_bot:
                await update.message.reply_text("Detected a bot in the group.")
            else:
                await start(update, context)  # Call the start function for non-bot users

if __name__ == '__main__': # 메인 함수
    application = ApplicationBuilder().token(TOKEN).build() # Applicationbuilder 객체 선언
    #chat_member_handler = ChatMemberHandler(ChatMemberHandler.MY_CHAT_MEMBER, new_chat_members)
    start_handler = CommandHandler('start',start) # start() 핸들러 생성
    application.add_handler(start_handler) # 핸들러 추가
    #application.add_handler(chat_member_handler) # 핸들러 추가
    application.run_polling() # 폴링 방식으로 실행
