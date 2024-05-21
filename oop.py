class bankAccount:
    def __init__(self, name, ballance, password):
        self.name = name
        self.__ballance = ballance
        self.__password = password
    
    def checkPassword(self):
        return input("Enter password: ") == self.__password

    def getBallance(self):
        print(f"Your current account ballance is: {self.__ballance}")
    
    def addBallance(self, ballance):
        self.__ballance += ballance
    
    def deposit(self):
        amount = int(input("How much do you want to deposit: "))
        self.__ballance += amount
        print(f"Your current account ballance is: {self.__ballance}")
    
    def withdraw(self):
        amount = int(input("How much do you want to withdraw: "))
        self.__ballance -= amount
        print(f"Your current account ballance is: {self.__ballance}")
    
    def transfer(self, bank):
        amount = int(input("How much do you want to transfer: "))
        name = input("Who do you want to transfer to: ")
        accountIndex = findAccount(bank, name)
        if accountIndex != -1:
            bank[accountIndex].addBallance(amount)
            print(f"Transfered ${amount} to {name}.")
        else:
            print("That account does not exist.")

bank = []
currentAccount = None

def findAccount(bank, name):
    for i, account in enumerate(bank):
        if account.name == name:
            return i
    return -1

while True:
    if not currentAccount:
        print("Press c to create a new account")
        print("Press l to login to account")
        print("Press q to quit")
        userInput = input().lower()
        if userInput == 'c':
            nameProposition = input("Enter your username: ")
            if findAccount(bank, nameProposition) != -1:
                print("Sorry, that username is taken")
            else:
                bank.append(bankAccount(nameProposition, 0, input("Enter your password: ")))
                currentAccount = bank[-1]
        elif userInput == 'l':
            accountIndex = findAccount(bank, input("Enter your username: "))
            if accountIndex == - 1: print("That account does not exist.")
            else: 
                if bank[accountIndex].checkPassword():
                    currentAccount = bank[accountIndex]
                else:
                    print("Wrong password")
        elif userInput == 'q':
            break
        else:
            print("That command is not recognised.")
    else:
        print('Press b to get the balance')
        print("Press d to deposit")
        print("Press w to withdraw")
        print("Press l to logout")
        print("Press t to transfer")
        print('Press q to quit')
        userInput = input().lower()
        if userInput == 'b': currentAccount.getBallance()
        elif userInput == 'd': currentAccount.deposit()
        elif userInput == 'w': currentAccount.withdraw()
        elif userInput == 'l': currentAccount = None
        elif userInput == 't': currentAccount.transfer(bank)
        elif userInput == 'q': break
        else: print("Sorry, that command isn't recognised.")
