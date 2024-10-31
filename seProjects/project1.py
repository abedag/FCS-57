class DrvMenu:
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

    def menu(self):
        pass

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

    def driverInp(self):
        print(
        "1. View all the drivers\n"
        "2. Add a driver\n"
        "3. Check similar drivers\n"
        "4. Go back to the main menu\n")
        while True:
            self.d = int(input("Enter the number of yhe option you want:"))
            if self.d == 1:
                return self.viewDrivers()
            elif self.d == 2:
                return self.addDriver()
            elif self.d == 3:
                return self.checkSimilar()
            elif self.d == 4:
                return self.menu()
            else:
                print("Invalid input.Try Again")

d = DrvMenu()
d.driverInp()
