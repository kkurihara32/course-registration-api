import unittest

from course_registration_api.domain.courses.period import Period
from course_registration_api.domain.shared.exceptions \
    import InvalidPeriodException


class MyTestCase(unittest.TestCase):
    def test_initialize(self):
        test_period = Period(1)
        actual = test_period.value
        expected = 1
        self.assertEqual(actual, expected)

    def test_initialize_with_invalid_value(self):
        with self.subTest(msg="valueがfloatの場合の異常系のテスト"):
            with self.assertRaises(InvalidPeriodException):
                Period(1.0)
        with self.subTest(msg="valueがstrの場合の異常系のテスト"):
            with self.assertRaises(InvalidPeriodException):
                Period("dummy")
        with self.subTest(msg="1-8以外の数字を指定した場合の異常系のテスト"):
            with self.assertRaises(InvalidPeriodException):
                Period(9)


if __name__ == '__main__':
    unittest.main()
