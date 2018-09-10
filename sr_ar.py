class Calc():
    def __init__(self, nam, asd):
        self.number = nam
        value = self.calc_value()
        self.print_number(value)



    def calc_value(self):
        return self.number * 10 + 2

    def print_number(self, value_to_print):
        print('-----')
        print('Number is ', value_to_print)
        print('-----')


s = Calc(2, 7)

