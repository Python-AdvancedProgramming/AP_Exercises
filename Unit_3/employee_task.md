# OOP Exercise: Employee Register

In this exercise you will design and implement a small object-oriented employee register. The `solutions/employee` package in the repository contains a working reference implementation; your task is to build your own version from scratch following the requirements below.

> **Note**: Do not copy the solution files directly—this exercise is meant to be solved independently. Once you have finished your implementation, compare it with the provided `solutions/employee` package to see alternate design choices.

## Learning goals

1. Practice defining classes with attributes, properties, and validation logic.
2. Use composition by managing one object type inside another class.
3. Implement special methods such as `__str__`, `__repr__`, and `__len__`.
4. Write clear docstrings and follow good naming conventions.

---

## Requirements

You should create the following classes in a new package or module (e.g. `employee.py`, `register.py`):

### `Employee`
- Attributes:
  - `firstname` (string) - cannot be empty.
  - `lastname` (string) - cannot be empty.
  - `position` (string) - cannot be empty.
  - `employee_id` (string) - cannot be empty.
- Use properties with setters to validate all values.
- Implement `__str__` to return a human-readable description of the employee.
- Implement `__repr__` to return an unambiguous representation of the object, including all key attributes.

### `Register`
- Manage a collection of `Employee` objects.
- The constructor may receive an initial list of employees (default to empty).
- Implement an `employees` property that ensures the value is always a list of `Employee` instances and never `None`.
- Methods:
  - `add_employee(employee)` - add an `Employee` to the collection, raising `TypeError` for invalid arguments.
  - `remove_employee(employee)` - remove an employee, propagating the `ValueError` if the employee is not present.
  - `find_by_lastname(lastname)` - return a list of all employees whose last names contain the given string (case-insensitive).
- Implement `__len__` so that `len(register)` returns the number of employees.
- Implement `__str__` and `__repr__` for useful debug and display output.

---

## Optional extensions

- Add a method `find_by_position(position)` to filter employees by role.
- Support duplicate-checking based on `employee_id` before inserting new employees.

---

Good luck and have fun building your employee register!
