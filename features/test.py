import unittest
from features.tools import get_user_credentials


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print(get_user_credentials())
        # self.assertEqual([x.strip('\n\r') for x in get_user_credentials()], ['g.ionutcristian95@gmail.com', 'JustTeST453385@!'])
        self.assertEqual(get_user_credentials(), ['g.ionutcristian95@gmail.com', 'JustTeST453385@!'])


if __name__ == '__main__':
    unittest.main()
