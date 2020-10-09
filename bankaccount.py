class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return "This account belongs to %s and balance is $%.2f" % (self.name, self.balance)

  def show_balance(self):
    print "The balance is $%.2f" % (self.balance)

  def deposit(self, amount):
    if amount <= 0:
      print "Error! Amount cannot be less than 0"
      return
    else:
      print "Deposit amount is: $%.2f" % (amount)
      self.balance += amount 
      self.show_balance()
  
  def withdraw(self, amount):
    if amount > self.balance:
      print "Withdrawal rejected! Not enough balance"
      return
    else:
      print "Amount withdrawn: $%.2f" % (amount)
      self.balance -= amount
      self.show_balance()

my_account = BankAccount("Anil")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account

