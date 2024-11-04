
def menu():
    print("\n1. To go to the drivers' menu\n"
            "2. To go to the cities' menu\n"
            "3. To exit the system\n")
    while True:
        mmenu = int(input("Hello! Please enter the number of the option you want:"))
        if  mmenu == 1:
            DriverMenu().driverInp()
            return

        elif mmenu == 2:
            CityMenu().cityInp()
        elif mmenu == 3:
            print("System exited!")
            exit()
        else:
            print("Invalid input.Try Again")



class DriverMenu:
    def __init__(self):
        self.drivers = [
            {"Name": "Charles Leclerc", "ID": "001", "City": "Saida"},
            {"Name": "Max Verstappen", "ID": "002", "City": "Akkar"},
            {"Name": "Lando Norris", "ID": "003", "City": "Jbeil"},
        ]
        self.cities = ["saida", "akkar", "jbeil", "beirut"]

    def driverInp(self):
        print(
            "\n1. View all the drivers\n"
            "2. Add a driver\n"
            "3. Check similar drivers\n"
            "4. Go back to the main menu\n"
        )
        while True:
            try:
                self.d = int(input("Enter the number of the option you want: "))
                if self.d == 1:
                    self.viewDrivers()
                elif self.d == 2:
                    self.addDriver()
                elif self.d == 3:
                    self.checkSimilar()
                elif self.d == 4:
                    print("Returning to main menu.")
                    return menu()
                else:
                    print("Invalid input. Try Again.")
            except ValueError:
                print("Please enter a valid number.")

    def viewDrivers(self):  
        print("\nAll Drivers:")          
        for driver in self.drivers:
            print(f"{driver['Name']}, {driver['ID']}, {driver['City']}")
        self.addDriver()

    def addDriver(self):
        while True:
            name = input("Enter the name of the driver: ").title().strip()
            city = input("Enter the start city of the driver: ").lower().strip()

            if city not in self.cities:
                add_city = input(f"{city} is not in the database, would you like to add it? (yes/no): ").lower().strip()
                if add_city == "no":
                    print("City not added.")
                elif add_city == "yes":
                    self.cities.append(city)
                    print(f"City '{city}' is added.")
                    newid = "" + str(len(self.drivers) + 1).zfill(3)
                    self.drivers.append({"Name": name, "ID": newid, "City": city})
                    print(f"{name} is added with start city {city} and ID {newid}.")
                    exit()
                else:
                    print("Invalid input. Try Again.")
            else:
                newid = "" + str(len(self.drivers) + 1).zfill(3)
                self.drivers.append({"Name": name, "ID": newid, "City": city})
                print(f"{name} is added with start city {city} and ID {newid}.")
                exit()
            break
        

    def checkSimilar(self):
        print("\nDrivers Grouped by Start City:")
        for city in self.cities:
            drivers_in_city = [driver["Name"] for driver in self.drivers if driver["City"].lower() == city]
            if drivers_in_city:
                print(f"{city.capitalize()}: {', '.join(drivers_in_city)}")
        return menu()



class CityMenu:
    def __init__(self):
        self.cities = {
            "saida" : {"ID": "001", "Name": "Charles Leclerc"},
            "akkar" : {"ID": "002", "Name": "Max Verstappen"},
            "jbeil" : {"ID": "003", "Name" : "Lando Norris"},
        } 
        self.driving_to_city = {city: [info["Name"]] for city, info in self.cities.items()}


    def cityInp(self):
        print(
        "\n1. Show cities\n"
        "2. Search city\n"
        "3. Print neighboring cities\n"
        "4. Print Drivers delivering to city\n"
        "5. Go back to the menu\n")
        while True:
            self.c = int(input("Enter the number of the option you want:"))
            if self.c == 1:
                return self.showCities()
            elif self.c == 2:
                return self.searchCity()
            elif self.c == 3:
                return self.cityNeib()
            elif self.c == 4:
                return self.delevToCity()
            elif self.c == 5:
                print("Returning to main menu.")
                return menu()
            else:
                print("Invalid input.Try Again")


    def showCities(self):
        sorted_cities = sorted(self.cities.keys(), reverse=True)
        print("Cities available are:")
        print("\n".join(city.title() for city in sorted_cities))
        return DriverMenu().driverInp()


    def searchCity(self):
        while True:
            self.search_cities = input("Enter the city or cities you want:").strip().lower()
            matching_cities = []
            for city in self.cities:
                if self.search_cities in city:
                    matching_cities.append(city.title())

            if matching_cities:
                print("Matching cities:\n", ", ".join(matching_cities))
                return DriverMenu().driverInp()
            else:
                print("City or cities entered are unavailable. Try Again.")


    def cityNeib(self):
        self.neibcity = {
            "akkar": {"n": "jbeil"},
            "beirut": {"n": "akkar"},
            "jbeil": {"n": "akkar, beirut"},
        }
        self.empt = "saida"
        while True:
            self.entnei = input("Enter the city to see its neighboring city or cities:").lower().strip()
            if self.entnei in self.neibcity:
                print(f"The neighboring city or cities are {self.neibcity[self.entnei]["n"]}")
                return DriverMenu().driverInp()
            elif self.entnei == self.empt:
                print("No neighboring cities for saida")
                return menu()
            else:
                print("City entered is unavailable.Try Again")


    def delevToCity(self):


        while True:
            self.e = input("Enter a city to see the drivers reaching it:").lower().strip()
            if self.e in self.driving_to_city:
                drivers = ", ".join(self.driving_to_city[self.e])
                print(f"Drivers reaching {self.e.capitalize()} are: {drivers}")
                return menu()
            else:
                print("City entered is unavailabe.Try Again")


menu = menu()
print(menu)

