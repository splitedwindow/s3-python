# Менеджер завдань
# Створіть консольну програму для управління завданнями (туду-ліст). 
# Завдання повинні мати назву, опис, пріоритет та статус 
# (наприклад, 'нове', 'у процесі', 'виконане'). Реалізуйте 
# функціональність для додавання, видалення, редагування 
# та пошуку завдань. Використайте списки та словники для 
# організації даних.


import sys

status = ['To do', 'In process', 'Done']
priority = ['Low', 'Medium', 'High']


class TodoList():
  def __init__(self, statusList, priorityList):
    self.statusList = statusList
    self.priorityList = priorityList
    self.todos = [
      {
        'name': 'Task 1',
        'description': 'Description for the task',
        'priority': 'Low',
        'status': 'To do'
      }
    ]
  
  def add_new_task(self, new_task):
    self.todos.append(new_task)
  
  def delete_task(self, index):
    del self.todos[index]
    print('Task deleted')
  
  def change_priority(self, index, new_priority_index):
    print(self.todos[index])
# end of classs ------------------------------------------------

def add_task(Todolist):
  # initializing dictionary
  task = {}

  name = input('Enter name of the task > ')
  # empty string handle
  while name.strip() == '':
    name = input('Wrong input, try again > ')
  
  print('Enter description of the task.\n\t > ')
  description = input()
  # empty string handle
  while description.strip() == '':
    description = input('Wrong input, try again > ')
  
  print('Choose priority of the task by number:')
  output_numbering = 1
  # empty string handle
  for i in Todolist.priorityList:
    print(f'{output_numbering}. {i}')
    output_numbering += 1
  
  priority = input(" > ")

  print(f"1{priority}1")
  # print choices
  while priority != '1' and priority != '2' and priority != '3':
    print("Wrong input, try again")
    priority = input(" > ")
  
  task = {
    'name': name,
    'description': description,
    'priority': priority,
    'status': Todolist.statusList[0]
  }

  Todolist.add_new_task(task)
# add_task end ---------------------------------------------------------

def print_list(Todolist):
  show_index = 1

  for task in Todolist.todos:
    display_name = task['name']
    display_status = task['status']
    display_priority = task['priority']
    display_description = task['description']
    print(f"\n\n{show_index}. {display_name} | {display_priority} | {display_status}")
    print(f"\tDescription:\n\t{display_description}")
    show_index += 1
# end print_list ----------------------------------------------------------

def delete_task(Todolist):

  while True:
    try:
      task_index = int(input("Choose task by number > "))
      task_index -= 1
      TodoList.delete_task(task_index)
    except ValueError:
      print(f"Wrong input")
      
def chagne_task(Todolist):

  while True:
    try:
      change_task_index = int(input("Choose task by number > "))
      if change_task_index < 0:
        print("Wrong input")
        sys.exit()
      change_task_index -= 1

      print(f"Choose what to change by number:")
      print("1. Name\n2. Description.\n3. Priority.\n4. Status")
      change_field_index = input(" > ")

      while change_field_index != '1' and change_field_index != '2' and change_field_index != '3' and change_field_index != '4':
        print("Wrong input, try again")
        change_field_index = input(" > ")

      field_name = ''
      if change_field_index == '1':
        field_name = 'name'

      elif change_field_index == '2':
        field_name = 'description'

      elif change_field_index == '3':
        field_name = 'priority'
        
      elif change_field_index == '4':
        field_name = 'status'
      else:
        print("Error occured")
        sys.exit()
      
      current_task = Todolist.todos[change_task_index]
      new_data = input("Enter new name > ")
      while new_data.strip() == '':
        print()
        new_data = input("Wrong input, try again > ")
      current_task[field_name] = new_data

      print("Task has been changed")

    except ValueError:
      print(f"Wrong input")

def find_by_name(Todolist):
  show_index = 1
  search_name = input("Search is on, enter name of the task > ")
  for task in Todolist.todos:
    if search_name in task['name']:
      display_name = task['name']
      display_status = task['status']
      display_priority = task['priority']
      display_description = task['description']
      print(f"\n\n{show_index}. {display_name} | {display_priority} | {display_status}")
      print(f"\tDescription:\n\t{display_description}")
      show_index += 1


def start():
  Todolist = TodoList(status, priority)
  print('Todo list has been created, enter number for functions:')

  while True:

    print('1. Print list.')
    print('2. Add new task.')
    print('3. Delete task.')
    print('4. Change task.')
    print('5. Find task by name.')
    print('6. Exit.')
    level_one_answer = input("\n > ")

    # handle choice
    if level_one_answer == '1':
      print_list(Todolist)
    elif level_one_answer == '2':
      add_task(Todolist)
    elif level_one_answer == '3':
      print_list(Todolist)
      delete_task(Todolist)
    elif level_one_answer == '4':
      print_list(Todolist)
      chagne_task(Todolist)
    elif level_one_answer == '5':
      print_list(Todolist)
      find_by_name(Todolist)
    elif level_one_answer == '6':
      sys.exit
    else: 
      print('Wrong input.')


start()


# display_task(task)
