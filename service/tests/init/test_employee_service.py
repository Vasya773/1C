import unittest
from unittest.mock import MagicMock
from app.services.employee_service import EmployeeService
from app.domain.models import Employee

class TestEmployeeService(unittest.TestCase):
    def test_get_all_employees(self):
        # Создание mock-репозитория
        mock_repo = MagicMock()
        mock_repo.get_employees.return_value = [
            Employee(id="1", name="John", last_name="Doe", phone="123", image_url="http://example.com/image.jpg"),
            Employee(id="2", name="Jane", last_name="Smith", phone="456", image_url="")
        ]

        # Создание экземпляра сервиса
        service = EmployeeService(mock_repo)

        # Вызов тестируемого метода
        employees = service.get_all_employees("test_club_id")

        # Проверки
        self.assertEqual(len(employees), 2)
        self.assertEqual(employees[0].id, "1")
        mock_repo.get_employees.assert_called_once_with("test_club_id")

    def test_get_employee_by_id_found(self):
        # Создание mock-репозитория
        mock_repo = MagicMock()
        mock_repo.get_employee_by_id.return_value = Employee(id="1", name="John", last_name="Doe", phone="123",
                                                             image_url="http://example.com/image.jpg")

        # Создание экземпляра сервиса
        service = EmployeeService(mock_repo)

        # Вызов тестируемого метода
        employee = service.get_employee_by_id("test_club_id", "1")

        # Проверки
        self.assertIsNotNone(employee)
        self.assertEqual(employee.id, "1")
        mock_repo.get_employee_by_id.assert_called_once_with("test_club_id", "1")

    def test_get_employee_by_id_not_found(self):
        # Создание mock-репозитория
        mock_repo = MagicMock()
        mock_repo.get_employee_by_id.return_value = None

        # Создание экземпляра сервиса
        service = EmployeeService(mock_repo)

        # Вызов тестируемого метода
        employee = service.get_employee_by_id("test_club_id", "2")

        # Проверки
        self.assertIsNone(employee)
        mock_repo.get_employee_by_id.assert_called_once_with("test_club_id", "2")
