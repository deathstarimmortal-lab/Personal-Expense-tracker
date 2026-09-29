def show_budget(budgets, category_totals):
    if len(budgets) == 0:
        print('No budgets set.')
        return

    print('\nBudget Report')
    print('-' * 35)
    for category in budgets:
        budget = budgets[category]
        spent = category_totals.get(category, 0)
        difference = budget - spent

        print(category, '| Budget:', budget, '| Spent:', spent)
        if difference >= 0:
            print('Remaining:', difference)
        else:
            print('Over budget:', -difference)
