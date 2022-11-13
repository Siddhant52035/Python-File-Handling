from Main import *
from datetime import datetime, date


running = True
while running:
    user_choice = 0
    try:
        user_choice = welcome()
    except:
        print("\n")
        print("The Input should be an Integer, Please enter a number!!!!")
        # displays welcome message and returns users input
    dictionary = dic_costume()
    # retrieve the data from txt file and stores it in dictionary

    # These lists store the information of rented and returned costumes
    items_in_rent = []
    items_in_return = []
    brands_in_rent = []
    brands_in_return = []

    if user_choice == 1:                                             # If user chooses 1, we initiate the Renting procedure
        print("\n")
        print("Let's Rent a costume") 
        display_costume()                                            # This method displays all the costumes
        print("----------------------------------------------------------------------------------")
        print("\n")
    

        costume_id = valid_costumeId(dictionary)



        # The method vaild quantity returns an integer value which is stored in varialbe quantity_rented
        
        quantity_rented = valid_quantity(int(dictionary[costume_id][3]))


        items_in_rent.append(dictionary[costume_id][0])
        brands_in_rent.append(dictionary[costume_id][1])
        print("\n")
        
        name = input("Enter your name: ")
        number = 0
        while True:
            try:
                number = int(input("Enter your number:"))
                break
            except:
                print("You entered an Invalid Number")
                continue

        # Here we update the dictionary by subtracting the total number of rented costumes from total quantity
        dictionary[costume_id][3] = int(dictionary[costume_id][3])- quantity_rented

        print("\n")

        # Now we update text file by passing dictionary as parameter
        edit_file_info(dictionary)


        # Now we print the total price
        totalPrice = total_price(quantity_rented,costume_id,dictionary)

        print("Do you want to rent another costume as well ??")
        re_rent = input("Please enter 'y' if you wanna rent another costume else provide any other value:").lower()

        while re_rent == "y":
           list1 =  rent_again()
           items_in_rent.append(dictionary[list1[1]][0])
           brands_in_rent.append(dictionary[list1[1]][1])

           totalPrice = totalPrice + total_price(list1[2],list1[1],dictionary)

           print("\n")
           print("Do you want to rent another costume as well ??")
           re_rent = input("Please enter 'y' if you wanna rent another costume else provide any other value:").lower()


        print("\n")
        print("==================================================")
        print("\t\t\t\tBill Details")
        print("==================================================")
        print("Name of the Customer: ",name )
        print("Date and Time of Borrow: ", datetime.now())
        print("Contact Number of the Customer: ",number )
        print("--------------------------------------------------")

        for i in range(len(items_in_rent)):
            print("Costume rented: ",items_in_rent[i] )
            print("Brands rented: ", brands_in_rent[i])
            print("---------------------------------------------------")
        print("Total price of all the rented Costumes is: $", totalPrice)
        print(f"Thank you for using our Application {name},Here's your bill.")



        file1 = open(f"{name}.txt","w")
        file1.write("\t\tBill Details\t\t\n\n")
        file1.write(f"Name of the Customer: {name}\n")
        file1.write(f"Date and Time of Borrow: {date.today()}\n")
        file1.write(f"Contact Number of the Customer: {number}\n")
        file1.write("---------------------------------------------------\n")
        for i in range(len(items_in_rent)):
            file1.write(f"Costumes rented are: {items_in_rent[i]}\n")
            file1.write(f"Brands rented are: {brands_in_rent[i]}\n")
            file1.write("---------------------------------------------------\n")


        file1.write(f"Total price of all the rented costumes is ${totalPrice}\n")
        file1.write(f"Thank you for using our Application {name}. Here's your bill.")

        file1.close()


    elif user_choice == 2:

        print("\n")
        print("Let's Return a costume")
        display_costume()
        print("------------------------------------------------------------")
        c_id = valid_costumeId_return()
        price = 0
        v_quantity = 0
        name = ""
        number1 = 0
        while True:
            try:

                v_quantity = int(input("Enter the quantity of the costume you want to return:"))
                while v_quantity <= 0:
                    print("Quantity can't be 0 or negative, Please Enter a valid quantity")
                    v_quantity = int(input("Enter the quantity of the costume you want to return:"))

                items_in_return.append(dictionary[c_id][0])
                brands_in_return.append(dictionary[c_id][1])

                dictionary[c_id][3] = int(dictionary[c_id][3]) + v_quantity

                print("\n")
                edit_file_info(dictionary)


                name = input("Enter your name: ")
                while True:
                    try:

                        number1 = int(input("Enter your number:"))
                        break
                    except:
                        print("You entered an Invalid Number")
                        continue
                break


            except:
                print("Invalid Input, Please Try again!!")
                continue

        price = 0
        while True:
            try:
                print("\n")
                days_kept = int(input("How many days did you keep the costume for ?"))

                if days_kept <= 5:
                    price = 0

                else:

                    price = (days_kept - 5) * v_quantity * 5
                break
            except Exception as e:
                print("Invalid Input, Please Try again!!")
                continue





        print("\n")
        print("Do you want to return another custome as well ??")
        re_return = input("Please enter 'y' if you want to return another costume else provide any other value:").lower()

        while re_return == "y":


          list2 = return_again()
          items_in_return.append(dictionary[list2[0]][0])
          brands_in_return.append(dictionary[list2[0]][1])

          price = price + list2[1]



          print("Do you want to return another custome as well ??")
          re_return = input("Please enter 'y' if you want to return another costume else provide any other value:").lower()

        print("\n")
        print("==================================================")
        print("\t\t\t\tBill Details")
        print("==================================================")
        print("Name of the Customer: ",name )
        print("Date and Time of Return: ", datetime.now())
        print("Contact Number of the Customer: ", number1)
        print("--------------------------------------------------")

        for i in range(len(items_in_return)):

            print("Costume returned: ",items_in_return[i] )
            print("Brands returned: ", brands_in_return[i])
            print("---------------------------------------------------")
        print("Total fine of all the returned Costumes is: $", price)
        print(f"Thank you for using our Application {name}. Here's your bill.")

        file1 = open(f"{name}.txt", "w")
        file1.write("\t\tBill Details\t\t\n\n")
        file1.write(f"Name of the Customer: {name}\n")
        file1.write(f"Date and Time of Return: {date.today()}\n")
        file1.write(f"Contact Number of the Customer: {number1}\n")

        file1.write("---------------------------------------------------\n")
        for i in range(len(items_in_return)):
            file1.write(f"Costumes returned are: {items_in_return[i]}\n")
            file1.write(f"Brands returned are: {brands_in_return[i]}\n")
            file1.write("---------------------------------------------------\n")

        file1.write(f"Total price of all the rented costumes is ${price}\n")
        file1.write(f"Thank you for using our Application {name}. Here's your bill.")

        file1.close()


    elif user_choice == 3:
        print("\n")
        print("Thank you for using our Application,\n We wish to see you again")
        running = False

    else:
        print("Invalid Input,Please try again")
