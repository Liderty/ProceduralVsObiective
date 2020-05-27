class Owner:
  __first_name = None
  __last_name = None

  @property
  def full_name(self):
    return '{0} {1}'.format(self.__first_name, self.__last_name)

  def __init__(self, first_name = None, last_name = None):
    self.__first_name = first_name
    self.__last_name = last_name


class BankAccount:
  __owner = None
  __number = 0
  __balance = 0

  def __init__(self, owner = None, number = 0):
    self.__owner = owner
    self.__number = number

  def deposit(self, amount = 0):
    if amount <= 0:
      raise ValueError('Money amount should be greater than 0.')

    self.__balance += amount

  def withdraw(self, amount = 0):
    if self.__balance - amount < 0:
      raise NotEnoughtMoneyException('Account with number {0} has not enought money to withdraw {1}.'.format(self.__number, amount))

    self.__balance -= amount

  def get_owner(self):
    return self.__owner

  def get_number(self):
    return self.__number

  def get_balance(self):
    return self.__balance


class Bank:
  __accounts = []

  def add_account(self, account):
    self.__accounts.append(account)

  def get_account(self, number):
    account = next(filter(lambda account: account.get_number() == number, self.__accounts), None)

    if not account:
      raise AccountNotFoundException('Account with number {0} not found.'.format(number))
      
    return account

  def make_deposit(self, account = None, amount = 0):
    account.deposit(amount)

  def make_withdraw(self, account = None, amount = 0):
    account.withdraw(amount)

  def make_transfer(self, payer_account = None, beneficiary_account = None, amount = 0):
    payer_account.withdraw(amount)
    beneficiary_account.deposit(amount)


class AccountNotFoundException(Exception):
  pass


class NotEnoughtMoneyException(Exception):
  pass
