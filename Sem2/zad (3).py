def ReverseWord(word):
    word = word[::-1]
    return word

def IsPalindrome(word):
    if word == ReverseWord(word):
        return (f"{word} is palindorme!")
    else:
        return (f"{word} is not palindrome")

print(ReverseWord("alamakota"))
print(IsPalindrome("alamakota"))

print(ReverseWord("kajak"))
print((IsPalindrome("kajak")))