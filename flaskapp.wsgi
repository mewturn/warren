activate_this = '/var/www/html/flaskapp/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
sys.path.insert(0, '/var/www/html/flaskapp')

from flaskapp import app as application