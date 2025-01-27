from abc import ABC, abstractmethod
from typing import List
from .models import Employee


class EmployeeRepository(ABC):
    @abstractmethod
    def get_employees(self, club_id: str) -> List[Employee]:
        pass
