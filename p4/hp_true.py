# from tkinter.font import ROMAN


# class Smartphone:

#     def __init__(self, mrek, type, cpu, ram, rom, layar):
#         self.mrek = mrek
#         self.type = type
#         self.cpu = cpu
#         self.ram = ram
#         self.rom = rom
#         self.layar = layar


# smartphone1 = Smartphone('samsung', 'a70', '2.5', 12, 128, 6)
# smartphone2 = Smartphone('samsung', 'a80', '2.5', 16, 128, 7)
# smartphone3 = Smartphone('samsung', 'a10', '2.5', 2, 32, 5)


# smartphone = [smartphone1, smartphone2, smartphone3]

# for hp in smartphone:
#     print("mrek : {} type : {} cpu : {} ram : {} rom : {} layar : {}".format(
#         hp.mrek, hp.type, hp.cpu, hp.ram, hp.rom, hp.layar))


import math


class titik:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class jarak:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def total(self):
        z = self.x*2 + self.y*2
        z = math.sqrt(z)
        print(z)


titik1 = titik(12, 7)
titik2 = titik(10, 11)
