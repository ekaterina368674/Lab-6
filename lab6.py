class Weapon:
    def __init__(self, patrons, skor, daln):
        self.patrons = patrons
        self.skor = skor
        self.daln = daln

    def __str__(self):
        return f'количество патронов {self.patrons}\n' \
               f'скорострельность {self.skor}\n' \
               f'дальность {self.skor}\n' \
               f'магазин опустеет за {self.pysto()}\n' \
               f'соотношение скорострельности к дальности {self.sootn()}'

    def __add__(self, other):
        return Weapon(self.patrons + other.patrons, self.skor, self.daln)

    def pysto(self):
        return self.patrons / self.skor

    def sootn(self):
        return self.skor / self.daln


class ShtyrmVint(Weapon):
    def __init__(self, color):
        super().__init__(20, 200, 750)
        self.color = color

    def recolor(self):
        self.color = self.color[::-1]

    def __str__(self):
        return super().__str__() + f'\nцвет {self.color}'


class SniperVint(Weapon):
    def __init__(self, ves):
        super().__init__(4, 1, 3000)
        self.weight = ves

    def off_load(self):
        self.patrons = 0
        self.weight /= 2

    def __str__(self):
        return super().__str__() + f'\nвес {self.weight}'


o = ShtyrmVint("black")
print(type(o), o, sep='\n')
y = SniperVint(13)
print(type(y), y, sep='\n')
i = o + y
print('результат сложения:')
print(type(i), i, sep='\n')
print(f'меняем цвет для {type(o)}')
o.recolor()
print(o)
print("выкидываем патроны")
y.off_load()
print(y)
