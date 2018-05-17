from parse_money_tracker_data import Parser
from categories import Income, Expense


class Aggregate:
    _parse = Parser('money_tracker.txt')
    __list = _parse.get_data()

    def print_data(self):
        for x in self.__list:
            print(x)

    @staticmethod
    def is_key_in_dict(key, dict):
        if key in dict:
            return True
        return False

    @staticmethod
    def split_it(info):
        return info.split(', ')

    def make_a_dict(self):
        self._information = {}
        for x in self.__list:
            if x[0] == '=':
                date = x
                if not self.is_key_in_dict(x, self._information):
                    self._information[x] = {'Income': [], 'Expense': []}
            else:
                amount, category, typee = self.split_it(x)
                if typee == 'New Income\n':
                    inc = Income(amount, category, typee)
                    self._information[date]['Income'].append(inc)
                elif typee == 'New Expense\n':
                    exp = Expense(amount, category, typee)
                    self._information[date]['Expense'].append(exp)

        return self._information

    def get_info(self):
        info = self.make_a_dict()
        for x in info:
            print(x)




