from peewee import *

db = SqliteDatabase('betsy.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    name = CharField()
    address = TextField()
    billing_info = TextField()

class Product(BaseModel):
    name = CharField()
    description = TextField()
    price = DecimalField(decimal_places=2, auto_round=True)
    quantity = IntegerField()
    owner = ForeignKeyField(User, backref='products')

class Tag(BaseModel):
    name = CharField(unique=True)

class ProductTag(BaseModel):
    product = ForeignKeyField(Product, backref='tags')
    tag = ForeignKeyField(Tag, backref='products')

class Transaction(BaseModel):
    buyer = ForeignKeyField(User, backref='transactions')
    product = ForeignKeyField(Product)
    quantity = IntegerField()

def initialize_db():
    db.connect()
    db.create_tables([User, Product, Tag, ProductTag, Transaction])

if __name__ == '__main__':
    initialize_db()
