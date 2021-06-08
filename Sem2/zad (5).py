#Zauważyłem że musze zrezygnowac z mojej konwencji nazewnictwa zadan po prostu 1,2,3 itd bo wtedy from 1 import ReverseWord nie dziłą, chba że coś robię źle xD
from Zad1 import ReverseWord

def test_palindrome():
    assert ReverseWord("kajak") == "kajak"

def test_isNotPalindrome():
    assert ReverseWord("alamakota") != "alamakota"

