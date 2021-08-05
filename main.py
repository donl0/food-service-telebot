import asyncio
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import time
#from adv_prog import adv_check
#PROXY_URL = 'socks5://138.197.145.103:1080'
loop = asyncio.get_event_loop()#поток
bot =Bot(BOT_TOKEN, parse_mode='HTML')#создание бота. С помощью него делаются запросы
#dp = Dispatcher(bot, loop=loop, storage=MemoryStorage())#диспатчер(жоставщик)
dp = Dispatcher(bot, loop=loop, storage=MemoryStorage())





if __name__ == "__main__":#при импорте этого файла выполняется всё кроме этой функции
    #from adv_prog import adv_check1
    from handlers import dp
    from loop_call import on_startup
    #from loop_call import on_startup
    executor.start_polling(dp, on_startup=on_startup)
    #executor.start_polling(dp)