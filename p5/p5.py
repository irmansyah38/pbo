

class Person:
    transport = 2000
    gaji = 10000
    Prshn = 'abc'

    def __init__(self, nama):
        self.nama = nama
    # memanggil atribut class

    def pendapatan(self):
        gaji = Person.gaji
        transport = Person.transport
        print(gaji, transport)


p2 = Person('ksks')


p2.pendapatan()

# print(p1._Person__jabata

# membuat atribut class
