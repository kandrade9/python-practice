# In functional programming, we sometimes write functions that create other functions.
# A simple and elegant way to do this is to use a closure.
# Closures provide a way to create functions dynamically, a little like lambdas but far more powerful.

# A closure normally requires three things:
# An outer function that contains an inner function.
# The outer function has parameters and/or local variables.
# The outer function returns the inner function as a function object.

# In fact, strictly speaking, any function that returns an inner function is a closure, even if it doesn’t have any parameters (e.g., our make_print function near the start of this lesson).
# However, a closure is not very useful if there is no way to vary the behavior of the closure.

# The make_print function defines an inner function, print_hello. But it doesn’t call print_hello. It simply returns it as a function object.
# When we call make_print in the main code, we assign the function pointer to the variable, fn.
# This means that fn is now effectively an alias of the inner function, print_hello.
# So, when we execute fn, it does what you would expect. It prints “hello”.
def make_print():
    def print_hello():
        print('hello')

    return print_hello

fn = make_print()  # print_hello
fn()

# Closure
def make_printx(x):
    def printx():
        print(x)

    return printx

fn1 = make_printx(7)
fn2 = make_printx(100)
fn1()
fn2()
# Our outer function, make_printx takes a parameter, and the inner function, printx, uses that parameter.
# That is fine, of course, because an inner function can access the local variables and parameters of the enclosing function. Now we call make_printx, passing in a value of 7.
# This creates a function object for the function printx, but here is the important part – that function object is associated with the value, x = 7.
# The combination of the function object together with the value of x is called a closure.
# In the code above, fn1 is a closure of printx with the x value of 7, and fn2 is a closure of printx with the x value of 100.
# Whenever we call fn1, it will print 7, and whenever we call fn2, it will print 100.

print("############################")
def make_printb(start, end):
  def printb(s):
    print(start + s + end)
  return printb

sq = make_printb('[', ']')
dbl_ang = make_printb('<<', '>>')
sq('hello')
dbl_ang('world')
cb = make_printb('{', '}')
cb("yerr")
# Here, make_printb accepts parameters for the start and the end brackets.
# However, in this case, the inner function, printb, accepts a parameter that represents the actual string to be printed inside the brackets.
# This means that the type of brackets is fixed when you create the closure, but you can set the content when you actually call the closure function.
# So, when we create the closure, sq, we set the brackets to be square brackets.
# Every time sq is called, it will use square brackets, but the content between the brackets can be whatever you like.
# Similarly, dbl_ang will always use double angle brackets.



