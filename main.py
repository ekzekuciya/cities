import requests
from flask import Flask, render_template, request, redirect, url_for
from models import *
from peewee import *

app = Flask(__name__)


@app.route('/')
def index():
    all_cities = City.select()
    return render_template('index.html', all_cities=all_cities)


@app.route('/cities/<int:city_id>')
def cities(city_id):
    city = City.get_or_none(id=city_id)
    if city:
        return render_template('city_detail.html', city=city)
    else:
        return 'Undefined 404'


@app.route('/add_city', methods=['GET', 'POST'])
def add_city():
    if request.method == 'POST':
        city = City(name=request.form['name'], country=request.form['country'], population=request.form['population'])
        city.save()
        return redirect(url_for('index'))

    return render_template('add_city.html')

@app.route('/delete', methods=['POST'])
def func():
    delete_city = City.get_or_none(id=request.form['id'])
    delete_city.delete_instance()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)



