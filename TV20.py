import math
'''
Obliczanie pola powierzchni i obwodu koła o zadanym promieniu
'''
# ustal promień koła i PI
r = float(input("Podaj promien kola: "))
#r = 3

PI = math.pi

# oblicz pole i obwód
obw = 2 * PI * r
p = PI * (r * r)

# wyświetl rezultaty
print("Obwod kola o promienu %.2f wynosi %.2f" %(r, obw))
print("Pole powierzchni kola o promieniu %.2f wynosi = %.2f" %(r, p))

# Pole koła o promieniu ... wynosi ...
# Obwód koła o promieniu ... wynosi ...