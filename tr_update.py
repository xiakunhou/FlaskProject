#!flask/bin/python
import os
import sys
if sys.platform == 'wn32':
    pybabel = 'flask\\Scripts\\pybabel'
else:
    pybabel = 'pybabel'
os.system(pybabel + ' extract -F babel.cfg -k lazy_gettext -o messages.pot iInvest/')
os.system(pybabel + ' update -i messages.pot -d iInvest/translations')
os.unlink('messages.pot')