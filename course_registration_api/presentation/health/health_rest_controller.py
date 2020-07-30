from flask import Blueprint, jsonify
from course_registration_api.presentation.health.health_resource import HealthResource


health_rest_controller_bp = Blueprint("HealthRestController", __name__)


@health_rest_controller_bp.route("/health", methods=["GET"])
def health_test():
    resource = HealthResource()
    return jsonify(resource.to_dict())
