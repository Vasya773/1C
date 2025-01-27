from flask import Blueprint, jsonify, request
from app.services.employee_service import EmployeeService
from app.config import Config

team_blueprint = Blueprint('team', __name__, url_prefix='/team')


def setup_team_controller(employee_service: EmployeeService, config: Config):
    @team_blueprint.route('/get_employees', methods=['GET'])
    def get_employees():
        club_id = request.args.get('club_id', config.DEFAULT_CLUB_ID)
        employees = employee_service.get_all_employees(club_id)

        return jsonify([
            {
                "id": employee.id,
                "name": employee.name,
                "last_name": employee.last_name,
                "phone": employee.phone,
                "image_url": employee.image_url
            }
            for employee in employees
        ])

    return team_blueprint
