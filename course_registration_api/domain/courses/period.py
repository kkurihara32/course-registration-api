from course_registration_api.domain.shared.value_object import ValueObject


def _is_valid_period(value: int) -> bool:
    if not isinstance(value, int):
        return False
    elif value < 1 or value > 8:
        return False
    else:
        return True


class Period(ValueObject):
    def __init__(self, value=None):
        if value is None or not(_is_valid_period(value)):
            raise RuntimeError()
        else:
            super().__init__()
