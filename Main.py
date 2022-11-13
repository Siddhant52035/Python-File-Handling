
def welcome():
    print("\n")
    print("******************Welcome to the Perfect Fit Costume Rentals*********************")
    print("\n")
    print("(1) || Press 1 to rent a Costume")
    print("(2) || Press 2 to return a Costume")
    print("(3) || Press 3 to exit")

    user = int(input("Select a desirable option:"))

    return user


def display_costume():
    file = open("costume.txt","r")
    count = 1

    print("----------------------------------------------------------------------------------")
    print("Id\t","Name\t\t\t","Brand\t\t\t","Price\t\t", "Quantity")
    print("----------------------------------------------------------------------------------")
    for line in file:
        print(count,"\t",line.replace(",","\t\t"))
        count+= 1

    file.close()

def dic_costume():
    file = open('costume.txt',"r")
    count = 0
    dicCostume = {}
    for line in file:
        count += 1
        a = line.replace("\n","")
        x = a.split(",")
        dicCostume[count] = x
    file.close()
    return dicCostume


def valid_costumeId(dic):
    v_costumeId = 0
    while True:
        try:
            print("\n")
            v_costumeId = int(input("Enter the Id of the costume you want to rent:"))
            while v_costumeId <= 0 or v_costumeId > len(dic_costume()):
                if v_costumeId <= 0 or v_costumeId > len(dic_costume()):
                    print("Invalid Costume Id,Please try again!!!!")
                    display_costume()
                    v_costumeId = int(input("Enter the Id of the costume you want to rent:"))

            while dic[v_costumeId][3] == "0":
                print("Sorry, The requested costume is unavailable!!!!!\nPlease Pick another costume")
                display_costume()
                v_costumeId = int(input("Enter the Id of the costume you want to rent:"))

            print("Costume having ID ", v_costumeId, " is available.")

            break

        except Exception as e:
            print(e)
            continue

    return v_costumeId

def valid_costumeId_return():
    v_costumeId = 0
    while True:
        try:
            v_costumeId = int(input("Enter the Id of the costume you want to return:"))

            while v_costumeId <=0 or v_costumeId > len(dic_costume()):
                print("Invalid Costume Id.Please try again!!!!")
                display_costume()
                v_costumeId = int(input("Enter the Id of the costume you want to return:"))
            break
        except Exception as e:
            print("The exception is ",e)
            continue
    return v_costumeId

def valid_quantity(available_quantity):

    v_quantity = 0
    while True:
        try:
            print("\n")
            v_quantity = int(input("Enter the quantity of the costume you want to rent:"))
            while v_quantity > available_quantity or v_quantity <= 0:
                if v_quantity > available_quantity:
                    print("The provided quantity is greater than what we have in stock, please select a smaller quantity")
                    v_quantity = int(input("Enter the quantity of the costume you want to rent:"))

                elif v_quantity <= 0:
                    print("Quantity can't be negative or Zero")
                    v_quantity = int(input("Enter the quantity of the costume you want to rent:"))

            print(v_quantity," costumes have been rented Successfully.")
            break
        except Exception as e:
            print("The exception is ",e)
            continue

    return v_quantity

def edit_file_info(c_dictionary):

    file = open("costume.txt","w")
    for i in c_dictionary.values():
        new_line=  str(i[0] + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3]))

        file.write(new_line)
        file.write("\n")

    file.close()


def total_price(quantity_rented,costume_id,dictionary):

    price = float(dictionary[costume_id][2].replace("$",""))
    total_price = quantity_rented * price
    return total_price


def rent_again():
    my_dictionary = dic_costume()

    print("Let's rent a costume")
    display_costume()
    print("------------------------------------------------------------")
    costume_id = valid_costumeId(my_dictionary)



    quantity_rented = valid_quantity(int(my_dictionary[costume_id][3]))


    my_dictionary[costume_id][3] = int(my_dictionary[costume_id][3]) - quantity_rented
    
    edit_file_info(my_dictionary)

    return list, costume_id, quantity_rented


def return_again():
    display_costume()
    print("------------------------------------------------------------")
    c_id = valid_costumeId_return()
    a = 0
    dictionary2 = dic_costume()
    while True:
        try:
            v_quantity = int(input("Enter the quantity of the costume you want to return:"))


            dictionary2[c_id][3] = int(dictionary2[c_id][3]) + v_quantity
            
            edit_file_info(dictionary2)
            print("\n")
            days_kept = int(input("How many days did you keep the costume for ?"))
            print("\n")

            if days_kept <= 5:
                a = 0

            else:

                a = (days_kept - 5) * v_quantity * 5
            break

        except Exception as e:
            print("The exception is ",e)
            continue

    return c_id,a
