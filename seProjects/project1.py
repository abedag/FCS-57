class DrvMenu:
    def __init__(self):
        self.drivers = {
            "Bassam Jaber": {"ID": "001", "City": "Akkar"},
             "Kosay Azzam" : {"ID": "002","City": "Beirut"},
             "Elias Skafi" : {"ID": "003", "City": "Jbeil"},
             "Ahmad Salem" : {"ID": "004", "City": "Saida"},
             "Hassan Hijazi" : {"ID": "005", "City": "Beirut"},
             "Abed Dahoud" : {"ID": "006", "City": "Saida"},
             "Ahmad Issa" : {"ID": "007", "City": "Jbeil"},
        } 

    def viewDrivers(self):
        self.id = self.drivers[""]
        
        print("""

            """)


    def driverInp(self):
        print(
        "1. To view all the drivers"
        "2. To add a driver"
        "3. Check similar drivers"
        "4. To go back to the main menu")
        while True:
            self.d = int(input("Enter the number of yhe option you want:"))
            if self.d == 1:
                return viewDrivers()
            elif self.d == 2:
                return addDriver()
            elif self.d == 3:
                return checkSimilar()
            elif self.d == 4:
                return backMenu()
            else:
                print("Invalid input.Try again")







