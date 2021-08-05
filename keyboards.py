from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

item_back = InlineKeyboardButton(text='Назад ↩️', callback_data='go_back')
item_back2 = InlineKeyboardButton(text='Назад ↩️')
'''
main_k = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
item_change_point = InlineKeyboardButton(text='Изменить точку')
spoiled = InlineKeyboardButton(text='Добавить списывание продукта в таблицу')
item_sklad_point = InlineKeyboardButton(text='Склад')
item_prihod_uhod = InlineKeyboardButton(text='Приход/уход')
item_who_read = InlineKeyboardButton(text='Посмотреть кто прочитал рассылку')
item_prof = InlineKeyboardButton(text='Профиль')
#item_filter_search2 = InlineKeyboardButton(text='⚙️ Search filter')

main_k.add(item_change_point, spoiled, item_sklad_point, item_prihod_uhod, item_who_read, item_prof)
'''
prof_k = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
item_change_fio = InlineKeyboardButton(text='Изменить ФИО')
prof_k.add(item_back2, item_change_fio)


prihod_uh_keyb = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
item_prih_make = InlineKeyboardButton(text='Сделать фотографию прихода')
item_uh_make = InlineKeyboardButton(text='Сделать фотографию ухода')
item_prih_see = InlineKeyboardButton(text='Посмотреть фотографии прихода')
item_uh_see = InlineKeyboardButton(text='Посмотреть фотографии ухода')

#item_filter_search2 = InlineKeyboardButton(text='⚙️ Search filter')

prihod_uh_keyb.add(item_back2,item_prih_make, item_uh_make, item_prih_see, item_uh_see)

#item_sklad_point = InlineKeyboardButton(text='Занести значение в склад')

sklad_keyb = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
item_sklad_point = InlineKeyboardButton(text='Занести значение в склад')
item_add_sklad_ph = InlineKeyboardButton(text='Добавить фотографию о принятии поставки')
item_check_sklad_ph = InlineKeyboardButton(text='Посмотреть фотографии с принятием поставки')

#item_filter_search2 = InlineKeyboardButton(text='⚙️ Search filter')

sklad_keyb.add(item_back2 ,item_sklad_point, item_add_sklad_ph, item_check_sklad_ph)



way_search_to_spoiled = InlineKeyboardMarkup(row_width=1, resize_keyboard=True)

item_but_spoiled = InlineKeyboardButton(text='Найти продукт в списке', callback_data='but_spoiled')
item_search_spoiled = InlineKeyboardButton(text='Найти продукт с помощью поиска', switch_inline_query_current_chat='')
way_search_to_spoiled.add(item_but_spoiled, item_search_spoiled)

way_search_to_sklad = InlineKeyboardMarkup(row_width=1, resize_keyboard=True)

item_but_sklad = InlineKeyboardButton(text='Найти продукт в списке', callback_data='but_Sklad')
item_search_sklad = InlineKeyboardButton(text='Найти продукт с помощью поиска', switch_inline_query_current_chat='')
way_search_to_sklad.add(item_but_sklad, item_search_sklad)


point_chose = InlineKeyboardMarkup(row_width=1, resize_keyboard=True)

point_grajd = InlineKeyboardButton(text='Гражданка', callback_data='Гражданка')
point_grib = InlineKeyboardButton(text='Грибы', callback_data='Грибы')
point_nevs872 = InlineKeyboardButton(text='Невский 872', callback_data='Невский 872')
point_nevsk85 = InlineKeyboardButton(text='Невский 85', callback_data='Невский 85')
point_park = InlineKeyboardButton(text='Парк', callback_data='Парк')
point_nov112 = InlineKeyboardButton(text='Нов112', callback_data='Нов112')
point_vet23 = InlineKeyboardButton(text='Ветеранов 23', callback_data='Ветеранов 23')

point_chose.add(point_grajd, point_grib, point_nevs872, point_nevsk85, point_park, point_nov112, point_vet23)



rassilka_k = InlineKeyboardMarkup(row_width=1, resize_keyboard=True)


rass_mess_pic = InlineKeyboardButton(text='Сообщение+картинка', callback_data='adv_mass_send1')
rass_mess = InlineKeyboardButton(text='Просто сообщение', callback_data='just_mes')

rassilka_k.add(rass_mess_pic, rass_mess)




rassilka_read_k = InlineKeyboardMarkup(row_width=1, resize_keyboard=True)

i_read = InlineKeyboardButton(text='Прочитал', callback_data='i read')
rassilka_read_k.add(i_read)