'''Írj egy programot, amelyben van egy 'kerulet' nevű függvény, amely az egyetlen kötelező paramétere mellett fogadhat több paramétert is! Az opcionális paraméterek száma alapján döntse el milyen síkidomról van szó, és számolja ki a kerületét (0 tetszőleges paraméter: négyzet, 1 tetszőleges paraméter: téglalap, 2 tetszőleges paraméter: háromszőg, 3 vagy több tetszőleges paraméter: sokszög)!

A program tartalmazzon mindegyik síkidom típusra egy-egy függvényhívást!'''

def kerulet(x, *args):
    if len(args) == 0:
        return 4 * x
    elif len(args) == 1:
        return 2 * (x + args[0])
    elif len(args) == 2:
        return x + args[0] + args[1]
    else:
        return sum(args)


print(kerulet(4, 5, 6, 7, 8))