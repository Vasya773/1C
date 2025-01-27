import unittest
from app import create_app
from app.config import Config
from unittest.mock import patch

class TestTeamController(unittest.TestCase):
    def setUp(self):
        # Создание тестового приложения
        self.app = create_app(config_class=Config)
        self.client = self.app.test_client()

    @patch('app.services.employee_service.EmployeeService.get_all_employees')
    def test_get_employees_endpoint(self, mock_get_all_employees):
        # Настройка mock-сервиса
        mock_get_all_employees.return_value = [
            Employee(id="1", name="John", last_name="Doe", phone="123", image_url="http://example.com/image.jpg"),
            Employee(id="2", name="Jane", last_name="Smith", phone="456", image_url="")
        ]

        # Выполнение запроса к эндпоинту
        response = self.client.get('/team/get_employees?club_id=test_club_id')

        # Проверки
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["id"], "1")
        self.assertEqual(data[0]["name"], "John")
        self.assertEqual(data[0]["last_name"], "Doe")
        self.assertEqual(data[0]["phone"], "123")
        self.assertEqual(data[0]["image_url"], "http://example.com/image.jpg")
        self.assertEqual(data[1]["id"], "2")
        self.assertEqual(data[1]["name"], "Jane")
        self.assertEqual(data[1]["last_name"], "Smith")
        self.assertEqual(data[1]["phone"], "456")
        self.assertEqual(data[1]["image_url"], "")
        mock_get_all_employees.assert_called_once_with("test_club_id")
