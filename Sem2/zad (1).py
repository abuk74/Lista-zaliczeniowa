def Check():
    try:
        postcode = int(input("Podaj polski kod pocztowy (bez przecinka bo po co :P): "))
        return postcode
    except ValueError:
        return False

def PolishPostcodeChecker():
    postcode = Check()
    if postcode== False:
        print("Kod pocztowy MUSI zawierać wyłącznie cyfry!")
        print(postcode)
    else:
        print(postcode)
        if len(str(postcode)) != 5:
            print("Kod pocztowy musi zawierać 5 cyfr!")
        else:
            print("Prawidłowy kod pocztowy!")
            f = open("kodypocztowe.txt", "a+")
            f.write(f"{str(postcode)}\n")
            f.close()

def Menu():
    PolishPostcodeChecker()
    ans = input("Czy chcesz podać kolejny kod pocztowy: ")
    while ans.upper() == "TAK":
        PolishPostcodeChecker()
        ans = input("Czy chcesz podać kolejny kod pocztowy:")

print(Menu())