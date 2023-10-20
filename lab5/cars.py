import csv

file = open('./database.csv')
csvReader = csv.reader(file)

# headers from the file
header = []
header = next(csvReader)

# read all the cars
cars = []
for car in csvReader:
  cars.append(car)


while True:
  print("Enter action you want to perform by number:")
  print("1. Print cars.")
  print("2. Search for car by criteria.")
  print("3. Change one of the fields.")
  print("4. Delete car form the database.")
  print("5. Exit.")
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

            fileToSave = [header] + cars

            print(fileToSave)
            
            with open('database.csv', 'w', newline='') as csvfile:
              csv_writer = csv.writer(csvfile)

              # Write each row in the file
              for row in fileToSave:
                print(row)
                csv_writer.writerow(row)

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
        fileToSave = [header] + cars

        print(fileToSave)
        
        with open('database.csv', 'w', newline='') as csvfile:
          csv_writer = csv.writer(csvfile)

          # Write each row in the file
          for row in fileToSave:
            print(row)
            csv_writer.writerow(row)

    except ValueError:
      print("Wrong input")

    print("\n\n")

  elif answer == '5':
    exit()
  else:
    print("Wrong input")



"""
Brand,Model,Year,Color
Koenigsegg,Jesko,2022,White
Lexus,LFA,2012,Black
Hummer,H1,2022,Grey
Porsche,911 GT3 RS,2023,Grey
Porsche,718 Cayman GT4,2023,Yellow
"""