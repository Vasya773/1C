from flask import Flask
from app.config import Config
from app.infrastructure.one_c_adapter import OneCAdapter
from app.services.employee_service import EmployeeService
from app.api.team_controller import setup_team_controller


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    config = Config()
    one_c_adapter = OneCAdapter(config)
    employee_service = EmployeeService(one_c_adapter)

    # Регистрация blueprint-ов
    app.register_blueprint(setup_team_controller(employee_service, config))

    return app
