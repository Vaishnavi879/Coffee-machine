from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_menu=Menu()
my_coffee_maker=CoffeeMaker()
my_money_machine=MoneyMachine()
while(1):
    x=input(f"What would you like? ({my_menu.get_items()}): ")
    if(x=="report"):
        my_coffee_maker.report()
        my_money_machine.report()
    elif(x=="off"):
        print("Turning off")
        break
    else:
        if(not my_coffee_maker.is_resource_sufficient(my_menu.find_drink(x))):
            continue
        if(not my_money_machine.make_payment(my_menu.find_drink(x).cost)):
            continue
        my_coffee_maker.make_coffee(my_menu.find_drink(x))




