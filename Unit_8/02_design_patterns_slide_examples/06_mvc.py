
# Model
class Pizza:
    def __init__(self, name, price_chf):
        self.name = name
        self.price_chf = price_chf


# Data access
class PizzaDAO:
    def list_menu(self):
        return [
            Pizza("Diavola", 16.50),
            Pizza("Funghi", 15.00),
        ]


# Application service
class PizzaService:
    def __init__(self, pizza_dao):
        self.pizza_dao = pizza_dao

    def list_menu(self):
        return self.pizza_dao.list_menu()


# Controller
class ShoppingController:
    def __init__(self, pizza_service):
        self.pizza_service = pizza_service

    def menu(self):
        return self.pizza_service.list_menu()


# View
class Pages:
    def __init__(self, shopping_controller):
        self.shopping_controller = shopping_controller

    def show_menu(self):
        for pizza in self.shopping_controller.menu():
            print(pizza.name, pizza.price_chf)


def main():
    pages = Pages(ShoppingController(PizzaService(PizzaDAO())))
    pages.show_menu()


if __name__ == "__main__":
    main()