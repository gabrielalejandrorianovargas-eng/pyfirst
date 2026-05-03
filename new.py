
print("\n ===CONVERSOR===")
while True:
    print("Escoge una opcion: ")
    print("opcion_1 = kilometers_to_miles")
    print("opcion_2 = miles_to_kilometers")
    print("opcion_3 = celsius_to_fahrenheit")
    print("opcion_4 = fahrenheit_to_celsius")
    print("opcion_5 = leave")

    opcion = input("escoge una opcion") 
    if opcion =="1":
        print("\n ===kilometers value===")
        kilometers = float(input("insert kilometers value: "))
        miles = float(1.61)
        result = kilometers / miles
        print("The value of kilometers to miles is: ", result)
    elif opcion == "2":
        print("\n ===miles value===")
        miles = float(input("insert the value of miles: "))
        kilometers = float(1.61)
        result = miles * kilometers
        print("The result of miles convert to kilometers is: ", result)
    elif opcion == "3":
        print("\n===celsius to fahrenheit")
        celsius = float(input("insert celsisu value: "))
        fahrenheit = (32)
        result = (celsius * 9/5)+ fahrenheit
        print("the value of celsisu convert to fahrenheit is: ", result)
    elif opcion == "4":
        print("\n ===fahrenheit to celsisu===")
        fahrenheit = float(input("insert fahrenheit value"))
        celsius = float(32)
        result = (fahrenheit - celsius) / 5 / 9
        print(" the result of fahrenheit to celsius is: ", result)
    elif opcion == "5":
        break
    else:
        print("invalid option, try again")



