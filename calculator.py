class Calculator:
    def calculate(self, num1, num2, operator):
        if operator == '+':
            return self.add(num1, num2)
        elif operator == '-':
            return self.subtract(num1, num2)
        elif operator == '*':
            return self.multiply(num1, num2)
        elif operator == '/':
            return self.divide(num1, num2)

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return 'Error: Division by zero'
