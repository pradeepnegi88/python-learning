def decorator_greetings(function):
    def another_function(word):
        print("Hello")
        function(word)
        print("Goodbye")

    return another_function


@decorator_greetings
def uppercase(text):
    print(text.upper())


@decorator_greetings
def lowercase(text):
    print(text.lower())


my_function = uppercase
my_function("Python")


def ucase(text):
    print(text.upper())


def lcase(text):
    print(text.lower())


decorator_upper = decorator_greetings(lcase)
decorator_upper("Pradeep")
