import unittest
from flask import current_app
from app import create_app, db
from app.models import User
from app.routes import bp

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('config.Config')
        self.app.register_blueprint(bp)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home(self):
        with self.app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(response.json, list)

