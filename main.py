# Pycharm was used in the making ofthis file. It may appear different on other types of idle like lin 175 to 179
import matplotlib.pyplot as plt
import datetime
import time
from datetime import date

j = datetime.datetime.now()
now_date = j.strftime("%d/%m/%Y")
now_time = time.strftime("%H:%M")
f1 = open("Vehicle.txt")
f2 = open("Vehicle.txt", "a+")
car_details = f1.readlines()
loop = 0
Accessories_library = ['mini-fridge', 'cleaning_cloth', 'GPS navigator']


# This is the main menu of the program
def main_menu():
    print("          Vehicle Menu")
    print("Display Cars                         1")
    print("Add/delete Vehicle*                  2")
    print("Rent Vehicle: Ordinary or Premium    3")
    print("Complete Rent                        4")
    print("Reporting vehicle information*       5")
    print("Exit                                 6")

# This function displays the cars available for rent
def displayCars():
    car_count = 0
    try:
        display_vehicles = str(input("Do you want to display Rented/Available Vehicles(A/R):"))
        # The user can choose to display either rented or available vehicles
        if display_vehicles == "R":
            for line in car_details:
                individual_vehicle = line.strip().split(',')
                if display_vehicles == individual_vehicle[5]:
                    car_count = car_count + 1
                    print(line, end='')
            print("\nRented Cars are", car_count)
        elif display_vehicles == "A":
            for line in car_details:
                individual_vehicle = line.strip().split(',')
                if display_vehicles == individual_vehicle[5]:
                    car_count = car_count + 1
                    print(line, end='')
            print("\nAvailable Cars are", car_count)
        else:
            print("Invalid Input")
    except ValueError as v:
        print(v)

# This function adds a new vehicle to the list of vehicles
def Add_Vehicle():
    try:
        name = str(input("Vehicle name:"))
        types = str(input("Type:"))
        mil_allowed = float(input("Mileage allowance:"))
        rate = float(input("Daily rent rate:"))
        stats = str(input("Status:"))
        f2.write("\n" + car_id + "," + name + "," + types + "," + str(mil_allowed) + "," + str(rate) + "," + stats)
        f2.close()
    except ValueError as error:
        print(error)

# This function deletes a vehicle from the list of vehicles
def Delete_Vehicle():
    car_lis = []
    for line in car_details:
        individual_vehicle = line.strip().split(',')
        f2.close()
        if individual_vehicle[0] != car_id:
            car_lis.append(individual_vehicle)
    f3 = open("Vehicle.txt", 'w')
    for data in car_lis:
        car_data = (data[0] + ',' + data[1] + ',' + data[2] + ',' + data[3] + ',' + data[4] + ',' + data[5] + '\n')
        f3.write(car_data)
    f3.close()

# This function checks if matplotlib is installed, and if not, installs it
def math_matploter():
    try:
        import matplotlib
    except:
        import os
        os.system("python -m pip install -U matplotlib")

# This function plots the number of vehicles of each type and the income earned
def Graph_Plotter():
    car_dic = {}
    f3 = open("income earned.txt")
    ordinary = 0
    premium = 0
    # This function counts the number of ordinary and premium vehicles
    for line in car_details:
        individual_vehicle = line.strip().split(",")
        if individual_vehicle[2] == 'O':
            ordinary = ordinary + 1
        else:
            premium = premium + 1
    # This function plots the number of vehicles of each type
    d1 = {'ordinary': ordinary, 'premium': premium}
    keys = d1.keys()
    values = d1.values()
    plt.title("Display the number of vehicles of each type")
    plt.bar(keys, values)
    plt.show()
    # This function plots the income earned
    content12 = f3.readlines()
    for line in content12:
        individual_vehicle1 = line.strip().split(",")
        car_dic.update({individual_vehicle1[0]: float(individual_vehicle1[1])})
    keys2 = car_dic.keys()
    values2 = car_dic.values()
    plt.plot(keys2, values2)
    plt.title("Income earned")
    plt.xlabel("months")
    plt.ylabel("profit")
    plt.show()
    f3.close()

# This function rents a vehicle to a user
def rentVehicle():
    count = 0
    checker = 0
    try:
        # This function checks if the vehicle is available for rent
        vehicle_id = str(input("Vehicle id: "))
        for line in car_details:
            individual_vehicle = line.strip().split(",")
            if individual_vehicle[0] == vehicle_id and individual_vehicle[5] == "A":
                user_id = input("Renter's ID: ")
                # This function checks if the user ID is valid
                if len(user_id) != 11:
                    print(str(user_id) + " is an Invalid renter Id")
                    count = count + 1
                    break
                # This function checks if the vehicle is available for rent
                odometer_no = int(input("Odometer reading at the time of renting the vehicle: "))
                print(vehicle_id, "is rented to ", user_id)
                checker = checker + 1
                # This function checks if the odometer reading is valid
                if individual_vehicle[2] == "P":
                    print("Available accessories")
                    for i in Accessories_library:
                        print("->" + i)
                    add_on = str(input("Do you want to select accessories(Y/N): "))
                    # This function checks if the user wants to select accessories
                    if add_on == "Y":
                        print("         ******************* Vehicle Details ***************************         ")
                        print("vehicle ID=" + individual_vehicle[0] + "|" + "Description=" + individual_vehicle[1] + "|"
                              , "Daily Rate=" + format(float(individual_vehicle[4]), ".1f") + "|" + "accessories = 20.0"
                              + "|" + "Status=R\nRenter ID=" + user_id, "Date/time of rent=" + now_date, now_time
                              , "rent starting odometer=" + str(odometer_no))
                    elif add_on == 'N':
                        print("\t\t\t******************* Vehicle Details ***************************")
                        print("vehicle ID=" + individual_vehicle[0] + "|" + "Description=" + individual_vehicle[1] + "|"
                              , "Daily Rate=" + format(float(individual_vehicle[4]), ".1f") + "|" + "Status=R" + "|"
                              "\nRenter ID=" + user_id + "|" + "Date/time of rent=" + now_date, now_time + "|"
                              + "rent starting odometer=" + str(odometer_no))
                    # This function checks if the user input is valid
                    else:
                        print("invalid input. Please choose 'Y' or 'N'")
                        break
                # This function prints the vehicle details
                else:
                    print("\t\t\t******************* Vehicle Details ***************************")
                    print("vehicle ID=" + individual_vehicle[0] + "|" + "Description=" + individual_vehicle[1] + "|"
                          , "Daily Rate=" + format(float(individual_vehicle[4]), ".1f") + "|" + "Status=R" + "|" 
                          "\nRenter ID=" + user_id + "|" + "Date/time of rent=" + now_date, now_time + "|"
                          + "rent starting odometer=" + str(odometer_no))
                file = open("Vehicle.txt", "r")
                f_out = open("Vehicle.txt", "a")
                replacement = ""
                # This function updates the vehicle status to rented
                for line in file:
                    line = line.strip()
                    if individual_vehicle[1] in str(line):
                        changes = line.replace(",A", ",R")
                        replacement = replacement + changes + "\n"
                        f_out.write(replacement)
                        f_in = open("Vehicle.txt", "w")
                        f_in.close()
                    else:
                        f_out.write(line + "\n")
                file.close()
                f_out.close()

                # This function writes the rental details to a file
                class Format:
                    back = "\033[0m"
                    under_line = "\033[4m"

                print(Format.under_line + "Renting vehicle is successful" + Format.back)
                
                # This function writes the rental details to a file
                def rentDetails(filename):
                    f4 = open(filename, "a")
                    f4.write(individual_vehicle[0] + "," + user_id + "," + j.strftime("%d/%m/%Y") + ","
                             + time.strftime("%H:%M") + "," + str(odometer_no))
                    if add_on == "Y":
                        f4.write("," + "20.0" + "\n")
                    else:
                        f4.write("\n")
                    f4.close()

                rentDetails("rentVehicle.txt")

    except ValueError as v:
        print(v)
    except FileNotFoundError as v:
        print(v)


# This function completes the rental process and calculates the rental charges
def RentComplete():
    global car_id
    count = 0
    tester = 0
    try:
        # This function checks if the vehicle is available for rent
        car_id = str(input("Vehicle id: "))
        for line in car_details:
            individual_vehicle = line.strip().split(",")
            if individual_vehicle[0] == car_id and individual_vehicle[5] == "R":
                user_id = input("Renter's ID: ")
                if len(user_id) != 11:
                    print(str(user_id) + " is an Invalid renter Id")
                    count = count + 1
                    break
                # Calculating the distance taken
                while tester == 0:
                    odometer_initial = int(input("Odometer reading at the time of renting the vehicle: "))
                    odometer_currently = int(input("Odometer reading currently: "))
                    try:
                        distance_taken = odometer_currently - odometer_initial
                        if distance_taken <= 0:
                            raise Exception
                        else:
                            # Calculating the time rented
                            year_initial = int(input("Year rented: "))
                            month_initial = int(input("Month rented: "))
                            day_initial = int(input("Day rented: "))
                            w = j.strftime("%d,%m,%Y")
                            year_final = int(w[6:10])
                            month_final = int(w[3:5])
                            day_final = int(w[:2])
                            initial_time = date(year_initial, month_initial, day_initial)
                            current_time = date(year_final, month_final, day_final)
                            time_rented = current_time - initial_time
                            time_rented_days = int(time_rented.days)
                            # Checks if user had assesories & calculates the rental charges
                            if individual_vehicle[2] == "P":
                                accessory_choice = str(input("Did you select the (Y/N)accessories:"))
                                if accessory_choice == "Y":
                                    amount_charged = (time_rented_days * float(individual_vehicle[4])) \
                                                     + (distance_taken * 0.025) + (time_rented_days * 20)
                                    amount_charged1 = format(amount_charged, '.2f')
                                    # Prints the vehicle & renters details for premium vehicles with accessories
                                    print("     ******************* Vehicle Details ***************************     ")
                                    print("vehicle ID=" + individual_vehicle[0] + "|" + "Description="
                                          , individual_vehicle[1] + "|" + "Daily Rate="
                                          + format(float(individual_vehicle[4]), ".1f") + "|" + "Accessories=20.0")
                                    print("\nRenter ID=" + car_id + "|" + "Date/time of return=" + now_date, now_time
                                          + "|" + "rent starting\nodometer=" + str(odometer_initial) + "|"
                                          + "rent end odometer=" + str(odometer_currently) + "|" + "Kms.run="
                                          + str(distance_taken) + "|" + "Rental charges=" + amount_charged1 + "€")
                                # Prints the vehicle & renters details for premium vehicles without accessories                                 
                                elif accessory_choice == "N":
                                    amount_charged = (time_rented_days * float(individual_vehicle[4])) \
                                                     + (distance_taken * 0.020)
                                    amount_charged1 = format(amount_charged, '.2f')
                                    print("     ******************* Vehicle Details ***************************     ")
                                    print("vehicle ID=" + individual_vehicle[0] + "|" + "Description="
                                          , individual_vehicle[1] + "|" + "Daily Rate="
                                          + format(float(individual_vehicle[4]), ".1f") + "|" + "Accessories=0.0")
                                    print("\nRenter ID=" + user_id + "|" + "Date/time of return=" + now_date, now_time
                                          + "|" + "rent starting\nodometer=" + str(odometer_initial) + "|"
                                          + "rent end odometer=" + str(odometer_currently) + "|" + "Kms.run="
                                          + str(distance_taken) + "|" + "Rental charges=" + amount_charged1 + "€")
                                else:
                                    print("invalid input. Please choose 'Y' or 'N'")
                                    break
                            # Calculates the rental charges
                            else:
                                amount_charged = (time_rented_days * float(individual_vehicle[4])) \
                                                 + (distance_taken * 0.020)
                                amount_charged1 = format(amount_charged, '.2f')
                                # Prints the vehicle & renters details for ordinary vehicles
                                print("     ******************* Vehicle Details ***************************      ")
                                print("vehicle ID="+individual_vehicle[0] + "|" + "Description=", individual_vehicle[1]
                                      + "|" + "Daily Rate=" + format(float(individual_vehicle[4]), ".1f") + "|"
                                      + "Accessories=0.0")
                                print("\nRenter ID=" + car_id + "|" + "Date/time of return=" + now_date, now_time + "|"
                                      + "rent starting\nodometer=" + str(odometer_initial) + "|" + "rent end odometer="
                                      + str(odometer_currently) + "|" + "Kms.run=" + str(distance_taken) + "|"
                                      + "Rental charges=" + amount_charged1 + "€")
                            # This function updates the vehicle status to available
                            file = open("Vehicle.txt", "r")
                            f_out = open("Vehicle.txt", "a")
                            replacement = ""
                            for line in file:
                                line = line.strip()
                                if individual_vehicle[1] in str(line):
                                    changes = line.replace(",R", ",A")
                                    replacement = replacement + changes + "\n"
                                    f_out.write(replacement)
                                    f_in = open("Vehicle.txt", "w")
                                    f_in.close()
                                else:
                                    f_out.write(line + "\n")
                            file.close()
                            f_out.close()
                            print("Car", car_id, "is returned")
                            f5 = open("Transactions.txt", "a")
                            f5.write("\n" + individual_vehicle[0] + "," + user_id + "," + j.strftime("%d/%m/%Y")
                                        + " " + time.strftime("%H:%M") + "," + amount_charged1)
                            f5.close()
                            tester = tester + 1
                    except Exception:
                        print(odometer_currently, "must always be greater than", odometer_initial)

    except ValueError as v:
        print(v)
    except Exception:
        if count == 0:
            print(car_id, "does not exist or is not available for rent")
    else:
        pass

math_matploter()
# This function checks if the user input is valid
while loop != 6:
    main_menu()
    # Displays the main menu
    try:
        user_choice = int(input("Pick an option:"))
        if user_choice == 1:
            displayCars()
        elif user_choice == 2:
            try:
                car_id = str(input("Vehicle id: "))
                edit_vehicle = str(input("Add new vehicle or delete existing vehicle(A/D):"))
                if edit_vehicle == "A":
                    Add_Vehicle()
                elif edit_vehicle == "D":
                    Delete_Vehicle()
            except ValueError as error:
                print(error)
        elif user_choice == 3:
            rentVehicle()
        if user_choice == 4:
            RentComplete()
        elif user_choice == 5:
            Graph_Plotter()
        elif user_choice == 6:
            print("Thanks for using Car Rental System. Bye! Bye!")
            break
        else:
            print("Invalid input")
    except ValueError as error:
        print(error)
    except TypeError:
        print("Invalid input")
