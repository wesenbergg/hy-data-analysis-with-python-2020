#!/usr/bin/env python3

# def convert(obj):
#     return obj.osoittaja / obj.nimittaja

class Rational(object):
    def __init__(self, o, n):
        self.osoittaja = o
        self.nimittaja = n
    
    def __str__(self):
        return f'{self.osoittaja}/{self.nimittaja}'

    def __add__(self, number):
        nimittaja = int( self.nimittaja * number.nimittaja ) 
        osoittaja = int( self.osoittaja * number.nimittaja + number.osoittaja * self.nimittaja )
        return Rational(osoittaja, nimittaja)

    def __sub__(self, number):
        nimittaja = int( self.nimittaja * number.nimittaja ) 
        osoittaja = int( self.osoittaja * number.nimittaja - number.osoittaja * self.nimittaja )
        return Rational(osoittaja, nimittaja)

    def __mul__(self, number):
        return Rational( (self.osoittaja * number.osoittaja), (self.nimittaja * number.nimittaja) )

    def __truediv__(self, number):
        return Rational( (self.osoittaja * number.nimittaja), (self.nimittaja * number.osoittaja))

    def __eq__(self, number):
        return self.osoittaja * number.nimittaja == self.nimittaja * number.osoittaja

    def __gt__(self, number):
        return self.osoittaja * number.nimittaja > self.nimittaja * number.osoittaja

    def __lt__(self, number):
        return self.osoittaja * number.nimittaja < self.nimittaja * number.osoittaja

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
