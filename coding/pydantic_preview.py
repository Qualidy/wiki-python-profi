

zahl:int = 5


def meine_funktion(zahl:int) -> int:
    return zahl

def test_meine_funktion():
    eingabewerte = [1,2,3]
    ausgabewerte = [1,2,3]
    for wert in zip(eingabewerte, ausgabewerte):
        assert wert[1] == meine_funktion(wert[0])
    