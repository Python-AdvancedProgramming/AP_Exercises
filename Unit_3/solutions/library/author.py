class Author:
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname: str = firstname
        self.lastname: str = lastname

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

    # --------------------------------------------------------------
    # string representations
    # --------------------------------------------------------------
    def __str__(self) -> str:
        """Return the author's full name."""
        return f"{self.firstname} {self.lastname}"

    def __repr__(self) -> str:
        # constructor-style repr makes it easy to recreate the object
        return f"Author(firstname={self.firstname!r}, lastname={self.lastname!r})"
