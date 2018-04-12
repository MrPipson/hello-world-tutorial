# An assertion is a sanity-check that you can turn on or turn off when you have
# finished testing the program.
# An expression is tested, and if the result comes up false, an exception is raised.
# Assertions are carried out through use of the assert statement.

print(1)
assert 2 + 2 == 4
print(2)
# assert 1 + 1 == 3
print(3)

# Programmers often place assertions at the start of a function to check for
# valid input, and after a function call to check for valid output.

# The assert can take a second argument that is passed to the AssertionError
# raised if the assertion fails.

temp = -10
# assert (temp >= 0), "Colder than zero!"

# AssertionError exceptions can be caught and handled like any other exception
# using the try-except statement, but if not handled, this type of exception will
# terminate the program.

# create a function that takes one argument and assert that the argument is positive

def my_func(x):
    y = int(x)
    assert y > 0, "Error, not positive"
    print(y)
my_func(input())
