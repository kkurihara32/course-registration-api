import unittest

from course_registration_api.domain.courses.day_of_week import DayOfWeek


class TestDayOfWeek(unittest.TestCase):
    def test_elements(self):
        with self.subTest(msg="number of elements"):
            actual = len(DayOfWeek._member_names_)
            expected = 7
            self.assertEqual(actual, expected)
        with self.subTest(msg="sunday"):
            actual = DayOfWeek.SUNDAY.value
            expected = "日"
            self.assertEqual(actual, expected)
        with self.subTest(msg="monday"):
            actual = DayOfWeek.MONDAY.value
            expected = "月"
            self.assertEqual(actual, expected)
        with self.subTest(msg="tuesday"):
            actual = DayOfWeek.TUESDAY.value
            expected = "火"
            self.assertEqual(actual, expected)
        with self.subTest(msg="wednesday"):
            actual = DayOfWeek.WEDNESDAY.value
            expected = "水"
            self.assertEqual(actual, expected)
        with self.subTest(msg="thursday"):
            actual = DayOfWeek.THURSDAY.value
            expected = "木"
            self.assertEqual(actual, expected)
        with self.subTest(msg="friday"):
            actual = DayOfWeek.FRIDAY.value
            expected = "金"
            self.assertEqual(actual, expected)
        with self.subTest(msg="saturday"):
            actual = DayOfWeek.SATURDAY.value
            expected = "土"
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
