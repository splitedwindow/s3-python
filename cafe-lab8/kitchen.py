import time

import config
import menu

class Kitchen():
  def __init__(self, Main_Cafe):
    self.Main_Cafe = Main_Cafe
    
    self.wait = True
    self.to_do_orders = []
    self.ready_orders = []

  def create_new_task(self):
    self.Main_Cafe.add_new_task(0)
  
  # waiter uses this function to bring new order to make
  def take_new_order(self, order):
    self.to_do_orders.append(order)

    order_price = menu.MENU[order['menu']]   # indexing may not work
    cost = order_price * (100 - config.PROFIT_MARGIN) / 100

    self.subtract_money_from_cafe(cost)
    
    print(f"(Kitchen) Kitchen has received order {order['table_number']}")
  
  # cooking to_do_orders[0] order
  def cook_order(self):
    time.sleep(config.COOKING_TIME)
    # move order from to_do_orders to ready_orders
    self.ready_orders.append(self.to_do_orders[0])
    self.to_do_orders.pop(0)

    self.create_new_task()

    print(f"(Kitchen) Order has been done")
  
  # waiter uses this function
  def give_order_away(self):
    ready_order = self.ready_orders[0]
    self.ready_orders.pop(0)
    return ready_order

  def subtract_money_from_cafe(self, cost):
    self.Main_Cafe.subtract_money(cost)
  
  def wait_for_order(self):
    while True:
      time.sleep(500 / config.TIME_ACCELERATOR)
      if len(self.to_do_orders) > 0:
        self.cook_order()
  
        
    