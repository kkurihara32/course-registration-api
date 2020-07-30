from abc import ABCMeta, abstractmethod

from course_registration_api.domain.courses.course import Course
from course_registration_api.domain.courses.course_name import CourseName


class CourseRepository(object, metaclass=ABCMeta):
    @abstractmethod
    def find_course_by_course_name(self, course_name: CourseName) -> Course:
        raise NotImplementedError

    @abstractmethod
    def register_course(self, course: Course) -> Course:
        raise NotImplementedError

    @abstractmethod
    def update_course(self, course: Course):
        raise NotImplementedError

    @abstractmethod
    def delete_course(self, course_name: CourseName):
        raise NotImplementedError
