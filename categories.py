class Category:

    def __init__(self, amount, name):
        if isinstance(amount, str):
            try:
                float(amount)
            except ValueError as e:
                raise e("Amount not a number")
        if float(amount) < 0:
            raise ValueError('Amount is negative!')

        self.amount = amount
        self.name = name

    def __int__(self):
        return int(self.amount)

    def __str__(self):
        return "{0}, {1}".format(self.amount, self.name)

    def __repr__(self):
        return "{0}, {1}".format(self.amount, self.name)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False


class Income(Category):

    def __init__(self, amount, name, typee):
        super().__init__(amount, name)
        if typee != 'New Income\n':
            raise TypeError("It's not an Income!")
        else:
            self.typee = typee

    def __str__(self):
        return "{0}, {1}, {2}".format(self.amount, self.name, self.typee)

    def __repr__(self):
        return "{0}, {1}, {2}".format(self.amount, self.name, self.typee)


class Expense(Category):

    def __init__(self, amount, name, typee):
        super().__init__(amount, name)
        if typee != 'New Expense\n':
            raise TypeError("It's not a Expense!")
        else:
            self.typee = typee

    def __str__(self):
        return "{0}, {1}, {2}".format(self.amount, self.name, self.typee)

    def __repr__(self):
        return "{0}, {1}, {2}".format(self.amount, self.name, self.typee)
