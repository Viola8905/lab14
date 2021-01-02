from math import sqrt
import random

class TPTriangle:
    def __init__(self, *arg):
        self.sides = arg

    def p(self):
        return sum(self.sides)

    def s(self):
        p = self.p() / 2

        return sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))


class Rivnostoroniy(TPTriangle):
    def __init__(self, a):
        super().__init__(a)

    def p(self):
        return super().p() * 3

    def s(self):
        return ((sqrt(3)) * (self.sides[0] ** 2)) / 4


class Pryamokutni(TPTriangle):
    def __init__(self, katet_1, katet_2):
        super().__init__(katet_1, katet_2)

    def s(self):
        return (self.sides[0] * self.sides[1]) / 2

    def p(self):
        return self.sides[0] + self.sides[1] + sqrt((self.sides[0]) ** 2 + (self.sides[1]) ** 2)


class Rivnobedrenij(TPTriangle):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.h = sqrt(int(self.sides[1]) ** 2 - ((int(self.sides[0]) / 2) ** 2))

    def s(self):
        return (self.h * self.sides[0]) / 2

    def p(self):
        return self.sides[0] + (self.sides[1] * 2)


n=int(input("n="))
figures = []
for i in range(n):
    num=random.randint(1,3)
    if num ==1:
        a=random.randint(1,100)
        b=random.randint(a,100)
        figures.append(Rivnobedrenij(a,b))
    elif num==2:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        figures.append(Pryamokutni(a, b))
    else:
        a=random.randint(1,100)
        figures.append(Rivnostoroniy(a))
for f in figures:
    print(type(f),f.s())

sum_sOfRivnostor = 0
sum_sOfPryam=0
sum_pOfRivnobed=0
for f in figures:
    if isinstance(f,Rivnostoroniy):
        sum_sOfRivnostor += f.s()
    elif isinstance(f,Rivnobedrenij):
        sum_pOfRivnobed+=f.p()
    else:
        sum_sOfPryam+=f.s()

print(sum_sOfRivnostor)
print(sum_sOfPryam)
print(sum_pOfRivnobed)