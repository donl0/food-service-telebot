from main import bot, dp, asyncio
from db_cursor import cursor, conn
import pymysql
from aiogram import types
from config import admin_id
import aioschedule

async def noon_print0():
    print("It's noon!1")
    cursor.execute(f"UPDATE `users` SET `product_get_photo` = '';")
    cursor.execute(f"UPDATE `users` SET `product_get_capt` = '';")
    #point_open_ph
    cursor.execute(f"UPDATE `users` SET `point_open_ph` = '';")
    cursor.execute(f"UPDATE `users` SET `point_open_capt` = '';")

    cursor.execute(f"UPDATE `users` SET `point_close_ph` = '';")
    cursor.execute(f"UPDATE `users` SET `point_close_capt` = '';")

    '''
    cursor.execute("SELECT id_tele FROM user_info WHERE id_tele=0")
    cursor.execute("SELECT id FROM films_list WHERE id=0")
    '''
    



async def noon_print():
    print("It's noon!1")
    #cursor.execute(f"SELECT id_tele from films_list Where id>0")
    cursor.execute(f"UPDATE films_list SET top_24 = 0")
    conn.commit()
async def noon_print2():
    cursor.execute(f"UPDATE films_list SET top_7 = 0")
    conn.commit()

async def noon_print3():
    cursor.execute(f"UPDATE films_list SET top_mounth = 0")
    conn.commit()


async def scheduler():
    #aioschedule.every(15).seconds.do(noon_print0)
    aioschedule.every().days.at("23:59").do(noon_print)
   # aioschedule.every(7).days.at("10:00").do(noon_print2)
   # aioschedule.every(30).days.at("10:00").do(noon_print3)
    #schedule.every().day.at("14:35").do(job, n=i)
    #aioschedule.every(1).days.at("14:43").do(noon_print2)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)



async def on_startup(x):
    asyncio.create_task(scheduler())
