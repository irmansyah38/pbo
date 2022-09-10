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

    def __init__(self, z = 0):
        self.z = z
       
    def total(self,x1,y1,x2,y2):
        x      = (x2 - x1)**2
        y      = (y2 - y1)**2
        self.z = math.sqrt(x + y)
        print(self.z)
        


titik1 = titik(6, 6)
titik2 = titik(10, 9)

q = jarak()

q.total(titik1.x,titik1.y,titik2.x,titik2.y)
