def fahrenheit_to_celsius(temp_f):
    temp_c = (temp_f - 32) * 5/9
    return round(temp_c, 3)
def closest_higher_mod_5(x):
    remainder = x % 5
    if remainder == 0:
        print(x)
    elif x % 5 != 0:
        while remainder != 0:
            x += 1
            remainder = x % 5
    print(x - 1)
