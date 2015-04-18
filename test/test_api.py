import os
import unittest
import tempfile
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from iInvest import app, db

class APITestCase(unittest.TestCase):
    """docstring for APITestCase"""
    def setUp(self):
        self.db_fd, app.config['SQLALCHEMY_DATABASE_URI']= tempfile.mkstemp()
        #self.app_context = app.app_context()
        #self.app_context.push()
        db.create_all()
        self.client = app.test_client()
        #port = int(os.environ.get('PORT', 33333))
        #app.debug=True
        #app.run(host='0.0.0.0',port=port)
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        #self.app_context.pop()
        os.close(self.db_fd)
        os.unlink(app.config['SQLALCHEMY_DATABASE_URI'])
    def test_get_trust_products(self):
        rv = self.app.get('/')
        print rv.data
        assert 'No entries here so far' in rv.data
if __name__ == '__main__':
    unittest.main()