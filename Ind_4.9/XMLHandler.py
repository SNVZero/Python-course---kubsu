import sqlite3 as sql
from xml.etree import ElementTree as El

root = El.Element("Pacients-List")

db = sql.connect("medicine.db")

cur = db.cursor()

id = cur.execute("""SELECT rowid FROM pacient""").fetchall()

for el in id:
    subroots = El.SubElement(root, "pacient")
    pid = int(el[0])
    pac = cur.execute("""SELECT * FROM pacient WHERE rowid = ?  """, (pid,)).fetchall()

    name = El.SubElement(subroots, "NameOfPacient")
    name.text = pac[0][0]

    policy = El.SubElement(subroots, "NumberOfPolicy")
    policy.text = pac[0][1]

    birth = El.SubElement(subroots, "YearOfBirth")
    birth.text = pac[0][2]

    loc = El.SubElement(subroots, "LocationOfPac")
    loc.text = pac[0][3]

    dia = cur.execute("""SELECT * FROM diagnosis WHERE id_policyDia = ?""", (pac[0][1],)).fetchall()

    dis = El.SubElement(subroots, "DiseaseName")
    dis.text = dia[0][0]

    sev = El.SubElement(subroots, "Severity")
    sev.text = dia[0][1]

    treatment = cur.execute("""SELECT * FROM treatment WHERE id_policyTre = ? """, (pac[0][1],)).fetchall()

    tre = El.SubElement(subroots, "MethodOfTreatment")
    tre.text = treatment[0][0]

    dur = El.SubElement(subroots, "DurationOfTreatment")
    dur.text = treatment[0][1]

    tree = El.ElementTree(root)
    tree.write("pacient.xml", encoding='UTF-8')

db.close()

