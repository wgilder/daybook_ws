import json
import os
import re
import time

from streifen.ws.daybook import get_next_item_id, get_directory

class Item(object):
    def __init__(self, user, id = -1, title = "", date = "", amount = -1, currency = "", location = ""):
        self.id = id
        self.user = user

        self.title = title
        self.date = date
        self.amount = amount
        self.currency = currency
        self.location = location

        if id > 0:
            self.deserialize()
        else:
            self.id = get_next_item_id(self.user.get_id())

    def set_title(self, title):
        self.title = title
        self.serialize()

    def get_title(self):
        return self.title

    def set_date(self, date):
        self.date = date
        self.serialize()

    def get_date(self):
        return self.date

    def set_location(self, location):
        self.location = location
        self.serialize()

    def get_location(self):
        self.location

    def set_amount(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def get_currency(self):
        return self.currency

    def get_amount(self):
        return self.amount

    def get_id(self):
        return id

    def get_user(self):
        return self.user

    def serialize(self):
        path = get_directory(self.user.get_id(), ensure_present = True) + str(self.id) + ".item"
        file = open(path, "w")
        raw = { 
            'title': self.title,  
            'date': self.date,
            'location': self.location,
            'amount': self.amount,
            'currency': self.currency
        }

        json.dump(raw, file)
        file.close()

    def deserialize(self):
        path = get_directory(self.user.get_id()) + str(self.id) + ".item"
        file = open(path, "r")
        raw = json.load(file)

        file.close()

        self.title = raw['title']
        self.date = raw['date']
        self.location = raw['location']
        self.amount = raw['amount']
        self.currency = raw['currency']



# return { 'email': email, 'order_count': self.order_count, 'sources': self.sources, 'connection_count': self.connection_count, 'gender': self.gender, 'locale': self.locale }


# Item attributes:
#  - ID (unique, assigned)
#  - Title
#  - Date
#  - Geo-location
#  - Amount
#  - Currency
## optional
#  - Notes
#  - Tags
#  - Method of payment