#!/usr/bin/python3
import re
import sqlite3 as sql

months_dict = { 'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6, 'july':7, 'august':8, 'september':9, 'october':10, 'november':11, 'december':12 }


# Nacita vsetky zaznamy, riadok po riadku z pripraveneho suboru
sources_filename = 'raw_data'
lines = []
with open(sources_filename) as f:
    lines = f.readlines()

# Naformatuje kazdu polozku a vlozi vsetky zaznamy do databazy
try:
    with sql.connect("data.db") as con:
        cur = con.cursor()

        born_day = 0
        born_month = 0

        for line in lines:

            # Date label
            if line[0] == '#':
                born_month = months_dict[re.sub('[^a-z]', '', line)]
                born_day = int(re.sub('[^0-9]', '', line))
                continue

            born_year = int(re.sub('[^0-9]+', '', line.split('–')[0]))
            person_name = ((re.sub('[ ][(][d][.].+', '', re.sub('.+[–][ ]', '', line))).split(',')[0]).strip()
            a = ((re.sub('[(][d][.][ ].+', '', re.sub('.+[–][ ]', '', line, 1))).strip())
            person_description = a.replace(a.split(',')[0] + ', ', '', 1)

            print(line)
            cur.execute("INSERT INTO persons (person_name,person_description,person_born_year,person_born_year_bc, person_born_month, person_born_day) VALUES (?,?,?,?,?,?)",(person_name,person_description,born_year,0,born_month,born_day))
            #print("y:" + str(born_year) + "\tn:" + person_name + "\td:" + person_description + "\t" + str(born_day) + "." + born_month)

        con.commit()
        msg = "Records successfully added"

except:
    con.rollback()
    msg = "error in insert operation"

finally:
    print(msg)
    con.close()
