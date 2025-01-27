import requests
from requests.auth import HTTPBasicAuth
from typing import List
from app.domain.models import Employee
from app.domain.repositories import EmployeeRepository
from app.config import Config

class OneCAdapter(EmployeeRepository):
    def __init__(self, config: Config):
        self.base_url = config.ONE_C_BASE_URL
        self.login = config.ONE_C_LOGIN
        self.password = config.ONE_C_PASSWORD
        self.request_id = config.ONE_C_REQUEST_ID

    def get_employees(self, club_id: str) -> List[Employee]:
        url = self.base_url
        headers = {'Content-Type': 'application/json'}
        auth = HTTPBasicAuth(self.login, self.password)
        payload = {
            "Request_id": self.request_id,
            "ClubId": club_id,
            "Method": "GetSpecialistList",
            "Parameters": {
                "ServiceId": ""
            }
        }

        try:
            response = requests.post(url, headers=headers, auth=auth, json=payload)
            response.raise_for_status()  # Проверяем статус ответа
            data = response.json()

            employees = []
            if "Return" in data and isinstance(data["Return"], list):
                for item in data["Return"]:
                    employee = Employee(
                        id=item.get("Специалист", ""),
                        name=item.get("Имя", ""),
                        last_name=item.get("Фамилия", ""),
                        phone=item.get("Телефон", ""),
                        image_url=item.get("Фото", "")
                    )
                    employees.append(employee)
            return employees
        except requests.exceptions.RequestException as e:
            print(f"Error during request to 1C: {e}")
            return []
