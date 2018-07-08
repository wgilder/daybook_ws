
import os

class Base(object):
    def __init__(self, template_name):
        if not template_name: 
            raise ValueError("template name not set")

        self._template_name = template_name

        if ("DAYBOOK_API_BUILD" in os.environ):
            self._build_number = os.environ["DAYBOOK_API_BUILD"] or "-1"
        else:
            self._build_number = "-1"

    def build_number(self):
        return self._build_number

    def attributes(self):
        d = { 
            "deploy_env": self.build_number()
        }
        return d

    def template_name(self):
        return self._template_name