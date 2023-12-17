#6765317557:AAHvuR9iD52G2HaXabZcOBNzlk7vTVYyl2U 토큰
#6732022602 idimport telepot  
import telepot
from telepot.loop import MessageLoop # 봇 구동
from telepot.namedtuple import InlineKeyboardMarkup as MU # 마크업
from telepot.namedtuple import InlineKeyboardButton as BT # 버튼
import time

token = '6765317557:AAHvuR9iD52G2HaXabZcOBNzlk7vTVYyl2U'  # 텔레그램 봇 API 문자열 형태로 입력 (봇 생성 시 확인 가능)
#mc = '6732022602'  # 사용자의 숫자 id (@userinfobot 과의 대화를 통해 확인 가능)
user_chats = {}  # Dictionary to store chat IDs of users who interact with the bot
bot = telepot.Bot(token)  # telepot 모듈의 Bot 함수로 봇 객체 생성하고 token 입력하여 정체성 부여 → bot 으로 이름 명명
should_run = True
bot_running = False  # Track if the bot is already running

def btn_show(chat_id):
    btn1 = BT(text = "1. Hello", callback_data = "1")
    btn2 = BT(text = "2. Bye", callback_data = "2")
    btn3 = BT(text = "3. plus", callback_data = "2")
    mu = MU(inline_keyboard = [[btn1, btn2],[btn3]]) # 가로로 배열
    bot.sendMessage(chat_id, "선택하세요", reply_markup = mu)

def query_ans(msg):
    query_id, _, query_data = telepot.glance(msg, flavor='callback_query')
    query_id = msg["id"] # 버튼 메시지 id
    query_data = msg["data"] # 콜백 데이터
    if query_data == "1": # 콜백 데이터가 1이라면
        bot.answerCallbackQuery(query_id, text = "안녕하세요")
    elif query_data == "2": # 콜백 데이터가 1이라면
        bot.answerCallbackQuery(query_id, text = "안녕히 계세요")

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        bot.sendMessage(chat_id, 'You said "{}"'.format(msg['text']))

bot.message_loop({'chat': btn_show, 'callback_query': query_ans})


#bot.message_loop({'chat': on_chat_message, 'callback_query': query_ans})
#MessageLoop(bot, {'chat': btn_show, "callback_query" : query_ans}).run_as_thread()
# Keep the program running
while True:
    pass
