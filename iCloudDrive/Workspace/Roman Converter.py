romans  = {"I":1,
           "V":5,
           "X":10,
           "L":50,
           "C":100,
           "D":500,
           "M":1000}


def converter(roman_input):
    roman_input_split = []
    global romans

    for letter in roman_input:
        roman_input_split.append(romans[letter])

    decimal = 0
    i = 0
    while i < len(roman_input_split):
        if i == len(roman_input_split)-1:
            decimal += roman_input_split[i]
        else:
            if roman_input_split[i] < roman_input_split[i+1]:
                decimal += roman_input_split[i+1] - roman_input_split[i]
                i += 1
            else:
                decimal += roman_input_split[i]
        i += 1
    print(decimal)

roman_input = input("Input Roman Number to Convert to Decimal: ")
converter(roman_input)
