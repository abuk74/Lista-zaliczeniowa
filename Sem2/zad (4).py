def womanPPM(weight, height, age):
    return 655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)

def menPPM(weight, height, age):
    return 66.5 + (13.75 * weight) + (5.003 * height) - (6.775 * age)

print(womanPPM(70, 180, 20))
print(menPPM(90, 180, 20))