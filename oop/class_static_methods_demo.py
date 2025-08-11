class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: Does not access class or instance attributes."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: Has access to the class via 'cls'."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b