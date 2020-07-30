import unittest

from course_registration_api.domain.shared.value_object import ValueObject


class TestValueObject(unittest.TestCase):
    def test_initialize(self):
        with self.subTest(msg="getterの正常動作確認"):
            test_value = ValueObject("test_object")
            actual = test_value.value
            expected = "test_object"
            self.assertEqual(actual, expected)
        with self.subTest(msg="二つのオブジェクトの同値性確認"):
            test_value = ValueObject("test_object")
            other_value = ValueObject("test_object")
            actual = test_value.value == other_value.value
            self.assertTrue(actual)
        with self.subTest(msg="hash値の保持の確認"):
            test_value = ValueObject("test_object")
            actual = type(hash(test_value.value))
            expected = int
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
