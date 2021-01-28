
#Bazuje na:
#https://stackoverflow.com/questions/2192533/function-to-return-date-of-easter-for-the-given-year
#https://dateutil.readthedocs.io/en/stable/_modules/dateutil/easter.html

import datetime

def Easter(year, method=3): # 3 to kalendarz gregorianski

    if not (1 <= method <= 3):
        raise ValueError("invalid method")

    # g - Golden year - 1
    # c - Century
    # h - (23 - Epact) mod 30
    # i - Number of days from March 21 to Paschal Full Moon
    # j - Weekday for PFM (0=Sunday, etc)
    # p - Number of days from March 21 to Sunday on or before PFM
    #     (-6 to 28 methods 1 & 3, to 56 for method 2)
    # e - Extra days to add for method 2 (converting Julian
    #     date to Gregorian date)

    y = year
    g = y % 19
    e = 0
    c = y//100
    h = (c - c//4 - (8*c + 13)//25 + 19*g + 15) % 30
    i = h - (h//28)*(1 - (h//28)*(29//(h + 1))*((21 - g)//11))
    j = (y + y//4 + i + 2 - c + c//4) % 7

    # p can be from -6 to 56 corresponding to dates 22 March to 23 May
    # (later dates apply to method 2, although 23 May never actually occurs)
    p = i - j + e
    d = 1 + (p + 27 + (p + 6)//40) % 31
    m = 3 + (p + 26)//30
    return datetime.date(int(y), int(m), int(d))
