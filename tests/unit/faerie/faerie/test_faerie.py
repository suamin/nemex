import unittest


class Test_ABC(unittest.TestCase):

    def setUp(self) -> None:
        return None

    def test_example(self):
        return self.assertEqual("", "")

    def tearDown(self) -> None:
        return None


if __name__ == '__main__':
    unittest.main()
