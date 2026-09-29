def view_expenses(expenses):
    if len(expenses) == 0:
        print('No expenses recorded.')
        return

    print('\nID  Date        Category       Amount  Note')
    print('-' * 55)
    for expense in expenses:
        print(expense[0], expense[1], expense[2], expense[3], expense[4], sep='  ')


def update_expense(expenses, expense_id, date, category, amount, note):
    for i in range(len(expenses)):
        if expenses[i][0] == expense_id:
            expenses[i] = (expense_id, date, category, amount, note)
            return True
    return False


def delete_expense(expenses, expense_id):
    for i in range(len(expenses)):
        if expenses[i][0] == expense_id:
            expenses.pop(i)
            return True
    return False
