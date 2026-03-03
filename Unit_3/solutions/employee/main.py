from employee import Employee
from register import Register


def main() -> None:
    # create some sample employees
    alice = Employee("Alice", "Anderson", "Developer", "E001")
    bob = Employee("Bob", "Brown", "Manager", "E002")
    carol = Employee("Carol", "Clark", "Designer", "E003")

    # build a register and add the employees
    reg = Register([alice, bob])
    reg.add_employee(carol)

    print(f"Register contains {len(reg)} employees:")
    for emp in reg.employees:
        print("  ", emp)

    # demonstrate a lookup
    matches = reg.find_by_lastname("Br")
    print("\nFind by lastname 'Br':", matches)


if __name__ == "__main__":
    main()
