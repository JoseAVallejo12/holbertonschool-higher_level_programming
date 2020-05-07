#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string:
        resul = 0
        ciclos = 0

        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_chars = sorted(roman.keys())

        if type(roman_string) is not str or len(roman_string) is 0:
                return 0

        for roman_values in list(roman_string):
            if not roman_values in roman_chars:
                return 0
            if ciclos > 0 and resul < roman[roman_values]:
                resul = roman[roman_values] - resul
            else:
                resul = resul + roman[roman_values]
            ciclos += 1
        return resul

    return 0
