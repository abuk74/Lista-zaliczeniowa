from Zad2 import menPPM
from Zad2 import womanPPM

def test_ifCaloriesAreMoreThan0ForMan():
    assert menPPM(90, 180, 20) > 0

def test_ifCaloriesAreMoreThan0ForWoman():
    assert womanPPM(70, 180, 20) < 0 #tutaj specjalnie <0 bo sprawdzam czy działa