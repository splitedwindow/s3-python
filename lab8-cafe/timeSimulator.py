import time
import config

# simulates time passing from 9:00 to 21:00
# it just affects randomizing_new_customers function in cafe.py
# decreases random time of waiting before new customer arrives in crowded time
class TimeSimulator():
  def __init__(self, opening_time, closing_time, time_accelerator):
    # if = 2 customers come twice faster than always
    self.customers_arriving_frequency_multiplier = 1
    
    self.opening_time = opening_time
    self.closing_time = closing_time
    self.current_time = opening_time
    self.current_minutes = 0

    # accelerates time in time_accelerator times
    self.time_accelerator = time_accelerator

    # dinner crowded time
    self.start_dinner_peak_hour = 12
    self.end_dinner_peak_hour = 15

    # evening crowded time
    self.start_evening_peak_hour = 19
    self.end_evening_peak_hour = 21

  # time passing simulation
  def start_time(self):
    while True:
      print(f"Time: {self.current_time}:00")
      # increasing speed of one hour passing
      self.current_minutes = 0
      for i in range(59):
        time.sleep(60/self.time_accelerator)
        self.current_minutes += 1
        if(self.current_minutes < 10):
          add_zero = '0' + str(self.current_minutes)
          print(f"Time: {self.current_time}:{add_zero}")
        else:
          print(f"Time: {self.current_time}:{self.current_minutes}")
          pass
      if self.current_time < 21:
        self.current_time += 1
        self.define_peek_hours()

  # at what time should be more people  
  def define_peek_hours(self):
    if self.current_time >= self.start_dinner_peak_hour and self.current_time <= self.end_dinner_peak_hour:
      # 2 times more customers in 12:00-15:00
      self.customers_arriving_frequency_multiplier = 2
    elif self.current_time >= self.start_evening_peak_hour and self.current_time < self.end_evening_peak_hour:
      self.customers_arriving_frequency_multiplier = 3
    elif self.current_time == 21:
      # some logic
      self.current_time = 9
    else:
      self.customers_arriving_frequency_multiplier = 1
      
  
  def get_customers_multiplier(self):
    return self.customers_arriving_frequency_multiplier
    
