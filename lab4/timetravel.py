import pprint

TravelList = [(2001, "9/11"), (1914, "Start of WW1"), (1918, "End of WW1"), (1939, "Start of WW2"), (1945, "End of WW2"), (1889, "Birth of Hitler")]

TravelDictionary = {

}

while True:
  print("Here are years you can visit:")
  pprint.pprint(TravelDictionary)

  getAnswer = input("1. Enter the year you want to visit\n2. Type 'exit' if you want to end the travel\n3. Type 'change' if you want to change years.\n > ")

  # If user wants to finish 
  if getAnswer == 'exit':
    break

  # User changes years
  if getAnswer == 'change':
    addOrDelete = input("Enter 'add' or 'delete' > ")
    while addOrDelete != 'add' and addOrDelete != 'delete':
      addOrDelete = input('Try again.')


    while True:
      try:
        yearEntered = int(input('Enter the year you want to travel in > '))
        break
      except ValueError:
        print('Invalid input. Please enter a valid year as an integer.')
    
    if yearEntered in TravelDictionary:
      print("The year is already in use. You go to the main menu.")
      break
    
    eventEntered = input('Enter event that happened this year > ')
    newEvent = { yearEntered: eventEntered }

    # Updating the dictionary
    newEvent = {yearEntered: eventEntered}
    TravelDictionary.update(newEvent)
  else:
    try:
      getAnswer = int(getAnswer)
      print(getAnswer, type(getAnswer))
      print("You traveled in year ", getAnswer, " and visited ", TravelDictionary[getAnswer])
    except ValueError:
      print("Error. Wrong input number")
    


    
  


  
  
  
  
