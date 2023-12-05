import time
import random
import sys
from threading import Thread

from waiters import Waiter
from kitchen import Kitchen
from tables import Table
from timeSimulator import TimeSimulator
import config


class Cafe():
  def __init__(self, tables_count, waiters_count):
    self.tables_count = tables_count
    self.waiters_count = waiters_count
    self.money = config.BALANCE

    self.task_manager = []
    self.Tables = []
    self.Waiters = []
    self.Kitchen = None

  def add_new_task(self, new_task):
    self.task_manager.append(new_task)
  
  def delete_task(self, task_to_delete):
    if task_to_delete in self.task_manager:
      self.task_manager.remove(task_to_delete)
    else:
      # trying to delete after first time if it was simple error
      if task_to_delete in self.task_manager:
        self.task_manager.remove(task_to_delete)
      else:
        # something wrong if unable to delete the task
        print("(WARNING) Unable to delete task")


  def add_new_table(self, table):
    self.Tables.append(table)

  def add_new_waiter(self, waiter):
    self.Waiters.append(waiter)

  def add_kitchen(self, kitchen):
    self.Kitchen = kitchen

  def add_money(self, amount):
    self.money += amount
    print(f"(Cafe) Balance update: {self.money}")
  
  def subtract_money(self, amount):
    self.money -= amount
    print(f"(Cafe) Balance update: {self.money}")


  def get_tables_count(self):
    return self.tables_count
  
  def get_tables_reference(self):
    return self.Tables
  
  def get_waiters_count(self):
    return self.waiters_count

  def get_waiters_reference(self):
    return self.Waiters
  
  def get_kitchen(self):
    return self.Kitchen
# ------------------------------------------------

def sleep_function():
  time.sleep(0)

def create_tables(Main_Cafe):
  tables_count = Main_Cafe.get_tables_count()
  
  for i in range(tables_count):
    table_number = i + 1
    capacity = random.randint(config.MINIMUM_TABLE_CAPACITY, config.MAXIMUM_TABLE_CAPACITY)
    new_table = Table(table_number, capacity, Main_Cafe)
    Main_Cafe.add_new_table(new_table)

    # print(f"New table has been created {new_table.__dict__}")
    sleep_function()
    
def create_waiters(Main_Cafe):
  waiters_count = Main_Cafe.get_waiters_count()

  for i in range(waiters_count):
    waiter_id = i + 1
    new_waiter = Waiter(waiter_id, Main_Cafe, config.WALKING_TIME)
    Main_Cafe.add_new_waiter(new_waiter)

    # print(f"New waiter has been created {new_waiter.__dict__}")
    sleep_function()

def create_kitchen(Main_Cafe):
  new_kitchen = Kitchen(Main_Cafe)
  Main_Cafe.add_kitchen(new_kitchen)
  # print(f"Kitchen has been created: {new_kitchen.__dict__}")

  # works till the end of the program
  new_kitchen.wait_for_order()
  

# has its own thread
# at random will call function under this one
# simulates customers arrive at random time
def randomizing_new_customers(Main_Cafe, Time_Simulator):
  minTime = config.MINIMUM_CUSTOMER_ARRIVING_TIME
  maxTime = config.MAXIMUM_CUSTOMER_ARRIVING_TIME
  
  # start the time
  starting_time_simulation_THREAD = Thread(target = Time_Simulator.start_time)
  starting_time_simulation_THREAD.start()
  customers_arriving_multiplier = Time_Simulator.get_customers_multiplier()
  # infinite loop to have customers come all the time
  while True:
    # random waiting time in sec before new customers arrive
    # multiplying on accelerator to get int first
    random_waiting_time = random.randint(minTime * config.TIME_ACCELERATOR, maxTime * config.TIME_ACCELERATOR)
    random_waiting_time = random_waiting_time / config.TIME_ACCELERATOR  # dividing back 
    
    time.sleep(random_waiting_time / customers_arriving_multiplier)
    print(f"New customers have come")
    
    # customers arriving and creating new order should be in a new thread
    customers_arrive_THREAD = Thread(target = simulate_customers_arriving, args=(Main_Cafe,))
    customers_arrive_THREAD.start()

# should be called at random by another function simulating 
# customers arrive at random time
def simulate_customers_arriving(Main_Cafe,):

  customers_arrived = random.randint(1, config.MAXIMUM_CUSTOMERS_GROUP)
  
  # array of tables in Cafe
  Tables = Main_Cafe.get_tables_reference()

  for current_table in Tables:
    if current_table.is_busy == True or current_table.is_reserved == True:  
      # skipping the table
      pass
    else:
      if current_table.capacity >= customers_arrived:
        # customers have taken the table
        current_table.customers_arrive()
        
  # if customers haven't found a table
  print(f"{customers_arrived} customers left not being able to find a place")

# create thread for each waiter and make them wait for the task
def simulate_waiters(Main_Cafe):
  for Waiter in Main_Cafe.Waiters:
    new_waiter_THREAD = Thread(target = Waiter.wait_for_new_task, args=(Main_Cafe,))
    new_waiter_THREAD.start()
  print("All waiters working")

# simulate table reservation
def simulate_reservation(Main_Cafe, Time_Simulator):
  minTime = config.MIN_RESERVATION_FREQUENCY
  maxTime = config.MAX_RESERVATION_FREQUENCY

  # infinite loop to have customers come all the time
  while True:
    # random waiting time in sec before new reservation
    # multiplying on accelerator to get int first
    random_waiting_time = random.randint(minTime * config.TIME_ACCELERATOR, maxTime * config.TIME_ACCELERATOR)
    random_waiting_time = random_waiting_time / config.TIME_ACCELERATOR  # dividing back 
    
    time.sleep(random_waiting_time)

    # customers arriving and creating new order should be in a new thread
    reserved_delay_realization_THREAD = Thread(target = reserved_delay_realization, args=(Main_Cafe, Time_Simulator))
    reserved_delay_realization_THREAD.start()

# creating time of arriving and creating order when customers come
def reserved_delay_realization(Main_Cafe, Time_Simulator):
  
  current_time = Time_Simulator.current_time
  

  # if current time + eating time + two waiting times is less than closing times
  # let table be reserved OR closing in 3 hours
  if (current_time + config.EATING_TIME/60 * config.TIME_ACCELERATOR + config.WAITING_TIME/60 * 2 * config.TIME_ACCELERATOR) < config.CLOSING_TIME or current_time < config.CLOSING_TIME + 3:
    reserved_time = random.randint(current_time + 2, config.CLOSING_TIME - 1)
    number_of_reserved_table = -1
    for current_table in Main_Cafe.Tables:
      if current_table.is_reserved == False:
        current_table.is_reserved = True
        number_of_reserved_table = current_table.table_number

        # waiting for arriving
        current_minutes = Time_Simulator.current_minutes
        minutes_left_to_hour = 60 - current_minutes

        # -1 because hour is added with 
        waiting_time = minutes_left_to_hour*60 + (reserved_time - current_time - 1)*3600
        print(f"Table {number_of_reserved_table} has been reserved. Current time: {current_time}:{current_minutes}. Reserved time: {reserved_time} ")
        time.sleep(waiting_time / config.TIME_ACCELERATOR)

        # table_number created with i+1, but to add in the Main_Cafe append() is used
        Main_Cafe.Tables[number_of_reserved_table-1].is_reserved = False
        print(f"Customers came to reserved table {current_table.table_number}, current time: {Time_Simulator.current_time}:{Time_Simulator.current_minutes}")
        Main_Cafe.Tables[number_of_reserved_table-1].customers_arrive()
        sys.exit()

      else:
        pass

    # if all tables has been reserved
    if number_of_reserved_table == -1:
      print("Reservation could not be done.")
      sys.exit()


# this is the main function of the Cafe
def start_cafe():
  # creating TimeSimulation object. Not turning on yet
  Time_Simulator = TimeSimulator(config.OPENING_TIME, config.CLOSING_TIME, config.TIME_ACCELERATOR)
  
  # creating main cafe class
  Main_Cafe = Cafe(config.TABLES_COUNT, config.WAITERS_COUNT)

  # initializing tables and waiters
  create_tables(Main_Cafe)
  create_waiters(Main_Cafe)

  # turning kitchen on
  create_kitchen_THREAD = Thread(target = create_kitchen, args=(Main_Cafe,))
  create_kitchen_THREAD.start()

  # customers arrive
  randomizing_new_customers_THREAD = Thread(target = randomizing_new_customers, args=(Main_Cafe, Time_Simulator))
  randomizing_new_customers_THREAD.start()
  
  # waiters start working

  simulate_waiters_THREAD = Thread(target = simulate_waiters, args=(Main_Cafe,))
  simulate_waiters_THREAD.start()

  # simulating reservation
  simulate_reservation_THREAD = Thread(target = simulate_reservation, args=(Main_Cafe, Time_Simulator))
  simulate_reservation_THREAD.start()


start_cafe()