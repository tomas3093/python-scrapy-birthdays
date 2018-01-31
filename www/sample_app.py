#!/usr/bin/python3

from flask import Flask, render_template, request
import requests
import json
import re

app = Flask(__name__)

def request_api_and_render(api_uri, template):
    messages = []
    data = {}
    try:
        data = requests.get(api_uri).json()
    except requests.ConnectionError:
        messages.append('Connection error!')
    except ValueError:
        messages.append('No such person!')

    return render_template(template, rows=data, messages=messages)


@app.route('/')
def main_page():
    return render_template('main_page.html')


@app.route('/search/name', methods=['GET', 'POST'])
def search_by_name():
    template = 'search_by_name.html'

    if request.method == 'POST':
        requested_name = re.sub('[^\w -%0-9]', '', request.form['name'])
        api_uri = "http://localhost:3000/api/v1.0/name=" + requested_name

        return request_api_and_render(api_uri, template)
    else:
        return render_template(template)


@app.route('/search/date-year', methods=['GET', 'POST'])
def search_by_date_year():
    template = 'search_by_date_year.html'

    if request.method == 'POST':
        fld_date = request.form['date']
        day = re.sub('^[0]*', '', fld_date.split('-')[2])
        month = re.sub('^[0]*', '', fld_date.split('-')[1])
        year = re.sub('^[0]*', '', fld_date.split('-')[0])
        api_uri = "http://localhost:3000/api/v1.0/day=" + day + "&month=" + month + "&year=" + year

        return request_api_and_render(api_uri, template)
    else:
        return render_template(template)


@app.route('/search/date', methods=['GET', 'POST'])
def search_by_date():
    template = 'search_by_date.html'

    if request.method == 'POST':
        fld_day = request.form['day']
        fld_month = request.form['month']
        api_uri = "http://localhost:3000/api/v1.0/day=" + fld_day + "&month=" + fld_month

        return request_api_and_render(api_uri, template)
    else:
        return render_template(template)


@app.route('/search/day', methods=['GET', 'POST'])
def search_by_day():
    template = 'search_by_day.html'

    if request.method == 'POST':
        fld_day = request.form['day']
        api_uri = "http://localhost:3000/api/v1.0/day=" + fld_day

        return request_api_and_render(api_uri, template)
    else:
        return render_template(template)


@app.route('/search/month', methods=['GET', 'POST'])
def search_by_month():
    template = 'search_by_month.html'

    if request.method == 'POST':
        fld_month = request.form['month']
        api_uri = "http://localhost:3000/api/v1.0/month=" + fld_month

        return request_api_and_render(api_uri, template)
    else:
        return render_template(template)


@app.route('/search/year', methods=['GET', 'POST'])
def search_by_year():
    template = 'search_by_year.html'

    if request.method == 'POST':
        fld_year = request.form['year']
        api_uri = "http://localhost:3000/api/v1.0/year=" + fld_year

        return request_api_and_render(api_uri, template)
    else:
        return render_template(template)


@app.route('/search/nation', methods=['GET', 'POST'])
def search_by_nation():
    template = 'search_by_nation.html'

    if request.method == 'POST':
        fld_nation = request.form['nation']
        api_uri = "http://localhost:3000/api/v1.0/nation=" + fld_nation

        return request_api_and_render(api_uri, template)
    else:
        return render_template(template)


@app.route('/search/profession', methods=['GET', 'POST'])
def search_by_profession():
    template = 'search_by_profession.html'

    if request.method == 'POST':
        fld_profession = request.form['profession']
        api_uri = "http://localhost:3000/api/v1.0/descpart=" + fld_profession

        return request_api_and_render(api_uri, template)
    else:
        return render_template(template)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
