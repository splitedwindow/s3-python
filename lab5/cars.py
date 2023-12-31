import sys

file = open('./database.csv')

# headers from the file
lines = file.readlines()
header_line = lines[0]
header = header_line.split(',')
# erase '\n' from the last element
header[len(header) - 1] = header[len(header) - 1].strip()


cars = []
index = 1
for line in lines:
  if index == 1:
    index += 1
  else:
    line_dict = line.split(',')
    line_dict[len(line_dict) - 1] = line_dict[len(line_dict) - 1].strip()
    cars.append(line_dict)


# read all the cars


while True:
  print("Enter action you want to perform by number:")
  print("1. Print cars.")
  print("2. Search for car by criteria.")
  print("3. Change one of the fields.")
  print("4. Delete car form the database.")
  print("5. Average year of the mark") # additional points
  print("6. Exit.")
  answer = input(" > ")

  if answer == '1':
    i = 1
    for car in cars:
      line = ', '.join(car)
      print(i, line)
      i = i + 1
    print("\n\n")
  elif answer == '2':
    print("Search by:\n1. Brand.\n2. Model.\n3. Year.\n4. Color.")
    findByChoice = input(" > ")

    modelsToShow = []
    empty = True

    # find by brand
    if findByChoice == '1':
      findByBrand = input("Enter the brand > ")
      print("\n\n")
      for car in cars:
        if car[0] == findByBrand:
          empty = False
          modelsToShow.append(car)
    # find by Model
    elif findByChoice == '2':
      findByModel = input("Enter the model > ")
      print("\n\n")

      for car in cars:
        if car[1] == findByModel:
          empty = False
          modelsToShow.append(car)
    # find by year
    elif findByChoice == '3':
      findByYear = input("Enter the year > ")
      print("\n\n")

      for car in cars:
        if car[2] == findByYear:
          empty = False
          modelsToShow.append(car)
    #find by color
    elif findByChoice == '4':
      findByColor = input("Enter the color > ")
      print("\n\n")

      for car in cars:
        if car[3] == findByColor:
          empty = False
          modelsToShow.append(car)


    # Print the cars found by criteria if it's not empty
    if empty:
      print("\n\nNothing was found by this input.")
    else:
      for car in modelsToShow:
          line = ' '.join(car)
          print(line)
  elif answer == '3':
    i = 1
    for car in cars:
      line = ' '.join(car)
      print(i, line)
      i = i + 1
    print("\n\n")
    print("Choose car to change by number.")
    carToChange = input(" > ")

    try:
      carToChange = int(carToChange)
      countOfCars = len(cars)
      if carToChange > countOfCars:
        print("Wrong input")
      else:
        print("Choose field to change.")
        print("1. Brand.\n2. Model.\n3. Year.\n4. Color.")
        fieldToChange = input(" > ")

        try:
          fieldToChange = int(fieldToChange)
          if fieldToChange < 1 and fieldToChange > 4:
            print("Wrong input")
          else:
            newFieldData = input("Enter new field data > ")
            cars[carToChange-1][fieldToChange-1] = newFieldData

            fileToSave_dict = [header] + cars
            fileToSave = ''
            for line in fileToSave_dict:
              text_line = ''
              for word in line:
                text_line += word + ','
              
              text_line = text_line[:-1]
              text_line = text_line + '\n'

              fileToSave += text_line

            print(fileToSave)

            with open('database.csv', 'w', newline='') as file_change_and_save:
              file_change_and_save.write(fileToSave)

        except ValueError:
          print("Wrong input")

    except ValueError:
      print("Wrong input")

  elif answer == '4':
    i = 1
    for car in cars:
      line = ', '.join(car)
      print(i, line)
      i = i + 1
    carToDelete = input("Choose car to delete > ")

    try:
      carToDelete = int(carToDelete)
      if carToDelete < 1 and carToDelete > len(cars):
        print("Wrong input")
      else:
        del cars[carToDelete-1]
        fileToSave_dict = [header] + cars
        fileToSave = ''
        for line in fileToSave_dict:
          text_line = ''
          for word in line:
            text_line += word + ','
          
          text_line = text_line[:-1]
          text_line = text_line + '\n'

          fileToSave += text_line

        print(fileToSave)

        with open('database.csv', 'w', newline='') as file_change_and_save:
          file_change_and_save.write(fileToSave)

    except ValueError:
      print("Wrong input")

    print("\n\n")

  elif answer == '5':
    print("Enter car brand to get the average year > ")
    car_brand = input()

    car_brand_exists = False
    for car in cars:
      if car[0] == car_brand:
        car_brand_exists = True
    
    if not car_brand_exists:
      print("Car brand doesn't exist.")
    else:
      sum_of_years = 0
      years_of_chosen_brand = []
      for car in cars:
        if car[0] == car_brand:
          years_of_chosen_brand.append(int(car[2]))
          sum_of_years += int(car[2])

      average_year = sum_of_years/len(years_of_chosen_brand)

      print(f"Average year of {car_brand} is {average_year}")
      
      
  elif answer == '6':
    exit()
  else:
    print("Wrong input")



"""
Brand,Model,Year,Color
Koenigsegg,Jesko,2022,White
Lexus,LFA,2012,Black
Hummer,H1,2022,Grey
Porsche,911 GT3 RS,2023,Grey
Porsche,718 Cayman GT4,2021,Yellow
"""