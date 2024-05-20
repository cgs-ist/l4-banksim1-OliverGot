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
    
    def deposit(self):
        amount = int(input("How much do you want to deposit: "))
        if input("Enter your password: ") == self.__password:
            self.__ballance += amount
            print(f"Your current account ballance is: {self.__ballance}")
        else:
            print("Wrong password.")

currentAccount = bankAccount(input("Enter your name: "), 1000, input("Enter your password: "))


while True:
    print('Press b to get the balance')
    print("Press d to deposit")
    print('Press q to quit')
    userInput = input().lower()
    if userInput == 'b':
        currentAccount.getBallance()
    if userInput == 'd':
        currentAccount.deposit()
    elif userInput == 'q':
        break
