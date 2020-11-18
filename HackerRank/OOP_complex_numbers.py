import math

import math

class Complex(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __add__(self, n):
        a = self.a + n.a
        b = self.b + n.b
        return Complex(a, b)

    def __sub__(self, n):
        a = self.a - n.a
        b = self.b - n.b
        return Complex(a, b)
        
    def __mul__(self, n):
        #(ac-bd) + i(bc+ad)
        a = self.a * n.a - self.b * n.b
        b = self.b * n.a + self.a * n.b
        return Complex(a, b)

    def __truediv__(self, n):
        #(ac + bd)/(c2 + d2) + (bc - ad)/(c2 + d2)i
        denominator = n.a**2 + n.b**2
        a = (self.a * n.a + self.b * n.b) / denominator
        b = (self.b * n.a - self.a * n.b) / denominator
        return Complex(a, b)
    
    def mod(self):
        #mod(a+bi) = sqrt(a**2 + b**2)
        a = math.sqrt(self.a**2 + self.b**2)
        b = 0.00
        return Complex(a, b)
        
    def __str__(self):
        if self.b == 0:
            result = "%.2f+0.00i" % (self.a)
        elif self.a == 0:
            if self.b >= 0:
                result = "0.00+%.2fi" % (self.b)
            else:
                result = "0.00-%.2fi" % (abs(self.b))
        elif self.b > 0:
            result = "%.2f+%.2fi" % (self.a, self.b)
        else:
            result = "%.2f-%.2fi" % (self.a, abs(self.b))
        return result


# c = map(float, input().split())
# d = map(float, input().split())
x = Complex(2, 1)
y = Complex(5, 6)
print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')