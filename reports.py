def total_expenses(expenses):
    total = 0
    for expense in expenses:
        total = total + expense[3]
    return total


def category_report(expenses):
    totals = {}
    categories = set()

    for expense in expenses:
        category = expense[2]
        amount = expense[3]
        categories.add(category)

        if category in totals:
            totals[category] = totals[category] + amount
        else:
            totals[category] = amount

    print('\nCategory Report')
    print('-' * 30)
    for category in categories:
        print(category, ':', totals[category])

    return totals


def show_report(expenses):
    count = len(expenses)
    total = total_expenses(expenses)

    print('\nExpense Report')
    print('-' * 30)
    print('Number of expenses:', count)
    print('Total spent:', total)

    if count > 0:
        print('Average expense:', total // count)
    else:
        print('Average expense: 0')

    category_report(expenses)
