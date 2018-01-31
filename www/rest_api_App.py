#!/usr/bin/python3

from flask import Flask, jsonify
import sqlite3 as sql

app = Flask(__name__)

######## Database REST API ##########
class Person:
    def __init__(self, id, name, description, year, month, day):
        self.id = id
        self.name = name
        self.description = description
        self.born_year = year
        self.born_month = month
        self.born_day = day

    def to_Json(self):
        return {
            'person_id': self.id,
            'person_name': self.name,
            'person_description': self.description,
            'person_born_year': self.born_year,
            'person_born_month': self.born_month,
            'person_born_day': self.born_day
        }

# Connect to database and execute required query with specified parameters
def db_connect_and_query(query, parameters):
    con = sql.connect('/home/tomas/sampleApp/data.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute(query, parameters)
    rows = cur.fetchall()
    con.close()

    result = {}
    if len(rows) > 0:
        for p in rows:
            result[p['person_id']] = (Person(p['person_id'], p['person_name'], p['person_description'], p['person_born_year'], p['person_born_month'], p['person_born_day']).to_Json())
        return jsonify( result )
    else:
        return jsonify( result )


# PERSONS BY NAME
@app.route('/api/v1.0/name=<name>', methods=['GET'])
def get_persons_by_name(name):
    query = "SELECT * FROM persons WHERE person_name = ?"
    parameters = [ name ]

    res = db_connect_and_query(query, parameters)
    return res


# PERSONS BY PART OF NAME
@app.route('/api/v1.0/namepart=<namepart>', methods=['GET'])
def get_persons_by_namepart(namepart):
    query = "SELECT * FROM persons WHERE person_name LIKE '%' || ? || '%'"
    parameters = [ namepart ]

    res = db_connect_and_query(query, parameters)
    return res


# PERSONS BY PART OF DESCRIPTION
@app.route('/api/v1.0/descpart=<descpart>', methods=['GET'])
def get_persons_by_descpart(descpart):
    query = "SELECT * FROM persons WHERE person_description LIKE '%' || ? || '%'"
    parameters = [ descpart ]

    res = db_connect_and_query(query, parameters)
    return res


# PERSONS BY NATIONALITY
@app.route('/api/v1.0/nation=<nation>', methods=['GET'])
def get_persons_by_nation(nation):
    query = "SELECT * FROM persons WHERE person_description LIKE ? || '%'"
    parameters = [ nation ]

    res = db_connect_and_query(query, parameters)
    return res


# PERSONS BY BORN DATE
@app.route('/api/v1.0/day=<int:day>&month=<int:month>&year=<int:year>', methods=['GET'])
def get_persons_by_born_date(day, month, year):
    query = "SELECT * FROM persons WHERE person_born_day = ? AND person_born_month = ? AND person_born_year = ?"
    parameters = [ day, month, year ]

    res = db_connect_and_query(query, parameters)
    return res


# PERSONS BY BORN DAY, MONTH
@app.route('/api/v1.0/day=<int:day>&month=<int:month>', methods=['GET'])
def get_persons_by_born_day_month(day, month):
    query = "SELECT * FROM persons WHERE person_born_day = ? AND person_born_month = ?"
    parameters = [ day, month ]

    res = db_connect_and_query(query, parameters)
    return res


# PERSONS BY BORN DAY
@app.route('/api/v1.0/day=<int:day>', methods=['GET'])
def get_persons_by_born_day(day):
    query = "SELECT * FROM persons WHERE person_born_day = ?"
    parameters = [ day ]

    res = db_connect_and_query(query, parameters)
    return res


# PERSONS BY BORN MONTH
@app.route('/api/v1.0/month=<int:month>', methods=['GET'])
def get_persons_by_born_month(month):
    query = "SELECT * FROM persons WHERE person_born_month = ?"
    parameters = [ month ]

    res = db_connect_and_query(query, parameters)
    return res


# PERSONS BY BORN YEAR
@app.route('/api/v1.0/year=<int:year>', methods=['GET'])
def get_persons_by_born_year(year):
    query = "SELECT * FROM persons WHERE person_born_year = ?"
    parameters = [ year ]

    res = db_connect_and_query(query, parameters)
    return res
######################################################


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=3000)
