from expenses import view_expenses, update_expense, delete_expense
from reports import show_report, category_report
from budget import show_budget
from validators import get_amount, get_non_empty, get_expense_id


def menu():
    print('\nPERSONAL EXPENSE TRACKER')
    print('1. Add expense')
    print('2. View expenses')
    print('3. Update expense')
    print('4. Delete expense')
    print('5. Expense report')
    print('6. Set budget')
    print('7. View budget')
    print('8. Exit')


def main():
    expenses = []
    budgets = {}
    next_id = 1

    while True:
        menu()
        choice = input('Enter choice: ').strip()

        if choice == '1':
            date = get_non_empty('Enter date (DD-MM-YYYY): ')
            category = get_non_empty('Enter category: ')
            amount = get_amount()
            note = input('Enter note: ').strip()
            expenses.append((next_id, date, category, amount, note))
            print('Expense added with ID:', next_id)
            next_id = next_id + 1

        elif choice == '2':
            view_expenses(expenses)

        elif choice == '3':
            if len(expenses) == 0:
                print('No expenses to update.')
                continue
            expense_id = get_expense_id(expenses)
            date = get_non_empty('Enter new date (DD-MM-YYYY): ')
            category = get_non_empty('Enter new category: ')
            amount = get_amount()
            note = input('Enter new note: ').strip()
            update_expense(expenses, expense_id, date, category, amount, note)
            print('Expense updated.')

        elif choice == '4':
            if len(expenses) == 0:
                print('No expenses to delete.')
                continue
            expense_id = get_expense_id(expenses)
            delete_expense(expenses, expense_id)
            print('Expense deleted.')

        elif choice == '5':
            show_report(expenses)

        elif choice == '6':
            category = get_non_empty('Enter category: ')
            amount = get_amount()
            budgets[category] = amount
            print('Budget saved.')

        elif choice == '7':
            category_totals = category_report(expenses)
            show_budget(budgets, category_totals)

        elif choice == '8':
            print('Thank you for using Personal Expense Tracker.')
            break

        else:
            print('Invalid choice.')


if __name__ == '__main__':
    main()
