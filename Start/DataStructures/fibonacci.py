class Fibonacci:

    def __init__(self):
        pass

    @staticmethod
    def fib(n):
        assert n >= 0 and isinstance(n, int), f"fibonacci number must be a positive integer!"
        if n in (0, 1):
            return n
        return Fibonacci.fib(n - 1) + Fibonacci.fib(n - 2)


if __name__ == "__main__":
    print(Fibonacci.fib(1))
