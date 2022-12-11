#!/usr/bin/env python3
import cgi
import sqlite3 as sql
import html

db = sql.connect('medicine.db')

cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS pacient (
    NameOfPacietn TEXT,
    NumberOfPolicy TEXT,
    YearOfBirth TEXT,
    LocationOfPac TEXT 
)''')

cur.execute('''CREATE TABLE IF NOT EXISTS diagnosis (
    DiseaseName TEXT,
    Severity TEXT,
    id_policyDia TEXT,
    FOREIGN KEY (id_policyDia) REFERENCES pacietn(NumberOfPolicy) 
)''')

cur.execute('''CREATE TABLE IF NOT EXISTS treatment (
    MethodOfTreatment TEXT,
      TEXT,
    id_policyTre TEXT,
    FOREIGN KEY (id_policyTre) REFERENCES pacietn(NumberOfPolicy) 
)''')

form = cgi.FieldStorage()

try:
    val1 = (str(form.getfirst("NameOfPacietn")), str(form.getfirst("NumberOfPart")), str(form.getfirst("YearOfBirth")), str(form.getfirst("LocationOfPac")))
    val2 = (str(form.getfirst("DiseaseName")),str(form.getfirst("Severity")), str(form.getfirst("NumberOfPart")))
    val3 = (str(form.getfirst("Treatment")), str(form.getfirst("DurationOfTreat")), str(form.getfirst("NumberOfPart")))

    cur.execute("""INSERT INTO pacient VALUES (?,?,?,?)""", val1)



    cur.execute("""INSERT INTO diagnosis VALUES (?,?,?)""", val2)



    cur.execute("""INSERT INTO treatment VALUES (? ,? ,?)""", val3)

    db.commit()
    cur.close()
    db.close()

    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
               <html>
               <head>
                   <meta charset="utf-8">
                   <title>Карточка пациента</title>
               </head>
               <body>""")

    print("<h1>Карточка пациента сохранена</h1>")

    print("""</body>
               </html>""")


except:
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
                  <html>
                  <head>
                      <meta charset="utf-8">
                      <title>Карточка пациента</title>
                  </head>
                  <body>""")

    print("<h1>Ошибка сохранения в базу</h1>")

    print("""</body>
                  </html>""")

    cur.close()
    db.close()

