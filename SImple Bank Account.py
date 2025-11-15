class Bankaccount
   def__init__(*self, owner, balance):
       self.owner = owner
       self.__balance = balance # private attribute
   def deposit(self, amount):
       self.__balance += amount

   def show_balance(self):
       print(f"{self.owner}'s balance is ${self._balance}")

acc = BankAccount("Nitin",500000)
acc.deposit(10000)
acc.show_balance()