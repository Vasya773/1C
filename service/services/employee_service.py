from typing import List, Optional
from app.domain.models import Employee
from app.domain.repositories import EmployeeRepository

class EmployeeService:
    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repository = employee_repository

    def get_all_employees(self, club_id: str) -> List[Employee]:
        return self.employee_repository.get_employees(club_id)

    def get_employee_by_id(self, club_id: str, employee_id: str) -> Optional[Employee]:
        return self.employee_repository.get_employee_by_id(club_id, employee_id)
