from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password(self):
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))


    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)



    def test_hashing(self):
        u = User(username='yura')
        u.set_password('huila')
        self.assertFalse(u.check_password('nehuila'))
        self.assertTrue(u.check_password('huila'))

    def test_avatar(self):
        u = User(username='susan')
        u.set_photo('https://www.gravatar.com/avatar/d4c74594d841139328695756648b6bd6?d=identicon&s=128')
        self.assertFalse(u.check_photo('https://www.google.com/url?sa=i&url=https%3A%2F%2Fzen.yandex.ru%2Fmedia%2Feternalanime%2Fanime-pary-u-kotoryh-vse-zashlo-daleko-za-predely-poceluev-5dac795434808200afbf9c46&psig=AOvVaw3DLfwgWeDQdulxOiB3d35x&ust=1591962799688000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCKDl59vZ-ekCFQAAAAAdAAAAABAG'))
        self.assertTrue(u.check_photo('https://www.gravatar.com/avatar/d4c74594d841139328695756648b6bd6?d=identicon&s=128'))
        
    

if __name__ == '__main__':
    unittest.main(verbosity=2)