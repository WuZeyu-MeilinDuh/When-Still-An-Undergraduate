# Question 5: Roman to Integer
# Please DO NOT modify the given function except the TODO part
# You may have your own functions if necessary


def roman_to_integer(num):
    ''' 
    Given a Roman numeral, convert it to an integer
    parameter num: string
    return: int
    '''
    # TODO part
    # ------- Your code start here -------

    roman_dict = {"I": 1,
                  "V": 5,
                  "X": 10,
                  "L": 50,
                  "C": 100,
                  "D": 500,
                  "M": 1000}
    roman_dict_pro = {"IV": 4,
                       "IX": 9,
                       "XL": 40,
                       "XC": 90,
                       "CD": 400,
                       "CM": 900}
    result = 0
    if "IV" not in num and "IX" not in num and "XL" not in num and "XC" not in num and "CD" not in num and "CM" not in num:
        for i in num:
            result = result + roman_dict[i]
        return result
    else:
        f1 = 0
        f2 = 0
        f3 = 0
        f4 = 0
        f5 = 0
        f6 = 0
        if "IV" in num:
            f1 = roman_dict_pro["IV"]
            result = result - 1 - 5
        if "IX" in num:
            f2 = roman_dict_pro["IX"]
            result = result - 1 - 10
        if "XL" in num:
            f3 = roman_dict_pro["XL"]
            result = result - 10 - 50
        if "XC" in num:
            f4 = roman_dict_pro["XC"]
            result = result - 10 - 100
        if "CD" in num:
            f5 = roman_dict_pro["CD"]
            result = result - 100 - 500
        if "CM" in num:
            f6 = roman_dict_pro["CM"]
            result = result - 100 - 1000
        result = result + f1 + f2 + f3 + f4 + f5 + f6
        for i in num:
            result = result + roman_dict[i]
        return result

    # ------- End of your code -----------


if __name__ == '__main__':
    # Sample test cases
    rom = "IV"
    print(roman_to_integer(rom) == 4)
