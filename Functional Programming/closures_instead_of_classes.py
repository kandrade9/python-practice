# Formatter class
class Format():
  def __init__(self, precision):
    self.p = precision

  def format(self, x):
    return '{:.{prec}f}'.format(x, prec=self.p)

format3 = Format(3)
print(format3.format(1.2345678))
print(Format(5).format(1.2345678))
print("##################################")
# Using a closure instead
def formatn(precision):
  def format(x):
    return '{:.{prec}}'.format(x, prec=precision)
  return format

format3 = formatn(3)
print(type(format3))
var = format3(1.2345678)
print(var)
print(type(var))
print(formatn(5)(1.2345678))

# Both are valid, and there is nothing wrong with using a class in this case, but a closure offers quite an elegant solution.
# Generally, you can use a closure instead of a class if:
# The class would only have one method.
# The parameters are set in the __init__ method and never changed.
# If these conditions are not met, you will often be better off using a class.


