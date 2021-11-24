import mongoengine as me

class Stock(me.Document):
    meta = {"collection": "stock"}

    name = me.StringField(required = True)

class ItemSize(me.EmbeddedDocument):
    width = me.FloatField()
    height = me.FloatField()
    deep = me.FloatField()

class Item(me.Document):
    meta = {"collection": "item"}

    name = me.StringField(required = True)
    description = me.StringField(required = True)
    weight = me.FloatField(default = 0)
    
    size = me.EmbeddedDocumentField(ItemSize)

class Status(me.Document):
    meta = {"collection": "ststus"}

    buyer = me.StringField(required = True)
    seller = me.StringField(required = True)
    item = me.StringField(required = True)