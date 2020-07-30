from flask import Flask

from course_registration_api.presentation.health.health_rest_controller \
    import health_rest_controller_bp


class Initializer(object):
    @staticmethod
    def initialize():
        app = Flask("CourseRegistration")
        app.config["JSON_AS_ASCII"] = False
        app.register_blueprint(health_rest_controller_bp, url_prefix="/api/v1")
        return app
