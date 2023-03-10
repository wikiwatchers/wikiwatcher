""" index.py
Defines index which will be default view when accessing our application in browser
"""
from flask import render_template
from flask.views import MethodView


class Index(MethodView):
    """ Our default index view """
    def get(self):
        """ Renders index template """
        return render_template('index.html')
