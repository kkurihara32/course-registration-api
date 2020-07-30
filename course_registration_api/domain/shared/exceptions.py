class CourseRegistrationException(RuntimeError):
    def __init__(self, message="CourseRegistration"):
        super().__init__(message)


class InvalidCourseNameException(CourseRegistrationException):
    def __init__(self, message="InvalidCourseNameException"):
        super().__init__(message)


class InvalidPeriodException(CourseRegistrationException):
    def __init__(self, message="InvalidPeriodException"):
        super().__init__(message)
