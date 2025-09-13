from numbers import Number
from numbers import Integral


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other
    
    def scalar_mul(self, number):
        if isinstance(number, Number):
            return Polynomial( tuple( number* i for i in self.coefficients ) )
        else:
            return NotImplemented
    def __mul__(self,other):
        if isinstance(other, Polynomial):
            poly = Polynomial((0,))
            for i in other.coefficients:
                poly+= self.scalar_mul(i)
            return poly
        elif  isinstance(other, Number):
            return self.scalar_mul(other)
        else:
            return NotImplemented
    def __rmul__(self, other):
        return self* other
    def __sub__(self, other):
        if isinstance(other,Polynomial ):
            common= min (self.degree, other.degree)
            coefs= tuple(a-b for a,b in zip(self.coefficients, other.coefficients))
            coefs+= self.coefficients(common)+ other.coefficients(common)
            return Polynomial(coefs)
        elif isinstance(other, Number):
            coefs=(self.coefficients[0] - other ,) + self.coefficients[1:]
            return Polynomial(coefs)
        else:
            return NotImplemented
    def __rsub__(self,other): 
        return -1 *(self - other)
    def __pow__(self,int):
        if isinstance(int , Integral):
            if int > 0:
              poly= 1
              for _ in len(int):
                poly= poly* self
              return self
            else:
                return NotImplemented
        else:
            return NotImplemented
    def __call__(self, scalar):
        if isinstance(scalar, Number):
            value=0
            for d,c in enumerate(self.coefficients):
                value+= c*scalar**d
            return value
        else:
            return NotImplemented
        
