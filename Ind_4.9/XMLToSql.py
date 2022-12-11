import sqlite3 as sql
from xml.etree import ElementTree as El

db = sql.connect("medicine.db")

cur = db.cursor()

tree = El.parse("pacient.xml")
root = tree.getroot()

for pacient in root.findall("pacient"):
    name = str(pacient.find("NameOfPacient").text) + " XML"

    policy = pacient.find("NumberOfPolicy").text

    birth = pacient.find("YearOfBirth").text

    loc = pacient.find("LocationOfPac").text

    dis = pacient.find("DiseaseName").text

    sev = pacient.find("Severity").text

    tre = pacient.find("MethodOfTreatment").text

    dur = pacient.find("DurationOfTreatment").text

    cur.execute("""INSERT INTO pacient VALUES (?,?,?,?)""", (name, policy, birth, loc))

    cur.execute("""INSERT INTO diagnosis VALUES (?,?,?)""", (dis, sev, policy))

    cur.execute("""INSERT INTO treatment VALUES (? ,? ,?)""", (tre, dur, policy))

    db.commit()

db.close()
