
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
            break
        else:
            print("Invalid input.Try Again")



class DriverMenu:
    def __init__(self):
        self.drivers = {
            "abed dahoud" : {"ID": "001", "City": "Saida"},
            "ahmad salem" : {"ID": "002", "City": "Saida"},
            "bassam jaber": {"ID": "003", "City": "Akkar"},
            "elias skafi" : {"ID": "004", "City": "Jbeil"},
            "hassan hijazi" : {"ID": "005", "City": "Beirut"},
            "kosay azzam" : {"ID": "006","City": "Beirut"},
            "mohammad issa" : {"ID": "007", "City": "Jbeil"},
        } 


    def driverInp(self):
        print(
        "\n1. View all the drivers\n"
        "2. Add a driver\n"
        "3. Check similar drivers\n"
        "4. Go back to the main menu\n")
        while True:
            self.d = int(input("Enter the number of the option you want:"))
            if self.d == 1:
                return self.viewDrivers()
            elif self.d == 2:
                return self.addDriver()
            elif self.d == 3:
                return self.checkSimilar()
            elif self.d == 4:
                return menu()
            else:
                print("Invalid input.Try Again")


    def viewDrivers(self):            
        print("Name: Abed Dahoud, ID: 001, City: Saida\n"
            "Name: Ahmad Salem, ID: 002, City: Saida\n"
            "Name: Bassam Jaber, ID: 003, City: Akkar\n"
            "Name: Elias Skafi, ID: 004, City: Jbeil\n"
            "Name: Hassan Hijazi, ID: 005, City: Beirut\n"
            "Name: Kosay Azzam, ID: 006, City: Beirut\n"
            "Name: Mohammad Issa, ID: 007, City: Jbeil\n")
        
        self.addDriver()


    def addDriver(self):
        while True:
            self.name = input("Enter the name of the driver you want:").strip().lower()

            if self.name not in self.drivers:
                print(f"{self.name} not found.Try Again")
                continue
            
            self.city = input("Enter the start city of the chosen driver:").strip().lower()

            if self.drivers[self.name]["City"].lower() != self.city:
                print(f"{self.city} doesn't match the chosen driver. Try Again.")
                continue
            
            self.id = self.drivers[self.name]["ID"]
            print(f"{self.name.title()} with {self.city.title()} start city and ID {self.id} is saved.")
            break
        

    def checkSimilar(self):
        self.same_city = input("Enter the city to see the drivers starting from it:").strip().lower()
        matching_drivers = [name.title() for name, details in self.drivers.items() if details["City"].lower() == self.same_city]

        if matching_drivers:
            print(f"Drivers starting from {self.same_city.title()}: {', '.join(matching_drivers)}")
        else:
            print("City not found. Try Again.")
        return self.addDriver()

class CityMenu:
    def __init__(self):
        self.cities = {
            "jbeil" : {"ID": "007", "Name": "Mohammad Issa"},
            "jbeil" : {"ID": "004", "Name": "Elias Skafi"},
            "saida" : {"ID": "002", "Name": "Ahmad Salem"},
            "saida" : {"ID": "001", "Name": "Abed Dahoud"},
            "beirut" : {"ID": "006","Name": "Kosay Azzam"},
            "beirut" : {"ID": "005", "Name": "Hassan Hijazi"},
            "akkar": {"ID": "003", "Name": "Bassam Jaber"},
        } 


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
                print("City or cities are unavailable. Try Again.")


    def cityNeib(self):
        pass


    def delevToCity():
        pass




menu = menu()
print(menu)