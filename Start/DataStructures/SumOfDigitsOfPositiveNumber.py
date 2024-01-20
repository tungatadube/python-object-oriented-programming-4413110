class SumOfDigitsOfPositiveNumber:

    def __int__(self):
        pass

    @staticmethod
    def sum_digits(n):
        assert n >= 0 and isinstance(n, int), f"Number {n} must be a positive integer!"
        if n == 0:
            return 0
        return int(n % 10) + SumOfDigitsOfPositiveNumber.sum_digits(int(n / 10))


if __name__ == "__main__":
    print(SumOfDigitsOfPositiveNumber.sum_digits(3450.8))
