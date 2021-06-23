from pymysql.cursors import DictCursor
import xlrd
import pymysql
import os


# Open the workbook and define the worksheet
filename = r"22062021.xls"
if not os.path.exists(filename):
    print("No encontré el archivo")

book = xlrd.open_workbook(filename)
sheet = book.sheet_by_name("Hoja1")
lista = []


database = pymysql.connect(
    host="remotemysql.com",
    user="Gqvfd1Hou1",
    passwd="3KYt6E4w2f",
    database="Gqvfd1Hou1",
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

for row in range(1, sheet.nrows):

    email = sheet.cell(row, 0).value
    emailComparar = sheet.cell(row, 0).value

    print(emailComparar)
    name = sheet.cell(row, 1).value
    last_name = sheet.cell(row, 2).value

    """ for row in lista:
        print(row + " + " + email)
        if row != email: """
    cursor = database.cursor()
    query = """INSERT INTO SLC_community (email, name, last_name) SELECT %s, %s, %s WHERE NOT EXISTS (SELECT * FROM SLC_community WHERE email = '"""+emailComparar +"""')"""
    values = (email, name, last_name)
    cursor.execute(query, values)
    cursor.close()
    """ database.commit() """

database.commit()

database.close()

print("")
print("Done! ")
print("")
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print("Acabo de importar", columns, "Columna y", rows, "Fila de datos a MySQL!")
