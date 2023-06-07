# Write a Python class called BankAccount with methods for depositing, withdrawing,
# and checking the account balance.

class BankAccount:
    def __init__(self,checking_ab):
        self.checking = checking_ab

    def depositing(self,new_deposit):
        self.checking += new_deposit

    def withdrawing(self,new_withdraw):
        if  new_withdraw <= self.checking:
            self.checking -= new_withdraw

        else:
            print('insufficient funds, withdrawal not possible')

    def checking_1(self):
        return self.checking

account = BankAccount(100)

account.depositing(500)

account.withdrawing(700)

balance = account.checking_1()
print ("Actual account balance", balance)



