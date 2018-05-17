from aggregated_money_tracker import Aggregate
from categories import Income, Expense


class MoneyTracker:

    def make_a_dict(self):
        aggra = Aggregate()
        self._data_dict = aggra.make_a_dict()
        return self._data_dict

    def list_user_data(self, all_user_data):
        for key in all_user_data:
            print(key)
            for x in all_user_data[key]['Income']:
                print(x)
            for x in all_user_data[key]['Expense']:
                print(x)

    def show_user_savings(self, all_user_data):
        for key in all_user_data:
            print(key)
            for x in all_user_data[key]['Income']:
                print(x)

    def show_user_expenses(self, all_user_data):
        for key in all_user_data:
            print(key)
            for x in all_user_data[key]['Expense']:
                print(x)

    @staticmethod
    def sort_item(obj):
        return obj.name

    def list_user_expenses_ordered_by_categories(self, all_user_data):
        expenses = []
        for key in all_user_data:
            for x in all_user_data[key]['Expense']:
                expenses.append(x)
        expenses.sort(key=lambda obj: self.sort_item(obj))
        for x in expenses:
            print(x)

    def show_user_data_per_date(self, date, all_user_data):
        if date in all_user_data:
            print(date)
            for x in all_user_data[date]['Income']:
                print(x)
            for x in all_user_data[date]['Expense']:
                print(x)
        else:
            print("The date you are looking for isn't in the data")

    def list_income_categories(self, all_user_data):
        set_with_categories = set()
        for key in all_user_data:
            for x in all_user_data[key]['Income']:
                set_with_categories.add(x.name)

        print(set_with_categories)

    def list_expense_categories(self, all_user_data):
        set_with_categories = set()
        for key in all_user_data:
            for x in all_user_data[key]['Expense']:
                set_with_categories.add(x.name)

        print(set_with_categories)

    def add_income(self, income_category, money, date, all_user_data):
        inc = Income(money, income_category, "New Income\n")
        real_date = '=== {} ===\n'.format(date)

        if real_date in all_user_data:
            all_user_data[real_date]['Income'].append(inc)
        else:
            all_user_data[real_date] = {'Income': [inc], 'Expense': []}

        with open('money_tracker.txt', 'w') as file:
            for key in all_user_data:
                file.write(key)
                for x in all_user_data[key]['Income']:
                    file.write(str(x))
                for x in all_user_data[key]['Expense']:
                    file.write(str(x))

    def add_expense(self, expense_category, money, date, all_user_data):
        exp = Expense(money, expense_category, "New Expense\n")
        real_date = '=== {} ===\n'.format(date)

        if real_date in all_user_data:
            all_user_data[real_date]['Expense'].append(exp)
        else:
            all_user_data[real_date] = {'Income': [], 'Expense': [exp]}

        with open('money_tracker.txt', 'w') as file:
            for key in all_user_data:
                file.write(key)
                for x in all_user_data[key]['Income']:
                    file.write(str(x))
                for x in all_user_data[key]['Expense']:
                    file.write(str(x))


