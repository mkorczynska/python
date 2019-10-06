import random


def srodek(max, min):
    s = (max + min) / 2
    return s


def losowanie(min, max):
    los = random.randint(min, max)
    return los


zakres_max = 10
zakres_min = 1

liczba = random.randint(1, 10)
liczba = losowanie(zakres_min, zakres_max)
s = srodek(zakres_max, zakres_min)
odp = ''
i = 1

while odp != "=":
    print("Czy to ta liczba: ", liczba, "?")
    odp = input("Większa/mniejsza/równa? [>/</=]")
    if odp == ">":
        zakres_min = liczba
        s = srodek(zakres_max, zakres_min)
        liczba = losowanie(zakres_min, zakres_max)
        i += 1
    elif odp == "<":
        zakres_max = liczba
        s = srodek(zakres_max, zakres_min)
        liczba = losowanie(zakres_min, zakres_max)
        i += 1
    elif odp == "=":
        print("OK. Znaleziono w ", i, "krokach")
        break
