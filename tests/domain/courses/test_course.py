import unittest

from course_registration_api.domain.courses.course import Course
from course_registration_api.domain.courses.course_name import CourseName
from course_registration_api.domain.courses.day_of_week import DayOfWeek
from course_registration_api.domain.courses.period import Period


class TestCourse(unittest.TestCase):
    def test_initialize(self):
        test_name = CourseName("テスト科目")
        test_day_of_week = DayOfWeek.MONDAY
        test_period = Period(1)
        test_course = Course(course_name=test_name,
                             day_of_week=test_day_of_week,
                             period=test_period)
        with self.subTest(msg="course_name"):
            actual = test_course.course_name
            expected = CourseName("テスト科目")
            self.assertEqual(actual, expected)
        with self.subTest(msg="day_of_week"):
            actual = test_course.day_of_week
            expected = DayOfWeek.MONDAY
            self.assertEqual(actual, expected)
        with self.subTest(msg="period"):
            actual = test_course.period
            expected = Period(1)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
