#6765317557:AAHvuR9iD52G2HaXabZcOBNzlk7vTVYyl2U 토큰
#6732022602 idimport telepot  
from telegram import Update, InlineKeyboardMarkup,InlineKeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

TOKEN = '6765317557:AAHvuR9iD52G2HaXabZcOBNzlk7vTVYyl2U'  # 텔레그램 봇 API
async def start(update : Update, context: ContextTypes.DEFAULT_TYPE) :
    send_msg = "🎄Welcome to the vibrant world of Renewlabs🎄\n🎄          on our official Telegram channel!        🎄" #버튼 상단 메시지 
    btn1 = InlineKeyboardButton(text = "Facebook🪴",url="https://www.facebook.com/renewlabs.official/") # 버튼 설정
    btn2 = InlineKeyboardButton(text = "Instagram🌵",url="https://www.instagram.com/renewlabs.official/")
    btn3 = InlineKeyboardButton(text="X🍃",url="https://twitter.com/renew_labs")
    btn4 = InlineKeyboardButton(text="Discord🎋",url="https://discord.gg/DuVbZHEXpm")
    btn5 = InlineKeyboardButton(text="Link Tree🌲",url="https://linktr.ee/renewlabs")
    mu = InlineKeyboardMarkup(inline_keyboard = [[btn1, btn2],[btn3,btn4],[btn5]]) # 버튼 배치 설정
    await context.bot.send_message(chat_id=update._effective_chat.id, reply_markup=mu,text=send_msg) #비동기식 버튼 전송

if __name__ == '__main__': # 메인 함수
    application = ApplicationBuilder().token(TOKEN).build() # Applicationbuilder 객체 선언
    start_handler = CommandHandler('start',start) # start() 핸들러 생성
    application.add_handler(start_handler) # 핸들러 추가
    application.run_polling() # 폴링 방식으로 실행
