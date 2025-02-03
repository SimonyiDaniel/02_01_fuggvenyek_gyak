'''Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! A program tartalmazza a függvény hívását is!'''


def harommal_oszthatok(list):
    db = 0
    for i in list:
        if i % 3 == 0:
            db += 1
    return db



szamok = [1, 9, 3, 1, 2, 1]
print('Hárommal osztható számok:', harommal_oszthatok(szamok))