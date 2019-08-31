import tensorflow as tf

class CalculatorModel:
    def __init__(self):
        pass
    def input_number(self):
        self.a = int(input('number 1'))
        self.b = int(input('number 2'))

    def hook(self,menu):
        self.input_number()
        if menu == 1:result = self.plus()
        elif menu == 2:result=self.minus()
        elif menu == 3:result = self.multi()
        elif menu == 4: result = self.divide()

    def plus(self):
        pass
    def minus(self):
        pass
    def multi(self):
        pass
    def divide(self):
        pass
