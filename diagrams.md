Design Diagrams

The following diagrams describe the actual structure and workflow of the
Personal Expense Tracker project.

System Architecture

+----------------+
|      User      |
+-------+--------+
        |
        v
+----------------+
|    main.py     |
| Program Flow   |
+-------+--------+
        |
        +------------------+
        |                  |
        v                  v
+---------------+   +---------------+
| validators.py |   |  expenses.py  |
| Input Checks  |   | View/Update/  |
+---------------+   | Delete        |
                    +---------------+
        |
        +------------------+
        |                  |
        v                  v
+---------------+   +---------------+
|  reports.py   |   |   budget.py   |
| Expense Report|   | Budget Check  |
+---------------+   +---------------+

Workflow

START
  |
  v
Show Main Menu
  |
  v
Take User Choice
  |
  +---- 1. Add Expense ---------> Validate Input
  |
  +---- 2. View Expenses -------> Display Expenses
  |
  +---- 3. Update Expense ------> Find ID -> Validate -> Update
  |
  +---- 4. Delete Expense ------> Find ID -> Delete
  |
  +---- 5. Expense Report ------> Count -> Total -> Average -> Category Report
  |
  +---- 6. Set Budget ----------> Store Category Budget
  |
  +---- 7. View Budget ---------> Compare Spending with Budget
  |
  +---- 8. Exit ----------------> END
  |
  v
Show Output
  |
  v
Return to Main Menu

Use Case Diagram

                 +--------------------------------------+
                 |     Personal Expense Tracker         |
                 |                                      |
User ----------> | Add Expense                          |
User ----------> | View Expenses                        |
User ----------> | Update Expense                       |
User ----------> | Delete Expense                       |
User ----------> | Generate Expense Report              |
User ----------> | Set Budget                           |
User ----------> | View Budget                          |
                 +--------------------------------------+

Sequence Diagram: Add Expense

User            main.py          validators.py
 |                |                    |
 |-- Add Expense->|                    |
 |                |-- Get Amount ----->|
 |                |<-- Valid Amount ---|
 |                |-- Get Category -->|
 |                |<-- Valid Input ---|
 |                |-- Get Date ------>|
 |                |<-- Valid Input ---|
 |                |-- Get Note ------>|
 |                |<-- Valid Input ---|
 |                |                    |
 |                |-- Store Expense --|
 |<-- Confirmation|                    |

Sequence Diagram: View Expense Report

User            main.py          reports.py
 |                |                  |
 |-- Report ----->|                  |
 |                |-- show_report -->|
 |                |                  |
 |                |<-- Total --------|
 |                |<-- Average ------|
 |                |<-- Category Data-|
 |<-- Report -----|                  |

Component / Module Diagram

                    +-------------+
                    |   main.py   |
                    | Program Flow|
                    +------+------+
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
 +----------------+ +---------------+ +---------------+
 | validators.py  | |  expenses.py  | |  reports.py   |
 | Input Validation| | View/Update/ | | Total/Average |
 |                | | Delete       | | Category      |
 +----------------+ +---------------+ +---------------+
                                           
                           +---------------+
                           |   budget.py   |
                           | Budget Check  |
                           +---------------+

Design of Data Structures

For the project, only simple Python data structures have been used which are
essential for the expense tracking problem.

Expenses List

Each expense is saved in the form of a tuple in a list.

expenses = [
    (1, "12-09-2026", "Entertainment", 6900, "worth it"),
    (2, "21-09-2026", "Grocery", 4200, "more potato next time")
]

List: saves all the expenses.

Tuple: saves the fixed fields of an expense.

Budgets Dictionary

budgets = {
    "Entertainment": 7000,
    "Grocery": 4100
}

This dictionary saves a category and its budget amount.

Category Totals Dictionary

The expense report maintains a dictionary to save the total amount spent on each category.

category_totals = {
    "Food": 250,
    "Travel": 50
}

Categories Set

Set data structure can be used to save the unique category names in the project.

categories = {
    "Food",
    "Travel",
    "Entertainment"
}

Algorithms Implemented

Only those algorithms that are applicable for the Personal Expense
Tracker have been implemented.

Counting

The number of expenses can be counted by counting the number of items in
the expense list.

Summation

The total expense is calculated by adding the amount of all expenses.

Average

The average expense is calculated using:

Average = Total Expense / Number of Expenses

Searching

Linear searching algorithm is used to look for an expense on the basis
of ID before making any changes to it.

Category Wise Calculation

The expense list is traversed and amounts are added corresponding to the
same category.

Time Complexity

For n number of expense records:

View Expenses           -> O(n)
Total Expense           -> O(n)
Category Wise Report    -> O(n)
Find Expense by ID      -> O(n)
Updating Expense        -> O(n)
Deleting Expense        -> O(n)

The project has kept the implementation simple by use of lists and
linear searching algorithm.