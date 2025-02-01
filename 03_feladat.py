'''Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! A program tartalmazza a függvény hívását is!'''

def harommal_oszthatok(list):
    db = 0
    for i in list:
        if i % 3 == 0:
            db += 1
    return db


szamok =  input('adja meg a szamokat (szóközt rakjon a számok kozé): ').split( )
print('3 oszthatok:' ,harommal_oszthatok(szamok))