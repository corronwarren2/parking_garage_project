class ParkingGarage:


    def __init__(self):
        self.tickets = [1, 2, 3, 4, 5]
        self.parking_spaces = [1, 2, 3, 4, 5]
       # self.current_ticket = currentTicket

    def takeTicket(self):
        self.tickets.remove('ticket') # removes one ticket
        self.parking_spaces.remove('spaces') # removes one space

    def payForParking(self): # defines payForParking
        while self.current_ticket['paid'] == False:# if there is a current ticket showing paid that information is FALSE
            payment = input('Pay for your ticket, please: ')
            if payment.lower() == 'yes':
                print('Thank you for parking, you have 15 minutes to exit parking garage.')
                self.current_ticket['paid'] = True
                continue
            if payment.lower() == 'no':
                print('You need to pay to exit')
                self.current_ticket['paid'] = True
                continue
            else:
                print('Incorrect input. Please enter yes or no')

    def leaveGarage(self):
        if self.payment != '':
            print('Thank you, have a nice day')
        else:
            self.payForParking()
        self.tickets.append('ticket')
        self.parking_spaces('spaces')

  # def runGarage():
      # ticket = [1, 2, 3, 4, 5]
      # parkingSpaces = [1, 2, 3, 4, 5]

        

myParkingGarage = ParkingGarage()
#myParkingGarage.payForParking()

#runGarage()
while True: 
    response = input('What would you like to do, Park / Pay / Leave / Quit?:')
   
    if response.lower() == 'park':# if this
        print('Please take a ticket')
        pass
    elif response.lower() == 'pay':# else if this
        print('What is your ticket number?')
        pass
    elif response.lower() == 'leave':# else if this
        print('What is your ticket number?:')
           #if myParkingGarage.tickets == True
        pass
    elif response.lower() == 'quit':# else if this
        break

    elif response.lower() == "dump":
        print(myParkingGarage.tickets)
        print(myParkingGarage.parking_spaces)
    else: #fall through case
        print('Please enter a valid statement!')