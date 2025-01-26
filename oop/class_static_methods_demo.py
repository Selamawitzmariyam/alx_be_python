class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        :param a: First number.
        :param b: Second number.
        :return: Sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        Prints the class attribute `calculation_type` before performing multiplication.
        :param a: First number.
        :param b: Second number.
        :return: Product of a and b.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


if __name__ == "__main__":
    # Using static method
    sum_result = Calculator.add(10, 5)
    print(f"Sum: {sum_result}")

    # Using class method
    product_result = Calculator.multiply(10, 5)
    print(f"Product: {product_result}")