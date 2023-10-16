from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money = MoneyMachine()
    is_on = True
    while is_on:
        order = input(f"What would you like? {menu.get_items()}: ") \
            .strip().lower()
        if order == 'off':
            is_on = False
        elif order == 'report':
            coffee_maker.report()
            money.report()
        elif menu.find_drink(order):
            drink = menu.find_drink(order)
            if coffee_maker.is_resource_sufficient(drink) and \
                    money.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()
