class Person:
    age = 10

    def hallo():
        print('hallo saya')


print(Person.age)


class Car:
    pass


Lamborgini = Car()
Ferarri = Car()
Honda = Car()

Lamborgini.jenis = "sedan"
Lamborgini.warna = 'hitam'

print(Lamborgini)
print(Lamborgini.jenis)

print(Lamborgini.__dict__)
