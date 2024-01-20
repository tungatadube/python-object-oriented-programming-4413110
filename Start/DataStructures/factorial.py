class Factorial:

    # define a method to recursively calculate n!
    # Given
    # n! = n * (n-1)!
    # 1! = 1
    # 0! = 1

    def __init__(self):
        pass

    @staticmethod
    def factorial(n):

        if n < 0 or not isinstance(n, int):
            raise ValueError(f"Number {n} must be non negative and an integer")
        if n in [0, 1]:
            return 1
        factorial = n * Factorial.factorial(n - 1)
        return factorial


if __name__ == "__main__":
    f = Factorial()
    print(f.factorial(10.2))
