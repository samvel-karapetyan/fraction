from math import gcd
from abc import ABC, abstractmethod


class BaseNumber(ABC):
    @abstractmethod
    def __add__(self, other):
        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    @abstractmethod
    def to_float(self):
        raise NotImplementedError

class Fraction(BaseNumber): # Fraction
    def __init__(self, numerator, denominator):
        # numerator / denominator
        if denominator == 0:
            raise ValueError("Denominator can not be zero!")

        gcd_value = gcd(numerator, denominator)

        self.numerator = numerator // gcd_value
        self.denominator = denominator // gcd_value

    def __str__(self): # print
        return f"{self.numerator} / {self.denominator}"
      
    def __add__(self, other): # +
        # a / b, c / d

        # (a * d + b * c) / b * d
        
        return Fraction(self.numerator * other.denominator \
                        + self.denominator * other.numerator, 
                        self.denominator * other.denominator)
    
    def __sub__(self, other): # -
        return Fraction(self.numerator * other.denominator \
                        - self.denominator * other.numerator, 
                        self.denominator * other.denominator)
    
    def __mul__(self, other): # *
        # (a / b) * (c / d) = (a * b) / (c * d)
        return Fraction(self.numerator * other.numerator, 
                        self.denominator * other.denominator)
    
    def __truediv__(self, other): # / # __div__
        # (a / b) : (c / d) = (a * d) / (b * c)
        return self * other._inverse()
    
    def _inverse(self):
        return Fraction(self.denominator, self.numerator)
    
    def __eq__(self, other): # ==
        # a / b == c / d -> a * d == b * c
        return self.numerator * other.denominator == self.denominator * other.numerator

    def to_float(self):
        return self.numerator / self.denominator

x = Fraction(30000, 30000) # 2 / 3
# y = Fraction(100, 100)
# z = Fraction(2400, 2400)

# 2/3 : 3/4 = 2/3 * 4/3

# print(x)
# print((x + y + z).to_float())

# //, % 