from peewee import *

db = SqliteDatabase('city_list.db')


class City(Model):
    name = CharField()
    country = CharField()
    population = IntegerField()

    class Meta:
        database = db


with db:
    db.create_tables([City])
    if not City.select().exists():
        City.create(name='Bishkek', country='Kyrgyzstan', population=5000000)
        City.create(name='Alma-ata', country='Kazaqstan', population=7000000)
        City.create(name='Tashkent', country='Uzbekistan', population=8000000)


cities = City.select()


