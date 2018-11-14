import json
import os
import re
import time

from streifen.ws.daybook import get_next_user_id, get_directory

class User(object):
    def __init__(self, id = -1, name = "", email = ""):
        self.name = name
        self.email = email
            
        if id > 0:
            self.id = id
            self.deserialize()
        else:
            self.id = get_next_user_id()

    def set_name(self, name):
        self.name = name
        self.serialize()

    def get_name(self):
        return self.name

    def set_email(self, email):
        self.email = email
        self.serialize()

    def get_email(self):
        return self.email

    def get_id(self):
        return self.id

    def serialize(self):
        path = get_directory(self.id, ensure_present = True) + "user.info"
        file = open(path, "w")
        raw = { 
            'name': self.name,  
            'email': self.email
        }

        json.dump(raw, file)
        file.close()

    def deserialize(self):
        path = get_directory(self.id) + "user.info"
        file = open(path, "r")
        raw = json.load(file)

        file.close()

        self.name = raw['name']
        self.email = raw['email']