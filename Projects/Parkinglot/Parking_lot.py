class Parking_lot:

    def __init__(self,name,size):
        self.name = name
        self.size = size
        self.slots = [(0,0)] * self.size

    
    def park_car(self, Registration_no, Color ):
        
        Empty_slot = self.get_slot()
        if Empty_slot == -1:
            print("Parking space is full, no slots available!")
            return None
        self.slots[Empty_slot] = (Registration_no, Color)
        print(f"Please park your Car in slot number : {Empty_slot}")

    def Exit(self,Registration_no):
        for slot in range(self.size):
            if self.slots[slot][0] == Registration_no:
                self.slots[slot] = (0,0)
                return slot

    def Cars_by_color(self,):
        pass

    def slot_of_car_by_Reg_no (self,Registration_no):
        
        for slot in range(self.size):
            if self.slots[slot][0] == Registration_no:
                print(f"The Car with Registration number '{Registration_no}' is parked in slot no. {slot}")
                break
        else:
            print("There is no such car parked here")

    def slots_of_cars_by_color (self,Color):
        Same_colored_cars = []
         
        for i in range(self.size):
            if self.slots[i][1] == Color:
                Same_colored_cars.append(i)

        print(f"The cars with color {Color} is present is following slots: {Same_colored_cars}")


    def get_slot(self):
        for slot in range(self.size):
            if self.slots[slot] == (0,0):
                return slot
        else:
            return -1



    def checkout_bill(self):
        pass

    def View_parking_arena(self):

        print("Slot No.\tRegistration No.\tColor")
        
        for i in range(self.size):
            if self.slots[i] != (0,0):
                print(str(i) + "\t\t" +str(self.slots[i][0]) + "\t\t" + str(self.slots[i][1]))
            else:
                continue


if __name__ == "__main__":

    # Parking_lot = Parking_lot("SafePark",6)
    # Parking_lot.park_car("KA51-AA-5396", "Red")
    # Parking_lot.slot_of_car_by_Reg_no("KA51-AA-5396")


    Name = input("What is the name of Parking lot: ")
    Size = int(input("How much car can it hold? "))
    Parking_lot = Parking_lot(Name, Size)  
    print(f"Welcome to {Name}, we can accomodate up to {Size} cars")

    def Menu():
        print("""
                        Please find the MENU below:

                        Press 1 to park your car
                        Press 2 to exit the parking lot
                        Press 3 to know your car slot
                        Press 4 to know all the slots for cars of particular color
                        press 5 to get the nearest empty slot
                        Type Exit or Quit to end the prompt

                        """)
    Menu()
    while True:

        Options = input()

        if Options == "1":
            Reg_no = input("Please Enter the registration number: ")
            Color = input("What is the color of your car? ")
            Parking_lot.park_car(Reg_no,Color)

        elif Options == "2":
            Reg_no = input("Please Enter the registration number: ")
            # Parking_lot.Exit(Reg_no)
            print(f"Your car with Reg_no - {Reg_no} is exited from slot no. {Parking_lot.Exit(Reg_no)}")

        elif Options == "3":
            Reg_no = input("Please Enter the registration number of your car: ")
            Parking_lot.slot_of_car_by_Reg_no(Reg_no)

        
        elif Options == "4":
            Color = input("Please type the color of the car: ").lower()
            Parking_lot.slots_of_cars_by_color(Color)

        elif Options == "5":
            print(f"The nearest empty slot is: {Parking_lot.get_slot()}")

        elif Options == "6":
                Parking_lot.View_parking_arena()

        elif Options.lower() == "quit" or Options.lower() == "exit":
            print(f"Thank you for choosing {Name}, Please visit again!")
            break

        else:
            print("Invalid choice, please select a valid option from the Menu")
            Menu()









