class bankAccount:
    def __init__(self, name, ballance, password):
        self.name = name
        self.__ballance = ballance
        self.__password = password
    
    def getBallance(self):
        if input("Enter your password: ") == self.__password:
            print(f"Your current account ballance is: {self.__ballance}")
        else:
            print("Wrong password.")

newAccount = bankAccount("Oliver", 1000, "thisismypassword")

while True:
    print('Press b to get the balance')
    print('Press q to quit')

    if input() == 'b':
        newAccount.getBallance()
    elif input == 'q':
        break
