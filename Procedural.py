accounts = {}

def is_account_exists(account_number):
  return account_number in accounts

def create_account(owner_first_name = None, owner_last_name = None, account_number = 0):
  if is_account_exists(account_number):
    raise ValueError('Account with number {0} is already exists.'.format(account_number))

  accounts[account_number] = {
    'owner': {
      'first_name': owner_first_name,
      'last_name': owner_last_name
    },
    'balance': 0
  }

def clear_accounts():
  accounts.clear()

def get_account_balance(account_number = 0):
  if not is_account_exists(account_number):
    raise ValueError('Account with number {0} not found.'.format(account_number))

  return accounts[account_number]['balance']

def make_deposit(account_number = 0, money_amount = 0):
  if not is_account_exists(account_number):
    raise ValueError('Account with number {0} not found.'.format(account_number))

  accounts[account_number]['balance'] += money_amount

def make_withdraw(account_number = 0, money_amount = 0):
  if not is_account_exists(account_number):
    raise ValueError('Account with number {0} not found.'.format(account_number))

  if accounts[account_number]['balance'] - money_amount < 0:
    raise ValueError('Not enought money.')

  accounts[account_number]['balance'] -= money_amount

def make_transfer(payer_account_number = 0, beneficiary_account_number = 0, money_amount = 0):
  if not is_account_exists(payer_account_number):
    raise ValueError('Payer account with number {0} not found.'.format(payer_account_number))

  if not is_account_exists(beneficiary_account_number):
    raise ValueError('Beneficiary account with number {0} not found.'.format(beneficiary_account_number))

  make_withdraw(payer_account_number, money_amount)
  make_deposit(beneficiary_account_number, money_amount)

