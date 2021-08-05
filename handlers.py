from main import bot, dp, asyncio
from aiogram import types
from config import admin_id, keys_acc
from config import admin_id
import pymysql
#from keyboards import start_kerboard, just_back_ganre_keybard, clear_keyboard, movie_keyboard, main_m_keyboard_2, Genre_keyboard, next_step_keyboard, years_keyboard, comment_keyboard, next_step_keyboard_years, filter_keyboard, just_back_yrarf_keybard, just_back_k, info_keyb, question_keyb, main_m_keyboard, box_keyboard, top_keyboard, my_prof_keyboard, search_keyboard, again_keyboard, comm_keyboard, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from keyboards import way_search_to_spoiled, sklad_keyb, point_chose, way_search_to_sklad, prihod_uh_keyb, rassilka_k, rassilka_read_k, prof_k, ReplyKeyboardMarkup, point_grajd, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from states import OrderDataUser, FSMContext, State

from db_cursor import cursor, conn
from exec_comm import client
from datetime import datetime
'''
@dp.message_handler(content_types=types.ContentTypes.ANY)
async def stasr(message: types.Message, state: FSMContext):
   
    user_name=message['from']['username']
    id_person=message['from']['id']
    #print(message)
    mess = message.text
    #getFullChat
  #  FullChat = await bot.get_chat('@misha_anime1')
    #print(FullChat)
    FullChat2 = await bot.get_chat_administrators('@misha_anime1')
    print('------------')
    for i in FullChat2:
        print(i)
    print('------------')
   # FullChat2 = await bot.get_chat_members_count('@dawg_chat')
    print(FullChat2)
    #print(message)
   # chat_id1 = message.ChatFull()
    #print(chat_id1)
    
  #  huy1 = types.Message.
   # huy = types.message.ChatFull()
   # print(huy1)
   # print(huy)
    print(message)
    print('--------------------------')
'''
@dp.message_handler(state=[OrderDataUser.sklad_keyb_st, OrderDataUser.state_photo_get, OrderDataUser.prih_uh_st, OrderDataUser.st_prof_keyb, OrderDataUser.st_get_new_fil, OrderDataUser.prihod_make_st, OrderDataUser.uh_make_st, OrderDataUser.product_sp2, OrderDataUser.product_sklad2], text='Назад ↩️')
async def product_button_spoiled_step3(message: types.Message):
    print('зашёл')
    id_person= message['from']['id']
    mess=message.text
    main_k = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    item_change_point = InlineKeyboardButton(text='Изменить точку')
    spoiled = InlineKeyboardButton(text='Добавить списывание продукта в таблицу')
    item_sklad_point = InlineKeyboardButton(text='Склад')
    item_prihod_uhod = InlineKeyboardButton(text='Приход/уход')
    item_who_read = InlineKeyboardButton(text='Посмотреть кто прочитал рассылку')
    item_prof = InlineKeyboardButton(text='Профиль')
    main_k.add(item_change_point, spoiled, item_sklad_point, item_prihod_uhod, item_who_read, item_prof)
    if id_person in admin_id:

        item_rass = InlineKeyboardButton(text='Рассылка')
        main_k.add(item_rass)

    await bot.send_message(chat_id=id_person, text='Гравное меню', reply_markup=main_k)


@dp.message_handler(commands=['start'], state="*")
async def stasr(message: types.Message, state: FSMContext):
   
    user_name=message['from']['username']
    id_person=message['from']['id']

    cursor.execute(f"SELECT tele_id FROM users WHERE tele_id='{id_person}'")
    enter_n = cursor.fetchone()
    #Ke12Pudge#$FEED10
    print(enter_n)
    main_k = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    item_change_point = InlineKeyboardButton(text='Изменить точку')
    spoiled = InlineKeyboardButton(text='Добавить списывание продукта в таблицу')
    item_sklad_point = InlineKeyboardButton(text='Склад')
    item_prihod_uhod = InlineKeyboardButton(text='Приход/уход')
    item_who_read = InlineKeyboardButton(text='Посмотреть кто прочитал рассылку')
    item_prof = InlineKeyboardButton(text='Профиль')
    main_k.add(item_change_point, spoiled, item_sklad_point, item_prihod_uhod, item_who_read, item_prof)
    if enter_n==None:
        await bot.send_message(chat_id=id_person, text='Здарова😁\nЯ должен быть уверен что ты не посторонний человек, чтобы предоставлять услуги\nПоэтому введи свой ключ')

        await OrderDataUser.access_checking.set()
    else:
        if id_person in admin_id:

            item_rass = InlineKeyboardButton(text='Рассылка')
            main_k.add(item_rass)
        cursor.execute(f"SELECT enter_name, point_today, key_access FROM users WHERE tele_id='{id_person}';")
        point = cursor.fetchone()

        await bot.send_message(chat_id=id_person, text='Здравствуй, '+str(point[0])+'\nВыбранная ночка: '+str(point[1])+'\n', reply_markup=main_k)

@dp.message_handler(state = OrderDataUser.access_checking, content_types=types.ContentTypes.TEXT)
async def genres_adding(message: types.Message, state: FSMContext):
    #user_data = await state.get_data()
    id_person= message['from']['id']
    mess=message.text
    user_name=message['from']['username']
    if mess in keys_acc:
        await bot.send_message(chat_id=id_person, text='Красава ключ верный!')
        #изменить стейт
        cursor.execute(f"INSERT INTO `users` (`id`, `user_name`, `enter_name`, `tele_id`, `key_access`, `product_get_photo`, `product_get_capt`, `mail_check`, `point_open_ph`, `point_open_capt`, `point_close_ph`, `point_close_capt`, `point_today`, `name_table_spis`, `name_table_postavka`) VALUES (NULL, '{user_name}', '', '{id_person}', '{mess}', '', '', '0', '', '', '', '', '', '', '');")
        if mess=='Ke12Pudge#$FEED10':
            cursor.execute(f"UPDATE `users` SET `name_table_spis` = 'spis_table' WHERE tele_id = {id_person};")
        conn.commit()
        await bot.send_message(chat_id=id_person, text='Теперь введи своё фио, чтобы сотрудники могли тебя опознать')
        await OrderDataUser.name_create.set()
    else:
        await bot.send_message(chat_id=id_person, text='Неверный ключ...')
    

@dp.message_handler(state = OrderDataUser.name_create, content_types=types.ContentTypes.TEXT)
async def genres_adding(message: types.Message, state: FSMContext):
    #user_data = await state.get_data()
    id_person= message['from']['id']
    mess=message.text
    cursor.execute(f"UPDATE `users` SET `enter_name` = '{mess}' WHERE `tele_id` = {id_person};")
    conn.commit()

    await state.finish()
#point_chose
    await bot.send_message(chat_id=id_person, text='Выбери сегодняшнюю точку', reply_markup=point_chose)


   # await bot.send_message(chat_id=id_person, text='Всё меню открыто для тебя!', reply_markup=main_k)

@dp.callback_query_handler(text='i read', state="*")
async def del_adv(call: types.CallbackQuery):
    id_person=call.from_user['id']
    cursor.execute(f"UPDATE `users` SET `mail_check` = '1' WHERE tele_id = {id_person};")
    conn.commit()
    print(call)
    print(call.message)
    try:
        await bot.edit_message_text(chat_id=id_person, message_id=call.message.message_id, text=call.message.text)
    except:
        await bot.edit_message_caption(chat_id=id_person, message_id=call.message.message_id, caption=call.message.caption)
    await bot.answer_callback_query(callback_query_id=call.id,text='Прочитал', show_alert=True)


@dp.message_handler(state="*", text='Рассылка')
async def genres_adding(message: types.Message, state: FSMContext):
    id_person= message['from']['id']
    mess=message.text
    if id_person in admin_id:
        await bot.send_message(chat_id=id_person, text='Выбери способ рассылки', reply_markup=rassilka_k)
@dp.callback_query_handler(text='adv_mass_send1', state="*")
async def del_adv(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.from_user['id'], text='Отправь фотографию с описанием к ней')
    await OrderDataUser.adv_ph_c_wait2.set()
    
    

@dp.message_handler(state=OrderDataUser.adv_ph_c_wait2, content_types=types.ContentTypes.PHOTO )
async def genres_adding(message: types.Message, state: FSMContext):
    caption = message.caption
    id_person= message['from']['id']
    pic = message['photo'][-1]['file_id']
    cursor.execute(f"SELECT key_access FROM users WHERE tele_id='{id_person}';")
    key = cursor.fetchone()[0]

    cursor.execute(f"SELECT tele_id FROM users WHERE key_access='{key}';")
    all_users=cursor.fetchall()
    print(all_users)
    for i in all_users:
        cursor.execute(f"UPDATE `users` SET `mail_check` = '0' WHERE tele_id = {i[0]};")
        conn.commit()
       # await bot.send_photo(chat_id=i, photo=pic, caption=caption, reply_markup=rassilka_read_k)
        try:
            await bot.send_photo(chat_id=i[0], photo=pic, caption=caption, reply_markup=rassilka_read_k)
            #await bot.send_photo(chat_id=i[0], photo=pic, caption=caption, reply_markup=rassilka_read_k)
        except:
            print('не вышло отправить рассылку')
    await state.finish()
@dp.callback_query_handler(text='just_mes', state="*")
async def del_adv(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.from_user['id'], text='Отправь сообщение')
    await OrderDataUser.st_get_mes_to_rassilka.set()

@dp.message_handler(state=OrderDataUser.st_get_mes_to_rassilka, content_types=types.ContentTypes.TEXT )
async def genres_adding(message: types.Message, state: FSMContext):
    caption = message.text
    id_person= message['from']['id']
  #  pic = message['photo'][-1]['file_id']
    cursor.execute(f"SELECT key_access FROM users WHERE tele_id='{id_person}';")
    key = cursor.fetchone()[0]


    cursor.execute(f"SELECT tele_id FROM users WHERE key_access='{key}';")
    all_users=cursor.fetchall()
    print(all_users)
    print(all_users[0][0])
    print(all_users[1][0])
    for i in all_users:
        
        cursor.execute(f"UPDATE `users` SET `mail_check` = '0' WHERE tele_id = {i[0]};")
        conn.commit()
        try:
            await bot.send_message(chat_id=i[0], text='⚡️⚡️⚡️ '+str(caption), reply_markup=rassilka_read_k)
        except:
            print('рассылка не вышла')
        '''
       # await bot.send_photo(chat_id=i, photo=pic, caption=caption, reply_markup=rassilka_read_k)
        try:
            await bot.send_message(chat_id=i, text=caption, reply_markup=rassilka_read_k)
        except:
            print('не вышло отправить рассылку')
        '''
    await state.finish()
        
#just_mes


@dp.message_handler(state="*", text=['Профиль', 'Добавить списывание продукта в таблицу', 'Изменить точку', 'Занести значение в склад','Склад','Добавить фотографию о принятии поставки', 'Посмотреть фотографии с принятием поставки', 'Сделать фотографию прихода', 'Сделать фотографию ухода', 'Приход/уход', 'Посмотреть фотографии прихода', 'Посмотреть фотографии ухода', 'Посмотреть кто прочитал рассылку'])
async def genres_adding(message: types.Message, state: FSMContext):
    id_person= message['from']['id']
    mess=message.text
    if mess=='Добавить списывание продукта в таблицу':

    #item_but_spoiled
        await bot.send_message(chat_id=id_person, text='Выберите способ поиска продукта',reply_markup=way_search_to_spoiled)
        await OrderDataUser.after_search_sp.set()
    elif mess=='Профиль':
        cursor.execute(f"SELECT enter_name, point_today, key_access FROM users WHERE tele_id='{id_person}';")
        point = cursor.fetchone()
        print(point)
        if point[2]=='Ke12Pudge#$FEED10':
            db_spis='https://docs.google.com/spreadsheets/d/1scplaO3iwa4ODsO1JlP9NuDP-hhQ6eFbVwXGEhTvnCE/edit#gid=1004098019'
            db_sklad='https://docs.google.com/spreadsheets/d/1AZS2RgTrrJf_Y73rED8VG0F5P04K6CSIiuDv6X-jIUk/edit#gid=914056915'

        await bot.send_message(chat_id=id_person, text='Здравствуй, '+str(point[0])+' 👏\nВыбранная ночка: '+str(point[1])+' ⛩\n\nСсылка на exel списывания товаров:🗓  '+str(db_spis)+'\nСсылка на exel поставка склада:📦  '+str(db_sklad), reply_markup=prof_k)
        await OrderDataUser.st_prof_keyb.set()
    
    elif mess=='Изменить точку':
        await bot.send_message(chat_id=id_person, text='Выбери сегодняшнюю точку', reply_markup=point_chose)
    elif mess=='Склад':
        await bot.send_message(chat_id=id_person, text='Смотри склад', reply_markup=sklad_keyb)
        await OrderDataUser.sklad_keyb_st.set()
    elif mess=='Занести значение в склад':
        await bot.send_message(chat_id=id_person, text='Выберите способ поиска продукта🌯',reply_markup=way_search_to_sklad)
    
        await OrderDataUser.after_search_sklad.set()
    elif mess=='Добавить фотографию о принятии поставки':
        await bot.send_message(chat_id=id_person, text='Отправь фотографию и надпись вместе(Надпись необходима только первой фотографии в день), я сохраню это\nЧтобы прикрепить ещё одно фотографию - прото повтори процедуру')
        await OrderDataUser.state_photo_get.set()
    elif mess=='Посмотреть фотографии с принятием поставки':
        cursor.execute(f"SELECT key_access FROM users WHERE tele_id ={id_person};")
        key=cursor.fetchone()[0]
        print(key)
        cursor.execute(f"SELECT enter_name, product_get_photo, product_get_capt FROM users WHERE key_access='{key}';")
        send_info=cursor.fetchall()
        print(send_info)
        send_info=list(send_info)
        #print(send_info)
        for all_info in send_info:
            enter_name1=all_info[0]
            photo = all_info[1]
            string=all_info[2]
            photo=photo.split('^')
            string=string
            while len(photo)>9:
                try:
                    del photo[0]
                except:
                    pass
           # media =[types.InputMediaVideo('BAACAgIAAxkBAAJ-4GBmL3wkZcB1XqdO3Igz4tsxIW76AALYDwACSE0xS_zsiWjpdoY5HgQ', caption=string)]
            
            media=[types.InputMediaPhoto(photo[0], caption=str(enter_name1)+':\n'+str(string))]
            del photo[0]
            for i in photo:
                media.append(types.InputMediaPhoto(i))
            try:
                await bot.send_media_group(chat_id=id_person,media=media)
            except:
                pass
    elif mess=='Приход/уход':
        await bot.send_message(chat_id=id_person, text='Открыл', reply_markup=prihod_uh_keyb)
        await OrderDataUser.prih_uh_st.set()
        #prihod_uh_keyb
    elif mess=='Сделать фотографию прихода':
        await bot.send_message(chat_id=id_person, text='Отправь фотографию и надпись вместе(Надпись необходима только первой фотографии в день), я сохраню это\nЧтобы прикрепить ещё одно фотографию - прото повтори процедуру')
        await OrderDataUser.prihod_make_st.set()
    elif mess=='Посмотреть фотографии прихода':
        cursor.execute(f"SELECT key_access FROM users WHERE tele_id ={id_person};")
        key=cursor.fetchone()[0]
        print(key)
        cursor.execute(f"SELECT enter_name, point_open_ph, point_open_capt FROM users WHERE key_access='{key}';")
        send_info=cursor.fetchall()
        print(send_info)
        send_info=list(send_info)
        #print(send_info)
        for all_info in send_info:
            enter_name1=all_info[0]
            photo = all_info[1]
            string=all_info[2]
            photo=photo.split('^')
            while len(photo)>9:
                try:
                    del photo[0]
                except:
                    pass
           
            string=string
           
           # media =[types.InputMediaVideo('BAACAgIAAxkBAAJ-4GBmL3wkZcB1XqdO3Igz4tsxIW76AALYDwACSE0xS_zsiWjpdoY5HgQ', caption=string)]
            
            media=[types.InputMediaPhoto(photo[0], caption=str(enter_name1)+':\n'+str(string))]
            del photo[0]
            for i in photo:
                media.append(types.InputMediaPhoto(i))
            try:
                await bot.send_media_group(chat_id=id_person,media=media)
            except:
                print('не отправил')
    elif mess=='Посмотреть фотографии ухода':
        cursor.execute(f"SELECT key_access FROM users WHERE tele_id ={id_person};")
        key=cursor.fetchone()[0]
        print(key)
        cursor.execute(f"SELECT enter_name, point_close_ph, point_close_capt FROM users WHERE key_access='{key}';")
        send_info=cursor.fetchall()
        print(send_info)
        send_info=list(send_info)
        #print(send_info)
        for all_info in send_info:
            enter_name1=all_info[0]
            photo = all_info[1]
            string=all_info[2]
            photo=photo.split('^')
            string=string
            while len(photo)>9:
                try:
                    del photo[0]
                except:
                    pass
        # media =[types.InputMediaVideo('BAACAgIAAxkBAAJ-4GBmL3wkZcB1XqdO3Igz4tsxIW76AALYDwACSE0xS_zsiWjpdoY5HgQ', caption=string)]
            
            media=[types.InputMediaPhoto(photo[0], caption=str(enter_name1)+':\n'+str(string))]
            del photo[0]
            for i in photo:
                media.append(types.InputMediaPhoto(i))
            try:
                await bot.send_media_group(chat_id=id_person,media=media)
            except:
                print('не отправил')
    elif mess=='Сделать фотографию ухода':
        await bot.send_message(chat_id=id_person, text='Отправь фотографию и надпись вместе(Надпись необходима только первой фотографии в день), я сохраню это\nЧтобы прикрепить ещё одно фотографию - прото повтори процедуру')
        await OrderDataUser.uh_make_st.set()

    elif mess=='Посмотреть кто прочитал рассылку':
        cursor.execute(f"SELECT key_access FROM users WHERE tele_id ={id_person};")
        key=cursor.fetchone()[0]
       # print(key)
        cursor.execute(f"SELECT enter_name, mail_check FROM users WHERE key_access='{key}';")
        send_info=cursor.fetchall()
        print(send_info)
        string=''
        for people_name,check_or_not in send_info:
          
            if check_or_not==1:
                string+=str(people_name)+' ✅\n'
            else:
                string+=str(people_name)+' ❌\n'
        await bot.send_message(chat_id=id_person, text=string)


@dp.message_handler(state=OrderDataUser.uh_make_st, content_types=types.ContentTypes.PHOTO)
async def photo_get(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    id_person= message['from']['id']
    mess=message.text
    pic = message['photo'][-1]['file_id']
    try:
        caption = message.caption

        
        if 	'^' in caption:
            await bot.send_message(chat_id=id_person, text='Не используй ^...')
        else:
            cursor.execute(f'SELECT point_close_ph FROM users WHERE tele_id = {id_person};')
            link_photos=cursor.fetchone()[0]
            if link_photos=='':
                link_photos=pic
            else:
                link_photos=str(link_photos)+'^'+pic
            cursor.execute(f"UPDATE `users` SET `point_close_ph` = '{link_photos}' WHERE tele_id = {id_person};")

            cursor.execute(f'SELECT point_close_capt FROM users WHERE tele_id = {id_person};')
            text_capt=cursor.fetchone()[0]
            if text_capt=='':
                text_capt=caption
            else:
                text_capt=str(text_capt)+'\n\n'+str(caption)
            cursor.execute(f"UPDATE `users` SET `point_close_capt` = '{text_capt}' WHERE tele_id = {id_person};")
            conn.commit()
            await bot.send_message(chat_id=id_person, text='Сохранил')
    except:
        cursor.execute(f'SELECT point_close_ph FROM users WHERE tele_id = {id_person};')
        link_photos=cursor.fetchone()[0]
        if link_photos=='':
            link_photos=pic
        else:
            link_photos=str(link_photos)+'^'+pic
        cursor.execute(f"UPDATE `users` SET `point_close_ph` = '{link_photos}' WHERE tele_id = {id_person};")
        conn.commit()
        await bot.send_message(chat_id=id_person, text='Сохранил')

@dp.message_handler(state=OrderDataUser.prihod_make_st, content_types=types.ContentTypes.PHOTO)
async def photo_get(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    id_person= message['from']['id']
    mess=message.text
    pic = message['photo'][-1]['file_id']
    try:
        caption = message.caption

        
        if 	'^' in caption:
            await bot.send_message(chat_id=id_person, text='Не используй ^...')
        else:
            cursor.execute(f'SELECT point_open_ph FROM users WHERE tele_id = {id_person};')
            link_photos=cursor.fetchone()[0]
            if link_photos=='':
                link_photos=pic
            else:
                link_photos=str(link_photos)+'^'+pic
            cursor.execute(f"UPDATE `users` SET `point_open_ph` = '{link_photos}' WHERE tele_id = {id_person};")

            cursor.execute(f'SELECT point_open_capt FROM users WHERE tele_id = {id_person};')
            text_capt=cursor.fetchone()[0]
            if text_capt=='':
                text_capt=caption
            else:
                text_capt=str(text_capt)+'\n\n'+str(caption)
            cursor.execute(f"UPDATE `users` SET `point_open_capt` = '{text_capt}' WHERE tele_id = {id_person};")


            conn.commit()
            await bot.send_message(chat_id=id_person, text='Сохранил')
    except:
        cursor.execute(f'SELECT point_open_ph FROM users WHERE tele_id = {id_person};')
        link_photos=cursor.fetchone()[0]
        if link_photos=='':
            link_photos=pic
        else:
            link_photos=str(link_photos)+'^'+pic
        cursor.execute(f"UPDATE `users` SET `point_open_ph` = '{link_photos}' WHERE tele_id = {id_person};")
        conn.commit()
        await bot.send_message(chat_id=id_person, text='Сохранил')

@dp.message_handler(state=OrderDataUser.state_photo_get, content_types=types.ContentTypes.PHOTO)
async def photo_get(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    id_person= message['from']['id']
    mess=message.text
    pic = message['photo'][-1]['file_id']
    try:
        caption = message.caption

        
        if 	'^' in caption:
            await bot.send_message(chat_id=id_person, text='Не используй ^...')
        else:
            cursor.execute(f'SELECT product_get_photo FROM users WHERE tele_id = {id_person};')
            link_photos=cursor.fetchone()[0]
            if link_photos=='':
                link_photos=pic
            else:
                link_photos=str(link_photos)+'^'+pic
            cursor.execute(f"UPDATE `users` SET `product_get_photo` = '{link_photos}' WHERE tele_id = {id_person};")

            cursor.execute(f'SELECT product_get_capt FROM users WHERE tele_id = {id_person};')
            text_capt=cursor.fetchone()[0]
            if text_capt=='':
                text_capt=caption
            else:
                text_capt=str(text_capt)+'\n\n'+str(caption)
            cursor.execute(f"UPDATE `users` SET `product_get_capt` = '{text_capt}' WHERE tele_id = {id_person};")


            conn.commit()
            await bot.send_message(chat_id=id_person, text='Сохранил')
    except:
        cursor.execute(f'SELECT product_get_photo FROM users WHERE tele_id = {id_person};')
        link_photos=cursor.fetchone()[0]
        if link_photos=='':
            link_photos=pic
        else:
            link_photos=str(link_photos)+'^'+pic
        cursor.execute(f"UPDATE `users` SET `product_get_photo` = '{link_photos}' WHERE tele_id = {id_person};")
        conn.commit()
        await bot.send_message(chat_id=id_person, text='Сохранил')
#but_spoiled
@dp.callback_query_handler(state="*", text='but_spoiled')
async def product_search_in_buttons_spoiled(call: types.CallbackQuery, state: FSMContext):
    capt = call.message['caption']
    id_person=call.from_user['id']

    print('СПОИЛД')
    #cursor.execute(f"SELECT name_table_spis FROM users WHERE tele_id={id_person} ")
   # table_name =cursor.fetchone()[0]
   # sheet = client.open(table_name).sheet1
    sheet = sheet_num('spis', id_person)
    all_products = sheet.col_values(1)
    #print(all_products)
    del all_products[0]
    item_back = InlineKeyboardButton(text='Назад ↩️', callback_data='go_back')
    spoiled2 = InlineKeyboardMarkup(row_width=3, resize_keyboard=True)
    spoiled2.add(item_back)
    check=True
    for prod in all_products:
        

        item_prod = InlineKeyboardButton(text=prod, callback_data=prod)
        if check==True:
            spoiled2.add(item_prod)
            check=False
        else:
            if len(prod)>35:
                pass
            else:
                spoiled2.insert(item_prod)
            
    await bot.send_message(chat_id=id_person, text='Выбери продукт', reply_markup=spoiled2)

    await state.update_data(enumirate=all_products)
    await OrderDataUser.product_sp1.set()






@dp.message_handler(state=OrderDataUser.product_sp2, content_types=types.ContentTypes.TEXT)
async def product_button_spoiled_step3(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    id_person= message['from']['id']
    mess=message.text
   # cursor.execute(f"SELECT name_table_spis FROM users WHERE tele_id={id_person} ")
    #table_name =cursor.fetchone()[0]
    #sheet = client.open(table_name).sheet1
    sheet = sheet_num('spis', id_person)
    all_products = sheet.row_values(1)

    current_datetime = datetime.now()
    print(current_datetime.year)            # 2019
    print(current_datetime.month)           # 12
    print(current_datetime.day) 
    day=current_datetime.day
    mounth=current_datetime.month
    mass_date=[day, mounth]
    num_=0
    for i in mass_date:
        if len(str(i))==1:
            i='0'+str(i)
            mass_date[num_]=i
        num_+=1
    string=str(mass_date[0])+'.'+str(mass_date[1])+'.'+str(str(current_datetime.year)[-2:])
   # cursor.execute(f"SELECT name_table_spis FROM users WHERE tele_id={id_person} ")
   # table_name =cursor.fetchone()[0]
    sheet = sheet_num('spis', id_person)
    
    all_products = sheet.row_values(1)
    num2=0
    print(string)
    for i in all_products:
        num2+=1
        if i==string:
            break
    print(user_data['enumirate'], num2)
    sheet.update_cell(user_data['enumirate'], num2, mess)
    await bot.send_message(chat_id=id_person, text='Внёс изменение в таблицу')


#after_search_sp
@dp.inline_handler(lambda query: len(query.query) > 0, state=OrderDataUser.after_search_sp)
async def query_text(query):
    #print('INL')
    print(query)
    id_person=query.from_user['id']
    print(id_person)
    film_name_by_inline = query.query.lower() #То что вводит пользователь при обращении
    print(film_name_by_inline)
    try:
       
     #   cursor.execute(f"SELECT name_table_spis FROM users WHERE tele_id={id_person};")
      #  table_name =cursor.fetchone()[0]
      #  sheet = client.open(table_name).sheet1
        sheet = sheet_num('spis', id_person)
        all_products = sheet.col_values(1)
        #print(all_products)
        del all_products[0]
    except:
        print("ну ошибка типо")
    fav_products = []
    for i in all_products:
        if film_name_by_inline in i.lower():
            print('добавил '+str(i))
            fav_products.append(i)
    
    results = []
   # print(film_list)
    for i in range(0, len(fav_products)):
        single_msg = types.InlineQueryResultArticle(
            id=fav_products[i],
            title=fav_products[i],
            input_message_content=types.InputTextMessageContent(message_text=fav_products[i]), #добавляем ссылку на фильм в чат
            #description='Year: ' + str(film_list[i][1]) + ' \n' + 'Rating: ' + str(film_list[i][2]),
            #thumb_url=film_list[i][5],
        )
        results.append(single_msg)
    #await OrderDataUser.search_spoiled_str.set()

    await bot.answer_inline_query(query.id, results)


@dp.message_handler(state=OrderDataUser.after_search_sp, content_types=types.ContentTypes.TEXT)
async def product_button_spoiled_step3(message: types.Message, state: FSMContext):
    print('зашёл')
    id_person= message['from']['id']
    mess=message.text
    user_data = await state.get_data()

    #cursor.execute(f"SELECT name_table_spis FROM users WHERE tele_id={id_person} ")
    #table_name =cursor.fetchone()[0]
    #sheet = client.open(table_name).sheet1
    sheet = sheet_num('spis', id_person)
    all_products = sheet.col_values(1)
    #print(all_products)
    del all_products[0]

    await bot.send_message(chat_id=id_person, text='Введи значение которое положить в ячейку')
    num=0
    for i in all_products:
        num+=1
        if mess==i:
            print(str(mess)+'+'+str(i))
            num+=1

            break
    await state.update_data(enumirate=num)
    await OrderDataUser.product_sp2.set()


#product_sp2
#go_backsklad_keyb_st


@dp.message_handler(state="*", text=['Изменить ФИО'])
async def genres_adding(message: types.Message, state: FSMContext):
    id_person= message['from']['id']
    mess=message.text
    await bot.send_message(chat_id=id_person, text='введи новые данные')
    await OrderDataUser.st_get_new_fil.set()
@dp.message_handler(state=OrderDataUser.st_get_new_fil, content_types=types.ContentTypes.TEXT)
async def photo_get(message: types.Message):
    id_person= message['from']['id']
    mess=message.text
    cursor.execute(f"UPDATE `users` SET `enter_name` = '{mess}' WHERE tele_id = {id_person};")
    await bot.send_message(chat_id=id_person,text='Обновил')
    await OrderDataUser.st_prof_keyb.set()




@dp.callback_query_handler(text='go_back', state = [OrderDataUser.product_sp1, OrderDataUser.search_spoiled_str, OrderDataUser.product_sp2])
async def product_button_spoiled_step2(call):
    id_person=call.from_user['id']
    await bot.send_message(chat_id=id_person, text='Выберите способ поиска продукта',reply_markup=way_search_to_spoiled)
    await OrderDataUser.after_search_sp.set()

@dp.callback_query_handler(text='go_back', state = [OrderDataUser.product_sklad1, OrderDataUser.search_sklad_str, OrderDataUser.product_sklad2])
async def product_button_spoiled_step2(call):
    id_person=call.from_user['id']
    await bot.send_message(chat_id=id_person, text='Выберите способ поиска продукта',reply_markup=way_search_to_sklad)
    await OrderDataUser.after_search_sp.set()


#@dp.callback_query_handler(text='go_back', state = OrderDataUser.after_search_sp
#async def genres_adding(message: types.Message):




def sheet_num(table_type, id_user):
    cursor.execute(f"SELECT key_access FROM users WHERE tele_id={id_user};")
    key=cursor.fetchone()[0]
    if key =='Ke12Pudge#$FEED10':
        if table_type=='spis':
            sheet = client.open('spis_table')
            cursor.execute(f"SELECT point_today FROM users WHERE tele_id={id_user};")
            point=cursor.fetchone()[0]
            sheet = sheet.worksheet(point)
            
        elif table_type=='sklad':
            sheet = client.open('sklad_table')
            cursor.execute(f"SELECT point_today FROM users WHERE tele_id={id_user};")
            point=cursor.fetchone()[0]
            sheet = sheet.worksheet(point)
            
        return sheet
#sheet = client.open(table_name).sheet1

#-----------------------после всего для склада
@dp.callback_query_handler(lambda c: True, state = OrderDataUser.product_sklad1)
async def product_button_spoiled_step2(call, state: FSMContext):
    user_data = await state.get_data()
    mess = call.data
    id_person=call.from_user['id']

    await bot.answer_callback_query(callback_query_id=call.id,text=mess+' был выбран', show_alert=False)
    await bot.send_message(chat_id=id_person, text='Введи значение которое положить в ячейку')
    num=0
    for i in user_data['enumirate']:
        num+=1
        if mess==i:
            print(str(mess)+'+'+str(i))
            num+=1

            break
    await state.update_data(enumirate=num)
    await OrderDataUser.product_sklad2.set()


#-----------------------после всего для просрочки
@dp.callback_query_handler(lambda c: True, state = OrderDataUser.product_sp1)
async def product_button_spoiled_step2(call, state: FSMContext):
    user_data = await state.get_data()
    mess = call.data
    id_person=call.from_user['id']

    await bot.answer_callback_query(callback_query_id=call.id,text=mess+' был выбран', show_alert=False)
    await bot.send_message(chat_id=id_person, text='Введи значение которое положить в ячейку')
    num=0
    for i in user_data['enumirate']:
        num+=1
        if mess==i:
            print(str(mess)+'+'+str(i))
            num+=1

            break
    await state.update_data(enumirate=num)
    await OrderDataUser.product_sp2.set()









#сюда пр СКЛАД

#but_spoiled
@dp.callback_query_handler(state="*", text='but_Sklad')
async def product_search_in_buttons_spoiled(call: types.CallbackQuery, state: FSMContext):
    capt = call.message['caption']
    id_person=call.from_user['id']

    print('СКЛАД')
    #cursor.execute(f"SELECT name_table_spis FROM users WHERE tele_id={id_person} ")
   # table_name =cursor.fetchone()[0]
   # sheet = client.open(table_name).sheet1
    sheet = sheet_num('sklad', id_person)
    all_products = sheet.col_values(1)
    #print(all_products)
    del all_products[0]
    item_back = InlineKeyboardButton(text='Назад ↩️', callback_data='go_back')
    spoiled2 = InlineKeyboardMarkup(row_width=3, resize_keyboard=True)
    spoiled2.add(item_back)
    check=True
   # print(all_products)
    counter_products=0
    #print(len(all_products))
    x=False
    print(all_products)
    #del all_products[50:]
    print(all_products)
    for prod in all_products:
        
       # print(counter_products)

        item_prod = InlineKeyboardButton(text=prod, callback_data=prod)
        if check==True:
            spoiled2.add(item_prod)
            check=False
        else:
           # print(sys.getsizeof(item_prod))
            if len(prod)>35:
                pass
            else:
                spoiled2.insert(item_prod)
        counter_products+=1
        #sys.getsizeof() 
        '''
        if counter_products>52:
            x=True
            print(counter_products)
            #print(all_products)
            del all_products[:50]
            print(all_products)
            spoiled2_2 = InlineKeyboardMarkup(row_width=3, resize_keyboard=True)
            spoiled2_2.add(item_back)
            for i in all_products:
                item_prod = InlineKeyboardButton(text=i, callback_data=i)
                spoiled2_2.add(item_prod)
            await bot.send_message(chat_id=id_person, text='Выбери продукт!', reply_markup=spoiled2_2)
      
            break
        '''
    await bot.send_message(chat_id=id_person, text='Выбери продукт', reply_markup=spoiled2)

    await state.update_data(enumirate=all_products)
    await OrderDataUser.product_sklad1.set()






@dp.message_handler(state=OrderDataUser.product_sklad2, content_types=types.ContentTypes.TEXT)
async def product_button_spoiled_step3(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    id_person= message['from']['id']
    mess=message.text
   # cursor.execute(f"SELECT name_table_spis FROM users WHERE tele_id={id_person} ")
    #table_name =cursor.fetchone()[0]
    #sheet = client.open(table_name).sheet1
    sheet = sheet_num('sklad', id_person)
    all_products = sheet.row_values(1)

    current_datetime = datetime.now()
    print(current_datetime.year)            # 2019
    print(current_datetime.month)           # 12
    print(current_datetime.day) 
    day=current_datetime.day
    mounth=current_datetime.month
    mass_date=[day, mounth]
    num_=0
    for i in mass_date:
        if len(str(i))==1:
            i='0'+str(i)
            mass_date[num_]=i
        num_+=1
    string=str(mass_date[0])+'.'+str(mass_date[1])+'.'+str(str(current_datetime.year)[-2:])
   # cursor.execute(f"SELECT name_table_spis FROM users WHERE tele_id={id_person} ")
   # table_name =cursor.fetchone()[0]
    sheet = sheet_num('sklad', id_person)
    
    all_products = sheet.row_values(1)
    num2=0
    print(string)
    for i in all_products:
        num2+=1
        if i==string:
            break
    print(user_data['enumirate'], num2)
    sheet.update_cell(user_data['enumirate'], num2, mess)
    await bot.send_message(chat_id=id_person, text='Внёс изменение в таблицу')


#after_search_sp
@dp.inline_handler(lambda query: len(query.query) > 0, state=OrderDataUser.after_search_sklad)
async def query_text(query):
    #print('INL')
    print(query)
    id_person=query.from_user['id']
    print(id_person)
    film_name_by_inline = query.query.lower() #То что вводит пользователь при обращении
    print(film_name_by_inline)
    try:
       
     #   cursor.execute(f"SELECT name_table_spis FROM users WHERE tele_id={id_person};")
      #  table_name =cursor.fetchone()[0]
      #  sheet = client.open(table_name).sheet1
        sheet = sheet_num('sklad', id_person)
        all_products = sheet.col_values(1)
        #print(all_products)
        del all_products[0]
    except:
        print("ну ошибка типо")
    fav_products = []
    for i in all_products:
        if film_name_by_inline in i.lower():
            print('добавил '+str(i))
            fav_products.append(i)
    
    results = []
   # print(film_list)
    for i in range(0, len(fav_products)):
        single_msg = types.InlineQueryResultArticle(
            id=fav_products[i],
            title=fav_products[i],
            input_message_content=types.InputTextMessageContent(message_text=fav_products[i]), #добавляем ссылку на фильм в чат
            #description='Year: ' + str(film_list[i][1]) + ' \n' + 'Rating: ' + str(film_list[i][2]),
            #thumb_url=film_list[i][5],
        )
        results.append(single_msg)
  #  await OrderDataUser.search_sklad_str.set()

    await bot.answer_inline_query(query.id, results)


@dp.message_handler(state=OrderDataUser.after_search_sklad, content_types=types.ContentTypes.TEXT)
async def product_button_spoiled_step3(message: types.Message, state: FSMContext):
    print('зашёл')
    id_person= message['from']['id']
    mess=message.text
    user_data = await state.get_data()

    #cursor.execute(f"SELECT name_table_spis FROM users WHERE tele_id={id_person} ")
    #table_name =cursor.fetchone()[0]
    #sheet = client.open(table_name).sheet1
    sheet = sheet_num('sklad', id_person)
    all_products = sheet.col_values(1)
    #print(all_products)
    del all_products[0]

    await bot.send_message(chat_id=id_person, text='Введи значение которое положить в ячейку')
    num=0
    for i in all_products:
        num+=1
        if mess==i:
            print(str(mess)+'+'+str(i))
            num+=1

            break
    await state.update_data(enumirate=num)
    await OrderDataUser.product_sklad2.set()





@dp.callback_query_handler(lambda c: True, state = '*')
async def product_button_spoiled_step2(call):
    mess = call.data
    id_person=call.from_user['id']
    mass_points=['Гражданка', 'Грибы', 'Невский 872', 'Невский 85', 'Парк', 'Нов112', 'Ветеранов 23']
    for point in mass_points:
        if mess==point:
            cursor.execute(f"UPDATE `users` SET `point_today` = '{mess}' WHERE tele_id = {id_person};")
            conn.commit()
            main_k = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            item_change_point = InlineKeyboardButton(text='Изменить точку')
            spoiled = InlineKeyboardButton(text='Добавить списывание продукта в таблицу')
            item_sklad_point = InlineKeyboardButton(text='Склад')
            item_prihod_uhod = InlineKeyboardButton(text='Приход/уход')
            item_who_read = InlineKeyboardButton(text='Посмотреть кто прочитал рассылку')
            item_prof = InlineKeyboardButton(text='Профиль')
            #item_filter_search2 = InlineKeyboardButton(text='⚙️ Search filter')

            main_k.add(item_change_point, spoiled, item_sklad_point, item_prihod_uhod, item_who_read, item_prof)
            await bot.send_message(chat_id=id_person, text=f'Теперь ваша точка - {mess}')
            if id_person in admin_id:

                item_rass = InlineKeyboardButton(text='Рассылка')
                main_k.add(item_rass)

            await bot.send_message(chat_id=id_person, text='Всё меню открыто для тебя!', reply_markup=main_k)
            break
    


@dp.message_handler(state='*', content_types=types.ContentTypes.TEXT)
async def product_button_spoiled_step3(message: types.Message, state: FSMContext):
    id_person= message['from']['id']
    main_k = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    item_change_point = InlineKeyboardButton(text='Изменить точку')
    spoiled = InlineKeyboardButton(text='Добавить списывание продукта в таблицу')
    item_sklad_point = InlineKeyboardButton(text='Склад')
    item_prihod_uhod = InlineKeyboardButton(text='Приход/уход')
    item_who_read = InlineKeyboardButton(text='Посмотреть кто прочитал рассылку')
    item_prof = InlineKeyboardButton(text='Профиль')
    #item_filter_search2 = InlineKeyboardButton(text='⚙️ Search filter')

    main_k.add(item_change_point, spoiled, item_sklad_point, item_prihod_uhod, item_who_read, item_prof)
    if id_person in admin_id:


        item_rass = InlineKeyboardButton(text='Рассылка')
        main_k.add(item_rass)
        
    cursor.execute(f"SELECT enter_name, point_today, key_access FROM users WHERE tele_id='{id_person}';")
    point = cursor.fetchone()

    await bot.send_message(chat_id=id_person, text='Здравствуй, '+str(point[0])+'\nВыбранная ночка: '+str(point[1])+'\n', reply_markup=main_k)
