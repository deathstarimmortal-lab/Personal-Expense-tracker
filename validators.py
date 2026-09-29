def get_amount():
    while True:
        amount = input('Enter amount: ')
        if amount.isdigit() and int(amount) > 0:
            return int(amount)
        print('Enter a positive whole number.')


def get_non_empty(message):
    while True:
        value = input(message).strip()
        if value != '':
            return value
        print('Input cannot be empty.')


def get_expense_id(expenses):
    while True:
        value = input('Enter expense ID: ')
        if value.isdigit():
            expense_id = int(value)
            for expense in expenses:
                if expense[0] == expense_id:
                    return expense_id
        print('Expense ID not found.')
