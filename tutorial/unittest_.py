from unittest import TestCase


def reserve(var):
    return var[::-1]


class TestReserve(TestCase):
    def test_str(self):
        self.assertEqual('olleh', reserve('hello'))

    def test_list(self):
        self.assertEqual([3, 2, 1], reserve([1, 2, 3]))


class Math(object):
    def min(self, x):
        return min(x)

    def max(self, x):
        return max(x)


class TestMath(TestCase):
    def setUp(self):
        self.x = [3, 1, 5, 7, 2]
        self.math = Math()

        print('setUp', self.x)

    def tearDown(self):
        print('tearDown', self.x)

    def test_min(self):
        self.assertEqual(1, self.math.min(self.x))

    def test_max(self):
        self.assertEqual(7, self.math.max(self.x))
