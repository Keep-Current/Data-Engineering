#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask_script import Manager, Server
from flask_script.commands import Clean, ShowUrls

from keep_current_storage.app import create_app


app = create_app(os.environ.get('FLASK_ENV') or 'DevConfig')
manager = Manager(app)

manager.add_command('server', Server())
manager.add_command('urls', ShowUrls())
manager.add_command('clean', Clean())

if __name__ == '__main__':
    manager.run()
