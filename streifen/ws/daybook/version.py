
import os

class Version(object):
    def __init__(self):
        if ("DAYBOOK_API_BUILD" in os.environ):
            self._build_number = os.environ["DAYBOOK_API_BUILD"]
        else:
            self._build_number = "-1"

    def message(self):
        return "Another Message"

    def version(self):
        return "0.0.2"

    def build_number(self):
        return self._build_number

    def author(self):
        return "Walter Gildersleeve"

    def email(self):
        return "wmg@puppet.com"
