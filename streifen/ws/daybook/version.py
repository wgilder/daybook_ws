from streifen.ws.daybook.base import Base

import os

class Version(Base):
    def __init__(self):
        super().__init__("version.html")

    def message(self):
        return "Another Message"

    def version(self):
        return "0.0.2"

    def author(self):
        return "Walter Gildersleeve"

    def email(self):
        return "wmg@puppet.com"

    def attributes(self):
        d = super().attributes()
    
        d["message"] = self.message()
        d["version"] = self.version()
        d["author"] = self.author()
        d["email"] = self.email()

        return d
