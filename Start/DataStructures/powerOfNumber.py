class PowerOfNumber:

    def __int__(self):
        pass

    def find_power(self, base, exp):
        assert exp >= 0 and isinstance(exp, int), f"The exponential \"{exp}\" must be a positive integer!"
        if exp == 0:
            return 1
        if exp == 1:
            return base
        return base * self.find_power(base, exp - 1)


if __name__ == "__main__":
    power = PowerOfNumber()
    print(power.find_power(2.5, 3))
