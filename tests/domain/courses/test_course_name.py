import unittest

from course_registration_api.domain.courses.course_name import CourseName
from course_registration_api.domain.shared.exceptions \
    import InvalidCourseNameException


class TestCourseName(unittest.TestCase):
    def test_initialize(self):
        test_name = CourseName("テスト科目")
        actual = test_name.value
        expected = "テスト科目"
        self.assertEqual(actual, expected)

    def test_intialize_with_invalid_value(self):
        with self.subTest(msg="value is Noneの場合の異常系のテスト"):
            with self.assertRaises(InvalidCourseNameException):
                CourseName()
        with self.subTest(msg="value が str 出ない場合の異常系のテスト"):
            with self.assertRaises(InvalidCourseNameException):
                CourseName(1)


if __name__ == '__main__':
    unittest.main()
