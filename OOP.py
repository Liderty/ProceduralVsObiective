import datetime

start_time = datetime.datetime.now()

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
      raise NotEnoughtMoneyException('Account with number {0} has not enought money to withdraw {1}.'.format(self.number, amount))

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


owner_fixtures = [
  Owner('Foo', 'Bar'),
  Owner('Foo', 'Baz')
]

account_fixtures = [
  BankAccount(owner_fixtures[0], 4578220122),
  BankAccount(owner_fixtures[1], 2347885320),
  BankAccount(owner_fixtures[1], 1174559614)
]

foo_bar_baz_bank = Bank()

foo_bar_baz_bank.add_account(account_fixtures[0])
foo_bar_baz_bank.add_account(account_fixtures[1])
foo_bar_baz_bank.add_account(account_fixtures[2])

for _ in range(0, 2_000_000):
  foo_bar_baz_bank.make_deposit(foo_bar_baz_bank.get_account(4578220122), 2)
  foo_bar_baz_bank.make_deposit(foo_bar_baz_bank.get_account(2347885320), 2)

for _ in range(0, 1_000_000):
  foo_bar_baz_bank.make_withdraw(foo_bar_baz_bank.get_account(4578220122), 1)
  foo_bar_baz_bank.make_withdraw(foo_bar_baz_bank.get_account(2347885320), 1)

for _ in range(0, 500_000):
  foo_bar_baz_bank.make_transfer(
    foo_bar_baz_bank.get_account(4578220122),
    foo_bar_baz_bank.get_account(2347885320),
    3
  )

for _ in range(0, 500_000):
  foo_bar_baz_bank.make_transfer(
    foo_bar_baz_bank.get_account(2347885320),
    foo_bar_baz_bank.get_account(4578220122),
    2
  )

print(foo_bar_baz_bank.get_account(4578220122).get_balance())
print(foo_bar_baz_bank.get_account(2347885320).get_balance())
print(foo_bar_baz_bank.get_account(1174559614).get_balance())

end_time = datetime.datetime.now()

print('Time elapsed: {0}'.format(end_time - start_time))
