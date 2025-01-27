import unittest
from unittest.mock import patch, MagicMock
from app.infrastructure.one_c_adapter import OneCAdapter
from app.config import Config
from app.domain.models import Employee

class TestOneCAdapter(unittest.TestCase):
    @patch('requests.post')
    def test_get_employees_success(self, mock_post):
        # Настройка mock-ответа
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "Return": [
                {"Специалист": "1", "Имя": "John", "Фамилия": "Doe", "Телефон": "123", "Фото": "http://example.com/image.jpg"},
                {"Специалист": "2", "Имя": "Jane", "Фамилия": "Smith", "Телефон": "456", "Фото": ""}
            ]
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        # Создание экземпляра адаптера
        config = Config()
        adapter = OneCAdapter(config)

        # Вызов тестируемого метода
        employees = adapter.get_employees("test_club_id")

        # Проверки
        self.assertEqual(len(employees), 2)
        self.assertEqual(employees[0].id, "1")
        self.assertEqual(employees[0].name, "John")
        self.assertEqual(employees[0].last_name, "Doe")
        self.assertEqual(employees[0].phone, "123")
        self.assertEqual(employees[0].image_url, "http://example.com/image.jpg")
        self.assertEqual(employees[1].id, "2")
        self.assertEqual(employees[1].name, "Jane")
        self.assertEqual(employees[1].last_name, "Smith")
        self.assertEqual(employees[1].phone, "456")
        self.assertEqual(employees[1].image_url, "")

    @patch('requests.post')
    def test_get_employees_request_error(self, mock_post):
        # Настройка mock-ответа с ошибкой
        mock_post.side_effect = requests.exceptions.RequestException("Test Error")

        # Создание экземпляра адаптера
        config = Config()
        adapter = OneCAdapter(config)

        # Вызов тестируемого метода
        employees = adapter.get_employees("test_club_id")

        # Проверки
        self.assertEqual(len(employees), 0)

    @patch('requests.post')
    def test_get_employees_empty_return(self, mock_post):
        # Настройка mock-ответа
        mock_response = MagicMock()
        mock_response.json.return_value = {"Return": []}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        # Создание экземпляра адаптера
        config = Config()
        adapter = OneCAdapter(config)

        # Вызов тестируемого метода
        employees = adapter.get_employees("test_club_id")

        # Проверки
        self.assertEqual(len(employees), 0)
