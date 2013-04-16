#!/usr/bin/env python
from flask.ext import script

from sanap.middlewares import ReverseProxied
from sanap.app import create_app

app = create_app()
app.wsgi_app = ReverseProxied(app.wsgi_app)


def main():
    global app
    manager = script.Manager(app)
    manager.run()

if __name__ == "__main__":
    main()
