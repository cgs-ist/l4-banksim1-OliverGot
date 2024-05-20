class bankAccount:
    def __init__(self, name, ballance, password):
        self.name = name
        self.__ballance = ballance
        self.__password = password
    
    def __checkPassword(self):
        return input("Enter password: ") == self.__password

    def getBallance(self):
        if self.__checkPassword():
            print(f"Your current account ballance is: {self.__ballance}")
        else:
            print("Wrong password.")
    
    def deposit(self):
        amount = int(input("How much do you want to deposit: "))
        if self.__checkPassword():
            self.__ballance += amount
            print(f"Your current account ballance is: {self.__ballance}")
        else:
            print("Wrong password.")
    
    def withdraw(self):
        amount = int(input("How much do you want to withdraw: "))
        if self.__checkPassword():
            self.__ballance -= amount
            print(f"Your current account ballance is: {self.__ballance}")
        else:
            print("Wrong password.")

currentAccount = bankAccount(input("Enter your name: "), 1000, input("Enter your password: "))

while True:
    print('Press b to get the balance')
    print("Press d to deposit")
    print("Press w to withdraw")
    print('Press q to quit')
    userInput = input().lower()
    if userInput == 'b':
        currentAccount.getBallance()
    if userInput == 'd':
        currentAccount.deposit()
    if userInput == 'w':
        currentAccount.withdraw()
    elif userInput == 'q':
        break
