def add_two_roman_numerals(first_numeral, second_numeral):
    return number_to_roman(roman_to_number(first_numeral) + roman_to_number(second_numeral))


# I = 1 V = 5 X = 10 L = 50 C = 100 D = 500 M = 1000
def number_to_roman(number):
    roman = "I" * number
    return roman\
        .replace("I" * 1000, "M")\
        .replace("I" * 900, "CM")\
        .replace("I" * 500, "D")\
        .replace("I" * 400, "CD")\
        .replace("I" * 100, "C")\
        .replace("I" * 90, "XC")\
        .replace("I" * 50, "L")\
        .replace("I" * 40, "XL")\
        .replace("I" * 10, "X")\
        .replace("I" * 9, "IX")\
        .replace("I" * 5, "V")\
        .replace("I" * 4, "IV")


def roman_to_number(roman):
    number = (
        roman.count("M") * 1000 +
        roman.count("D") * 500 +
        roman.count("C") * 100 +
        roman.count("L") * 50 +
        roman.count("X") * 10 +
        roman.count("V") * 5 +
        roman.count("I")
        )
    fix_lower_denomination = (
        roman.count("IV") +
        roman.count("IX") +
        roman.count("XL") * 10 +
        roman.count("XC") * 10 +
        roman.count("CD") * 100 +
        roman.count("CM") * 100
        ) * 2
    return number - fix_lower_denomination
