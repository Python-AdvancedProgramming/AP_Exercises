class Employee:
    def __init__(self, firstname: str, lastname: str, position: str, employee_id: str) -> None:
        self.firstname: str = firstname
        self.lastname: str = lastname
        self.position: str = position
        self.employee_id: str = employee_id

    @property
    def firstname(self) -> str:
        return self._firstname

    @firstname.setter
    def firstname(self, value: str) -> None:
        if not value:
            raise ValueError("firstname can not be empty")
        self._firstname: str = str(value)

    @property
    def lastname(self) -> str:
        return self._lastname

    @lastname.setter
    def lastname(self, value: str) -> None:
        if not value:
            raise ValueError("lastname can not be empty")
        self._lastname: str = str(value)

    @property
    def position(self) -> str:
        return self._position

    @position.setter
    def position(self, value: str) -> None:
        if not value:
            raise ValueError("position can not be empty")
        self._position: str = str(value)

    @property
    def employee_id(self) -> str:
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value: str) -> None:
        if not value:
            raise ValueError("employee_id can not be empty")
        self._employee_id: str = str(value)

    # --------------------------------------------------------------
    # string representations
    # --------------------------------------------------------------
    def __str__(self) -> str:
        """A human‑readable description of the employee."""
        return f"{self.firstname} {self.lastname} ({self.employee_id}) – {self.position}"

    def __repr__(self) -> str:
        return (
            f"Employee(firstname={self.firstname!r}, lastname={self.lastname!r}, "
            f"position={self.position!r}, employee_id={self.employee_id!r})"
        )
