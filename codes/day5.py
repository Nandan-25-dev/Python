#Encapsulation is the process of binding the data and methods together,
#such that it aint accessible by outside components
class Bankacc:
    def __init__(self,owner,balance,pin):
        self.owner=owner
        self._balance=balance
        self.__pin=pin
    def deposit(self,amount):
        print (amount,"rs successfully deposited!")
        self._balance+=amount
    def withdrawal(self,amount,pin):
        if(self.__pin==pin):
            if(amount<=self._balance):
                print(amount,"rs withdrawn successfully!")
                self._balance-=amount
            else:
                print("Insufficient balance!")
        else:
            print("Incorrect pin!")
    def viewbal(self):
        return self._balance
acc=Bankacc("Nandan",12000,2510)
acc.deposit(3000)
acc.withdrawal(1234,2510)
print("Account balance is: ",acc.viewbal())
