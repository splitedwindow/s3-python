exit = False

num1 = float(input("Enter first number > "))
num2 = float(input("Enter second number > "))

while exit == False:
  
  operation = input("Choose an operation by number: \n1. Compare numbers.\n2. Change type of the number.\n3. Change number.\n4. Add numbers (+).\n5. Subtract numbers (-).\n6. Multiply (*)\n7. Divide (÷)\n8. Exit.\n > ")

  
  match operation:
    # Compare numbers
    case "1":
      if(num1 > num2):
        print('Fist number is higher: ', num1, ' > ', num2)
      elif(num2 > num1):
        print('Second number is higher: ', num2, ' > ', num1)
      elif(num1 == num2):
        print("Numbers are equal: ", num1 , " = ", num2)
      break
    # Change type of number
    case "2":
      selected = input("Choose 1 or 2 number to change type > ")
      while selected != "1" or selected != "2":
        selected = input("That's far from 1 and 2 on the keyboard... try again > ")
      match selected:
        # Change type of first number
        case '1':
          changeType = input("Choose type to change into:\n1. Float.\n2.Int\n > ")
          if changeType == '1':
            num1 = float(num1)
            break
          elif changeType == '2':
            num1 = int(num1)
            break
          # Change type of second number
        case '2':
          changeType = input("Choose type to change into:\n1. Float.\n2.Int\n > ")
          if changeType == '1':
            num2 = float(num2)
            break
          elif changeType == '2':
            num2 = int(num2)
            break
    # Change number
    case '3':
      numberToChange = input("Choose number to change 1 or 2 > ")
      while numberToChange != '1' or numberToChange != '2':
        numberToChange = input(":) 1 or 2 > ")
      # Change first number
      if numberToChange == '1':
        num1 = float(input("Enter first number > "))
        break
      # Change second number
      elif numberToChange == '2':
        num2 = float(input("Enter second number > "))
        break
    # Add numbers
    case '4':
      print('Added numbers equal to ', num1 + num2)
      break
    # Subtract numbers
    case '5':
      print('Subtracted numbers equal to ', num1 - num2)
      break
    # Multiply numbers
    case '6':
      print('Multiplied numbers equal to ', num1 * num2)
      break
    # Divide numbers
    case '7':
      print('Divided numbers equal to ', num1 - num2)
      break
    case '8':
      exit = True
      break

print("\n\n☃\n\n")


# i think this doesn't work   
      
      

      