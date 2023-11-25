import time
import random
import config

import menu

class Table():
  def __init__(self, table_number, capacity, Main_Cafe):
    self.table_number = table_number
    self.capacity = capacity
    self.Main_Cafe = Main_Cafe
    self.is_busy = False
    self.order = None
    self.order_in_time = False
    self.price = 0
    self.is_payed = False

  # table is being taken by the customers
  def customers_arrive(self):
    self.is_busy = True
    self.create_new_task()
    self.make_an_order()
    self.customers_waiting()

  # Cafe uses Tasks to distribute work. New task is added to queue waiting to be 
  # taken by the waiter. Table and Kitchen creates new Tasks, Waiter deletes them
  def create_new_task(self):
    self.Main_Cafe.add_new_task(self.table_number)


  # customer waiting
  def customers_waiting(self):
    # wait for "WAITING_TIME" amount
    time.sleep(config.WAITING_TIME)

    # customers leave, function order_arrives prevents it when waiter arrives
    if self.order_in_time == False:
      self.is_busy = False
      self.price = 0
      print(f"\t\t\t\t\t(Table {self.table_number}) Customers left")
      self.is_busy = False
      self.order = None
    # customers stay
    else:
    # customers received food
      self.eat()

  # make an order
  def make_an_order(self):
    self.order = {}
    self.order['table_number'] = self.table_number
    
    menu_items_count = len(menu.MENU)
    menu_choice = random.randint(1, menu_items_count)
    self.order['menu'] = menu_choice
    
    # set price based on the dish...
    self.price = menu.MENU[menu_choice]
    
    # return order to waiter
    print(f"\t\t\t\t\t(Table {self.table_number}) Ready to order")
    return self.order

  # order arrives to the table
  def order_arrives(self):
    # customers haven't left
    if self.is_busy == True:
      self.order_in_time = True

    # customers left before receiving an order
    else:
      print(f"\t\t\t\t\t(Table {self.table_number}) Customers left")
      self.order = None
      # don't forget to delete order from the waiter

  def eat(self):
    print(f"\t\t\t\t\t(Table {self.table_number}) Customers are eating")
    time.sleep(config.EATING_TIME)
    self.pay()
  
  def pay(self):
    self.is_payed = True
    print(f"\t\t\t\t\t(Table {self.table_number}) Payed and left")
    self.create_new_task()
    # waiter takes the money and makes table free