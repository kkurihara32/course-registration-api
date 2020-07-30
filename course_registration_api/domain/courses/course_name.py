from course_registration_api.domain.shared.value_object import ValueObject


def _is_valid_course_name(value: str) -> bool:
    if not isinstance(value, str):
        return False
    else:
        return True


class CourseName(ValueObject):
    def __init__(self, value=None):
        if value is None or not(_is_valid_course_name(value)):
            raise RuntimeError
        else:
            super().__init__(value)
