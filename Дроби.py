class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def GCD(self, a, b):
        return self.GCD(b, a % b) if b else a

    def __add__(self, other):
        znumenatel = self.denominator * other.denominator // self.GCD(self.denominator, other.denominator)
        chislitel = znumenatel // self.denominator * self.numerator + znumenatel // other.denominator * other.numerator
        self.numerator = chislitel
        self.denominator = znumenatel
        return Fraction(numerator=chislitel, denominator=znumenatel)

    def __sub__(self, other):
        znumenatel = self.denominator * other.denominator // self.GCD(self.denominator, other.denominator)
        chislitel = znumenatel // self.denominator * self.numerator - znumenatel // other.denominator * other.numerator
        self.numerator = chislitel
        self.denominator = znumenatel
        return Fraction(numerator=self.numerator, denominator=self.denominator)

    def __mul__(self, other):
        chislitel = self.numerator * other.numerator
        znumenatel = self.denominator * other.denominator
        z = self.GCD(chislitel, znumenatel)
        chislitel //= z
        znumenatel //= z
        self.numerator = chislitel
        self.denominator = znumenatel
        return Fraction(numerator=self.numerator, denominator=self.denominator)

    def __floordiv__(self, other):
        x = other.numerator
        other.numerator = other.denominator
        other.denominator = x
        chislitel = self.numerator * other.numerator
        znumenatel = self.denominator * other.denominator
        z = self.GCD(chislitel, znumenatel)
        chislitel //= z
        znumenatel //= z
        self.numerator = chislitel
        self.denominator = znumenatel
        return Fraction(numerator=self.numerator, denominator=self.denominator)

    def str(self):
        return f"{self.numerator}/{self.denominator}"


num1 = 10 / 10
num2 = 5 / 10

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 // num2)
