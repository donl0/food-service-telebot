import pymysql
conn = pymysql.connect(host='localhost', 
                       user='root', 
                       passwd='root', 
                       db='coffe_db'
)
cursor = conn.cursor()

