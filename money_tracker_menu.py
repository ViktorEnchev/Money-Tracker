from money_tracker import MoneyTracker
import datetime
import os


class MTMenu:
    mt = MoneyTracker()
    __data_dict = mt.make_a_dict()

    def show_all_data(self):
        self.mt.list_user_data(self.__data_dict)

    @staticmethod
    def check_date(year, month, day):
        correct_date = None
        try:
            new_date = datetime.datetime(int(year), int(month), int(day))
            correct_date = True
        except ValueError:
            correct_date = False

        return correct_date

    def show_data_for_specific_date(self, day, month, year):
        if not self.check_date(year, month, day):
            print("Wrong date!")
            input('Continue')
            raise ValueError

        else:
            if int(day) < 10:
                day = '0{0}'.format(day)
            if int(month) < 10:
                month = '0{0}'.format(month)
            real_date = '=== {}-{}-{} ===\n'.format(day, month, year)
            self.mt.show_user_data_per_date(real_date, self.__data_dict)

    def show_expenses_ordered_by_cat(self):
        self.mt.list_user_expenses_ordered_by_categories(self.__data_dict)

    def checking_for_correctnes(self, amount, date):
        os.system('clear')

        try:
            float(amount)
        except ValueError:
            print("Amount isn't a number!")
            input('Continue')

        if float(amount) < 0:
            print("Amount is negative!")
            input('Continue')
            raise ValueError

        day, month, year = date.split('-')
        if not self.check_date(year, month, day):
            print("Wrong Date!")
            input('Continue')
            raise ValueError

        return True

    def add_inc(self):
        while True:
            os.system('clear')

            amount = input("New income amount: ")
            category = input("New income type: ")
            print("Date should look like this: xx-xx-xxxx")
            date = input("New income date: ")

            try:
                self.checking_for_correctnes(amount, date)
                self.mt.add_income(category, amount, date, self.__data_dict)
            except ValueError:
                continue
            else:
                break

    def add_exp(self):
        while True:
            os.system('clear')

            amount = input("New expense amount: ")
            category = input("New expense type: ")
            print("Date should look like this: xx-xx-xxxx")
            date = input("New expense date: ")

            try:
                self.checking_for_correctnes(amount, date)
                self.mt.add_expense(category, amount, date, self.__data_dict)
            except ValueError:
                continue
            else:
                break
