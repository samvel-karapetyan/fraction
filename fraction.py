class BaseNumber:
    def to_float(self):
        raise NotImplementedError("Subclasses must implement to_float method")

class Rational(BaseNumber):
    def __init__(self, numerator, denominator):
        raise NotImplementedError
    
    def __str__(self): # print
        raise NotImplementedError
      
    def __add__(self, other): # +
        raise NotImplementedError
    
    def __sub__(self, other): # -
        raise NotImplementedError
    
    def __mul__(self, other): # *
        raise NotImplementedError
    
    def __truediv__(self, other): # /
        raise NotImplementedError
    
    def __eq__(self, other): # ==
        raise NotImplementedError
    
    def to_float(self):
        return self.numerator / self.denominator
