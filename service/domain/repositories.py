from abc import ABC, abstractmethod
from typing import List, Optional
from .models import Employee

class EmployeeRepository(ABC):
    @abstractmethod
    def get_employees(self, club_id: str) -> List[Employee]:
        pass

    @abstractmethod
    def get_employee_by_id(self, club_id: str, employee_id: str) -> Optional[Employee]:
        pass
