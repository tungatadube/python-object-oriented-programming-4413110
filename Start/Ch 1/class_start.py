# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:

    # TODO: Properties defined at the class level are shared by all instances

    # TODO: double-underscore properties are hidden from other classes

    # TODO: create a class method

    # TODO: create a static method

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    # Initialises the class,
    # it's called the initialiser function as object will have been created when method is called
    def __init__(self, title, author, pages, price):
        self.price = price
        self.title = title
        self.author = author
        self.pages = pages
        self.__secret = "This is a secret"
# TODO: access the class attribute

# TODO create instance methods
    def get_price(self):
        if hasattr(self, "_discount"):
            self.price = self.price * (1 - self._discount)
        return self.price

    def set_discount(self, factor):
       # "the underscore is used to signal that variable
       # is 'private', ie must only be used insede of class
       #dunder on the other hand allows python intepreter to mungle tha name
        self._discount = factor


# TODO: Create some book instances
if __name__ == "__main__":
    book1 = Book("Pursuit of happiness", "Will Smith", 210, 23)
    book2 = Book("Ukuthunjwa KukaSukuzukuduma", "Geshom M.P Khiyaza", 250, 10)
    print(book1.title.title() + "by " + book2.author)
    print(f"The non discounted price is ${book1.get_price()}")
    book1.set_discount(1)
    print(f"The discounted price is ${book1.get_price()}")
    print(f"The secret is {book1._Book__secret}")


# TODO: Use the static method to access a singleton object
