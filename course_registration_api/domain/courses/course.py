from course_registration_api.domain.courses.course_name import CourseName
from course_registration_api.domain.courses.day_of_week import DayOfWeek
from course_registration_api.domain.courses.period import Period


class Course(object):
    def __init__(self,
                 course_name: CourseName,
                 day_of_week: DayOfWeek,
                 period: Period):
        self._counse_name = course_name
        self._day_of_week = day_of_week
        self._period = period

    @property
    def course_name(self):
        return self._counse_name

    @property
    def day_of_week(self):
        return self._day_of_week

    @property
    def period(self):
        return self._period
