while True:
    print('''
        ******** Distance Converter *********
        1. Centimeter to meters
        2. Meter to Centimeters
        3. Inches to Meters
        4. Meter to inches
        5. Inches to foots
        6. Foots to Inches
        7. Milimeters to meters
        8. Meters to milimeters
        9. Kilometers to meters
       10. Meters to Kilometers
       11. Mile to Meters
       12. Meter to Miles 
       13. Yards to Meters
       14. Meter to Yards ''')
    choice = int(input("Enter your choice: "))
    try: 
        if choice == 1:
            unit = int(input("Enter distance in Centimeters: "))
            m = 100/unit
            print("Distance in Meters is: ",m, "m") 
            command = input("Do you want to exit? Yes/No: ")
            if command == "Yes" or command == "yes" or command == "y" or command == "YES":
                break
        elif choice == 2:
            unit = int(input("Enter distance in Meters: "))
            cm = 100*unit
            print("Distance in Centimeters is: ",cm, "cm")
            command = input("Do you want to exit? Yes/No: ")
            if command == "Yes" or command == "yes" or command == "y" or command == "YES":
                break
        elif choice == 3:
            unit = int(input("Enter distance in Inches: "))
            m = 0.0254*unit
            print("Distance in Meters is: ",m, "m")
            command = input("Do you want to exit? Yes/No: ")
            if command == "Yes" or command == "yes" or command == "y" or command == "YES":
                break
        elif choice == 4:
            unit = int(input("Enter distance in Meters: "))
            inch = 39.3701*unit
            print("Distance in Inches is: ",inch, "inches")
            command = input("Do you want to exit? Yes/No: ")
            if command == "Yes" or command == "yes" or command == "y" or command == "YES":
                break
        elif choice == 5:
            unit = int(input("Enter distance in Inches: "))
            feets = 0.0833333*unit
            print("Distance in Feets is: ",feets, "feets")
            command = input("Do you want to exit? Yes/No: ")
            if command == "Yes" or command == "yes" or command == "y" or command == "YES":
                break
        elif choice == 6:
            unit = int(input("Enter distance in Feets: "))
            inch = 12*unit
            print("Distance in Inches is: ",inch, "inches")
            command = input("Do you want to exit? Yes/No: ")
            if command == "Yes" or command == "yes" or command == "y" or command == "YES":
                break
        elif choice == 7:
            unit = int(input("Enter distance in Milimeters: "))
            m = 0.001*unit
            print("Distance in Meters is: ",m, "m")
            command = input("Do you want to exit? Yes/No: ")
            if command == "Yes" or command == "yes" or command == "y" or command == "YES":
                break
        elif choice == 8:
            unit = int(input("Enter distance in Meters: "))
            mm = 1000*unit
            print("Distance in Milimeters is: ",mm, "mm")
            command = input("Do you want to exit? Yes/No: ")
            if command == "Yes" or command == "yes" or command == "y" or command == "YES":
                break
        elif choice == 9:
            unit = int(input("Enter distance in Kilometers: "))
            m = 1000*unit
            print("Distance in Meters is: ",m, "m")
            command = input("Do you want to exit? Yes/No: ")
            if command == "Yes" or command == "yes" or command == "y" or command == "YES":
                break
        elif choice == 10:
            unit = int(input("Enter distance in Meters: "))
            km = 0.001*unit
            print("Distance in Kilometers is: ",km, "km")
            command = input("Do you want to exit? Yes/No: ")
            if command == "Yes" or command == "yes" or command == "y" or command == "YES":
                break
        elif choice == 11:
            unit = int(input("Enter distance in Miles: "))
            m = 1609.34*unit
            print("Distance in Meters is: ",m, "m")
            command = input("Do you want to exit? Yes/No: ")
            if command == "Yes" or command == "yes" or command == "y" or command == "YES":
                break
        elif choice == 12:
            unit = int(input("Enter distance in Meters: "))
            mile = 0.000621371*unit
            print("Distance in Miles is: ",mile, "miles")
            command = input("Do you want to exit? Yes/No: ")
            if command == "Yes" or command == "yes" or command == "y" or command == "YES":
                break
        elif choice == 13:
            unit = int(input("Enter distance in Yards: "))
            m = 0.9144*unit
            print("Distance in Meters is: ",m, "m")
            command = input("Do you want to exit? Yes/No: ")
            if command == "Yes" or command == "yes" or command == "y" or command == "YES":
                break
        elif choice == 14:
            unit = int(input("Enter distance in Meters: "))
            yard = 1.09361*unit
            print("Distance in Yards is: ",yard, "yards")
            command = input("Do you want to exit? Yes/No: ")
            if command == "Yes" or command == "yes" or command == "y" or command == "YES":
                break
    except:
        print("Invalid Input! Try Again")