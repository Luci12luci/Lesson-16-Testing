class Kalkulacka:
    def sucet(self, a, b):
        return a + b

    def sucin(self, a, b):
        return a * b

    def delenie(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Chyba: Delenie nulou!"

    def dlzka_predpony(self, a, b):
        return (a**2 + b**2)**0.5

    def kvadraticka_rovnica(self, a, b, c):
        D = b**2 - 4*a*c
        if D > 0:
            x1 = (-b + D**0.5) / (2*a)
            x2 = (-b - D**0.5) / (2*a)
            return x1, x2
        elif D == 0:
            x = -b / (2*a)
            return x
        else:
            return

kalkulacka = Kalkulacka()
# print("Súčet: ", kalkulacka.sucet(5, 3))
# print("Súčin: ", kalkulacka.sucin(5, 3))
# print("Podiel: ", kalkulacka.delenie(9, 3))
# print("Dĺžka predpony: ", kalkulacka.dlzka_predpony(3, 4))
# print("Korene kvadratickej rovnice: ", kalkulacka.kvadraticka_rovnica(1, 4, 3))

