from decimal import Decimal

class Fees(object):
    def __init__(self):
        self._fee = None

    def get_fee(self):
        return self._fee

    def set_fee(self, value):
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value

    fee = property(get_fee, set_fee)  # making the arguments into properties

f = Fees()
f.set_fee("1")
print(f.fee)

f.fee = "2"
print(f.fee)

# Even though we are getting and setting using fee on the object, Python can distinguish between the 2 based on if there is an '=', which implies setting.
# Otherwise, it'll know you want to just get_fee.