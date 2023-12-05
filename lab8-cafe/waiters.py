import time

import config

class Waiter():
  def __init__(self, waiter_id, Main_Cafe, walking_time):
    self.waiter_id = waiter_id
    self.Main_Cafe = Main_Cafe

    self.ready_order = None
    self.order = None
    self.carrying_money = 0
    self.current_task = None
    self.walking_time = walking_time

    # waiter's position: Hall, Kitchen, Corridor
    self.position = 'Hall'
    
  # take task from the Cafe tasks manager
  def take_task(self, Main_Cafe):
    # wait if there is no task
    if len(Main_Cafe.task_manager) == 0:
      pass

    # take new task
    else:
      new_task = Main_Cafe.task_manager[0]
      # delete so other waiter don't take this task
      self.delete_task(new_task)

      self.current_task = new_task

      # task = 0 - Kitchen, task > 0 - Tables
      # task is number, having it extract Table instance to pass
      current_Table = None
      for Table in Main_Cafe.Tables:
        if Table.table_number == new_task:
          current_Table = Table
          break
      # go to table
      if new_task > 0:
        self.walk('Hall')
        self.approach_table(current_Table)
      # go to kitchen
      elif new_task == 0:
        self.walk('Kitchen')
        self.take_ready_order()

  # delete taken task
  def delete_task(self, task_to_delete):
    self.Main_Cafe.delete_task(task_to_delete)
  
  # table may be empty when waiter arrives so first is to approach it
  def approach_table(self, Table):
    if Table.is_busy == False:
      # wait for new task
      pass
    else:
      # approached table has people
      if Table.is_payed == False:
        self.new_order(Table.order)
      # approached table is payed 
      elif Table.is_payed == True:
        self.clean_table(Table)

  # waiter just wrote down new order
  def new_order(self, order):
    print(f"\t\t\t\t\t\t\t\t\t(Waiter {self.waiter_id}) Just got an order {order['table_number']}")
    self.order = order
    self.give_order_to_kitchen()
  
  # making walking take time
  def walk(self, position_to_go):
    time.sleep(self.walking_time)

    if position_to_go != self.position:
      # walking to destination
      print(f"\t\t\t\t\t\t\t\t\t(Waiter {self.waiter_id}) At {self.position} going to {position_to_go}")

      time.sleep(self.walking_time)
      self.position = 'Corridor'
      print(f"\t\t\t\t\t\t\t\t\t(Waiter {self.waiter_id}) At {self.position} going to {position_to_go}")
      
      time.sleep(self.walking_time)
      self.position = position_to_go
      print(f"\t\t\t\t\t\t\t\t\t(Waiter {self.waiter_id}) At {self.position}")

  # give new order to kitchen
  def give_order_to_kitchen(self):
    self.walk('Kitchen')
    print(f"\t\t\t\t\t\t\t\t\t(Waiter {self.waiter_id}) Gave kitchen new order: {self.order['table_number']}")
    self.Main_Cafe.Kitchen.take_new_order(self.order)
    # creating template to clean order in Waiter
    order_template = self.order
    self.order = None
    return order_template # check if this works

  
  # take order from kitchen
  def take_ready_order(self):
    ready_order = self.Main_Cafe.Kitchen.give_order_away()
    print(f"\t\t\t\t\t\t\t\t\t(Waiter {self.waiter_id}) Took a ready order")
    self.ready_order = ready_order
    self.serve_order(ready_order)

  def serve_order(self, order):
    current_Table = None
    for Table in self.Main_Cafe.Tables:
      if Table.table_number == order['table_number']:
        current_Table = Table
        break
    
    self.Main_Cafe.Tables
    current_Table.order_arrives()
    # customers left before order arrived
    if current_Table.is_busy == False:
      # if table was reserved make it not reserved
      if current_Table.is_reserved == True:
        current_Table.is_reserved = False
      self.throw_dish_away()
    else:
      # putting dishes on the table
      self.ready_order = None

  
  # throw dish away if customers left
  def throw_dish_away(self):
    print(f"\t\t\t\t\t\t\t\t\t(Waiter {self.waiter_id}) Threw dish away")
    self.ready_order = None

  # cleaning table after customers ate their food
  # is_payed should always be true in this function
  def clean_table(self, Table):
    if Table.is_payed == True:
      self.carrying_money += Table.price
      Table.is_busy = False
      Table.order = None
      Table.order_in_time = False
      Table.is_payed = False
      
      print(f"\t\t\t\t\t\t\t\t\t(Waiter {self.waiter_id}) Table {Table.table_number} has been payed {Table.price} ")

      # taking money from table 
      Table.price = 0
      self.leave_money_in_cafe()
    else:
      print(f"(Warning) Table {Table.table_number} ate food but didn't pay ")

  def wait_for_new_task(self, Main_Cafe):
    while True:

      # created to wait a bit more time so several waiters don't grab the same task
      # better would be to create array of waiting waiters
      additional_waiting_time = self.waiter_id / 100
      time.sleep(additional_waiting_time)
      self.take_task(Main_Cafe)
      time.sleep(100 / config.TIME_ACCELERATOR)

  def leave_money_in_cafe(self):
    self.Main_Cafe.add_money(self.carrying_money)
    self.carrying_money = 0
