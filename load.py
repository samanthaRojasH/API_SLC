from pymysql.cursors import DictCursor
import xlrd
import pymysql
import os
import sys
from datetime import datetime

# Open the workbook and define the worksheet
filename = r"C:/Users/saman/OneDrive/Documentos/SCRUM/01062021/01062021_SLC.xls"
if not os.path.exists(filename):
    print("No encontré el archivo")
    sys.exit()

book = xlrd.open_workbook(filename)
sheet = book.sheet_by_name("Hoja1")
lista = []


database = pymysql.connect(
    host="billfrqpmswhgyydyxcv-mysql.services.clever-cloud.com",
    user="uxhfzmaewjqzxbrj",
    passwd="GBn0L8UIFXxRYooyhJIE",
    database="billfrqpmswhgyydyxcv",
)

""" for row in range(1, sheet.nrows):

    email = sheet.cell(row, 0).value

    cursor_comprobar = database.cursor()
    query_comprobar = """ """SELECT email FROM SLC_community WHERE email = %s""" """
    values_comprobar = email
    cursor_comprobar.execute(query_comprobar, values_comprobar)

    result = cursor_comprobar.fetchall()
    for rowSave in result:
        comprobado = list(rowSave)
        lista.append(comprobado[0])
        database.commit()

cursor_comprobar.close() """
print(" ")
print("************************************CONSTRUYENDO COMUNIDAD SCRUM LATAM*************************************")
print(" ")
print("Loading..................................")
print(" ")
for row in range(0, sheet.nrows):

    email = sheet.cell(row, 0).value
    emailComparar = sheet.cell(row, 0).value
    print(emailComparar)
    name = sheet.cell(row, 1).value
    last_name = sheet.cell(row, 2).value

    webinar = sheet.cell(row, 3).value
    webinarComparar = sheet.cell(row, 3).value
    date = sheet.cell(row, 4).value
    member_type = sheet.cell(row, 5).value

    """ for row in lista:
        print(row + " + " + email)
        if row != email: """
    cursor = database.cursor()
    query = """INSERT INTO SLC_community_all (email, name, last_name) SELECT %s, %s, %s WHERE NOT EXISTS (SELECT * FROM SLC_community_all WHERE email = '"""+emailComparar +"""')"""
    values = (email, name, last_name)
    cursor.execute(query, values)

    today = datetime.now()
    today_date = str(today.date())
    today_date_N = today_date + "_W0106"

    query_1 = """INSERT INTO SLC_webinar (id_webinar, webinar, date) SELECT %s, %s, %s WHERE NOT EXISTS (SELECT * FROM SLC_webinar WHERE webinar = '"""+webinarComparar +"""')"""
    values_1 = (today_date_N, webinar, date)
    cursor.execute(query_1, values_1)

    query_2 = """INSERT INTO SLC_Participants (id_webinar, email, member_type) SELECT %s, %s, %s WHERE NOT EXISTS (SELECT * FROM SLC_Participants WHERE id_webinar = '"""+today_date_N +"""' and email = '"""+emailComparar +"""')"""
    values_2 = (today_date_N, email, member_type)
    cursor.execute(query_2, values_2)    

    cursor.close()
    
    database.commit()

database.close()

print("")
print("Done! ")
print("")
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print("Acabo de cargar", columns, "columnas y", rows, "filas de datos de excel para MySQL!")
