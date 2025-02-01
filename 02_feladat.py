'''Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, amely True értékkel tér vissza, ha a paraméterként átvett listaelemek (egész számok) között van páros, ellenkező esetben a visszatérési érték False! A program tartalmazza a függvény hívását is!'''

def paros_e(list):
    
    for i in list:
        if i % 2 == 0:
            return False
        else: 
            return True


# szamok =  input('adja meg a szamokat (szóközt rakjon a számok kozé): ').split( )
szamok = [1,2,3,1,7,1]
print('parosak e:' ,paros_e(szamok))