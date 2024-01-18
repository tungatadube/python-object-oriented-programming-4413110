# Python Object Oriented Programming by Joe Marini course example
# Programming challenge: define a class to represent a stock symbol

# Challenge: create a class to represent stock information.
# Your class should have properties for:
# Ticker (string)
# Price (float)
# Company (string)
# And a method get_description() which returns a string in the form
# of "Ticker: Company -- $Price"

class Stock:
    def __init__(self, ticker, price, company):
        self.company = company
        self.price = price
        self.ticker = ticker

    def get_description(self):
        return f"{self.get_ticker()}: {self.get_company()} -- ${self.get_price()}"

    def get_ticker(self):
        return self.ticker

    def get_company(self):
        return self.company

    def get_price(self):
        return self.price
# ~~~~~~~~~ TEST CODE ~~~~~~~~~
msft = Stock("MSFT", 342.0, "Microsoft Corp")
goog = Stock("GOOG", 135.0, "Google Inc")
meta = Stock("META", 275.0, "Meta Platforms Inc")
amzn = Stock("AMZN", 135.0, "Amazon Inc")

if __name__ == "__main__":
    print(msft.get_description())
    print(goog.get_description())
    print(meta.get_description())
    print(amzn.get_description())
