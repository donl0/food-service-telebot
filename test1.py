import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
pp = pprint.PrettyPrinter()

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('employees_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('spis_table')
sheet = sheet.worksheet("Грибы")
#telemedicine = sheet.get_all_records()
#pp.pprint(telemedicine)
#print(telemedicine[2])
all_v = sheet.cell(1, 1)
print(all_v)

#sheet.update_cell(1, 1, "telemedicine_id") #обновить конкретную строку
#ЗАхуярить в строку с номером 3
#row = ["I'm","inserting","a","new","row","into","a,","Spreadsheet","using","Python"]
#index = 3
#sheet.insert_row(row, index)

'''
sheet.get_all_values()#чиста получить все данные по строчкам по  rows
sheet.row_values(2)#получение конкретной строчки
sheet.col_values(16)#получение конкретного столбца
sheet.cell(1, 1).получение ячейки по координатам

'''