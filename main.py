print("--- BR Converter ---")

money = int(input("Enter how much money you want to convert: "))

print("\nChoose the currencies you want to convert:\n1. USD\n2. EUR\n3. UAH")
user = int(input("From this: "))
user1 = int(input("On this one: "))



if user == 1 and user1 == 1:
    print("[-]You cannot convert the same currency!")
elif user == 2 and user1 == 2:
    print("[-]You cannot convert the same currency!")
elif user == 3 and user1 == 3:
    print("[-]You cannot convert the same currency!")


elif (user == 1 and user1 == 2) or (user == 2 and user1 ==1):
    conUE = money * 0.93
    conEU = money * 1.08
    print("USD to EUR: ", conUE, "\nEUR to USD: ", conEU)
elif (user == 2 and user1 == 3) or (user == 3 and user1 ==2):
    conEU = money * 42.31
    conUE = money * 0.024
    print("EUR to UAH: ", conEU, "\nUAH to EUR: ", conUE)
elif (user == 1 and user1 == 3) or (user == 3 and user1 == 1):
    conUU1 = money * 39.17
    conUU2 = money * 0.026
    print("USD to UAH: ", conUU1, "\nUAH to USD:", conUU2)
else:
    print("You have entered an invalid value!")