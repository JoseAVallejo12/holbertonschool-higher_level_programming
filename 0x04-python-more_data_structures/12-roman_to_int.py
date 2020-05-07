#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        resul = 0
        ciclos = 0
        for roman_values in list(roman_string):  
            if ciclos > 0 and resul < roman[roman_values]:
                resul = roman[roman_values] - resul
            else:
                resul = resul + roman[roman_values]
            ciclos += 1
        return resul
    return 0
