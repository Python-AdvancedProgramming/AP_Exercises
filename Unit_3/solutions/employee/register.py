from typing import List

from employee import Employee


class Register:
    def __init__(self, employees: List[Employee] | None = None) -> None:
        # use the property setter so validation runs
        self.employees = employees or []

    @property
    def employees(self) -> List[Employee]:
        """A list of employees contained in the register."""
        return self._employees

    @employees.setter
    def employees(self, value: List[Employee]) -> None:
        if value is None:
            self._employees = []
            return
        if not isinstance(value, list):
            raise TypeError("employees must be a list of Employee instances")
        for item in value:
            if not isinstance(item, Employee):
                raise TypeError("all items in employees must be Employee instances")
        self._employees = value

    def add_employee(self, employee: Employee) -> None:
        """Append an employee to the collection."""
        if not isinstance(employee, Employee):
            raise TypeError("employee must be an Employee")
        self._employees.append(employee)

    def remove_employee(self, employee: Employee) -> None:
        """Remove an employee from the collection; ValueError if not present."""
        self._employees.remove(employee)

    def find_by_lastname(self, lastname: str) -> List[Employee]:
        """Return all employees whose lastname contains the given string."""
        return [e for e in self._employees if lastname.lower() in e.lastname.lower()]

    def __len__(self) -> int:
        return len(self._employees)

    # --------------------------------------------------------------
    # string representations
    # --------------------------------------------------------------
    def __str__(self) -> str:
        """A human-readable summary showing how many employees are present."""
        return f"Register with {len(self)} employee(s)"

    def __repr__(self) -> str:
        return f"Register(employees={len(self)})"
