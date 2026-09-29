from expenses import update_expense, delete_expense
from reports import total_expenses, category_report


def test_project():
    expenses = [
        (1, '01-09-2026', 'Food', 100, 'Lunch'),
        (2, '02-09-2026', 'Travel', 50, 'Bus'),
        (3, '03-09-2026', 'Food', 150, 'Dinner')
    ]

    if total_expenses(expenses) == 300:
        print('PASS: total expense')
    else:
        print('FAIL: total expense')

    totals = category_report(expenses)
    if totals['Food'] == 250 and totals['Travel'] == 50:
        print('PASS: category report')
    else:
        print('FAIL: category report')

    update_expense(expenses, 2, '02-09-2026', 'Travel', 70, 'Bus')
    if expenses[1][3] == 70:
        print('PASS: update expense')
    else:
        print('FAIL: update expense')

    delete_expense(expenses, 1)
    if len(expenses) == 2:
        print('PASS: delete expense')
    else:
        print('FAIL: delete expense')


test_project()
