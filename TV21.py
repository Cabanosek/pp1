# Zamiana stopni C na K i F

try:
    x = int(input("Temperatura w stopniach Celsjusza: "))
    print(f"{x}°C to {float(x)+273.15}°K i {float(x)*1.8 + 32}°F")
except ValueError:
    print("Podaj liczbę.")