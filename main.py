from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
menu=Menu()
# print (menu.get_items())

want_coffee=True
while want_coffee:
  answer=input(f"What would you like? ({menu.get_items()}):")
  if answer=="off":
    want_coffee = False
  elif answer=="report":
    coffee_maker.report()
  else:
    order=menu.find_drink(answer)
    print(order)

 
    is_resource_sucess=coffee_maker.is_resource_sufficient(order)
    # money_machine.process_coins()
    is_payment_successful=money_machine.make_payment(order.cost)
    
    if is_resource_sucess and is_payment_successful:
      coffee_maker.make_coffee(order)
    # else:
    #   print("gabisa")
    #   want_coffee = False
      