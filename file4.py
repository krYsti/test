# def policzSlowa(slowo):
#     slowa = slowo.split(" ")
#     return len(slowa)
#
# print(policzSlowa("Ala ma kota"))

# def policzSamogloski(slowo):
#     samogloski = ['a', 'o', 'i', 'e', 'u', 'y', 'ę', 'ą', 'ó']
#     ile = 0
#     slowo = slowo.lower()
#     litery = list(slowo)
#     for i in litery:
#         if i in samogloski:
#             ile += 1
#     return ile
#
# print(policzSamogloski("Ala ma kota"))

# def policzXO(slowo):
#     znakiX = ["x", "X"]
#     znakiO = ["o", "O"]
#     ileX = 0
#     ileO = 0
#     for litera in slowo:
#         if litera in znakiX:
#             ileX += 1
#         elif litera in znakiO:
#             ileO += 1
#         else:
#             print("Illegal character")
#             return False
#
#     if ileX == ileO:
#         print("Tyle samo")
#         return True
#     else:
#         print("Nie tyle samo")
#         return False
#
# print(policzXO("oxx"))

# def cenzuraCyfr(text):
#     text2 = ""
#     for litera in text:
#         if litera.isdigit():
#             text2 += "#"
#         else:
#             text2 += litera
#     return text2
#
# print(cenzuraCyfr("Ala1ma2kota345"))

file = open('py1.2')
slownik = {}

wiersze = file.readlines()
for i in wiersze:
    podzial1 = i.split('. ')[1]
    podzial2 = podzial1.split(' has ')
    imie = podzial2[0]
    podzial3 = podzial2[1].split(' and ')
    oczy = podzial3[0]
    podzial4 = podzial3[1].split(' is ')
    wzrost = podzial4[0].split(' ')[1]
    slownik[imie] = {'height': wzrost, 'eyes': oczy}

print(slownik)
