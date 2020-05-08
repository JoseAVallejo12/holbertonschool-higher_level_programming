#!/usr/bin/python3
def roman_to_int(roman_string):

    if type(roman_string) is not str or len(roman_string) is 0:
        return 0

    roman = {
        'I': 1, 'V': 5,
        'X': 10, 'L': 50,
        'C': 100, 'D': 500,
        'M': 1000
    }
    resul = 0
    ciclos = 0
    prev_val = 0

    for roman_key in roman_string:
        if ciclos > 0 and prev_val < roman[roman_key]:
            resul -= prev_val
            resul = resul + (roman[roman_key] - prev_val)
        else:
            resul = resul + roman[roman_key]

        ciclos += 1
        prev_val = roman[roman_key]
    return resul
