def binary_to_decimal(binary_str):
    """returns the decimal number for the given binary digits"""
    binary_str = str(binary_str)
    n = len(str(binary_str))
    i = 0
    numbers = []
    while i < n:
        numbers.append(int(binary_str[-(n-i)])*(2**(n-i-1)))
        i += 1
    return sum(numbers)

assert binary_to_decimal('1011') == 11
assert binary_to_decimal('00000') == 0
assert binary_to_decimal('00001') == 1
assert binary_to_decimal('11111') == 31


def decimal_to_binary(decimal_num):
    """the binary representation of the given decimal number"""
    #take my decimal number
    #keep dividing by base (2): loop?
    #I want to record the remainders some how: maybe store in a list?
    #I want to stop when my thing I'm dividing by is less than the base: conditional or loop stopper: while loop?

    #special case for 0 and 1

    if decimal_num == 0 or decimal_num == 1:
        return str(decimal_num)

    remainders = []

    while decimal_num > 0:

        remainder = decimal_num % 2
        remainders.append(str(remainder))
        print("Remainder: ", remainder)

        decimal_num = decimal_num // 2
        print("Decimal: ", decimal_num)
    
    print("".join(remainders))
    return "".join(remainders)[::-1]
  
assert decimal_to_binary(0) == '0'
# #result of our code    expected result
assert decimal_to_binary(1) == '1'
assert decimal_to_binary(2) == '10'
assert decimal_to_binary(55) == '110111'
assert decimal_to_binary(389) == '110000101'

#STRETCH: can you use what you have written so far to create hex_to_decimal() and decimal_to_hex() functions?

my_string = 'abcd'

def hex_to_decimal(hex_string):
    # I'm avoiding just using int(__, 16) on the whole number because that seemed outside of the spirit of the exercise
    """returns a decimal number from a given hexadecimal number"""
    i = 0
    result = 0
    
    for _ in str(hex_string[::-1]):
        # using builtin python conversion to avoid an unneccessarily long 
        # and pointless case switch statement to convert ABCDEF to dec equivalent digits
        result += int(_, 16) * 16 ** i
        i += 1
    return result

assert hex_to_decimal('abcd') == 43981
assert hex_to_decimal('abcdef') == 11259375
assert hex_to_decimal('abc00def') == 2881490415
assert hex_to_decimal('a1b2c3') == 10597059

def decimal_to_hex(decimal_num):
    """returns a hexadecimal number from a given decimal number"""
    # Again, I'm avoiding just using hex() on the whole string because that seemed outside of the spirit of the exercise
    hex_digits = []
    while decimal_num > 0:
        # using a hex() builtin because the case switch statement to convert 10 11 12 13 14 15
        # to a b c d e f is long and unnecessary again 
        hex_digits.append(hex(decimal_num % 16)[-1])
        decimal_num = decimal_num // 16
    return "".join(hex_digits[::-1])

assert decimal_to_hex(43981) == 'abcd'
assert decimal_to_hex(11259375) == 'abcdef'
assert decimal_to_hex(2881490415) == 'abc00def'
assert decimal_to_hex(10597059) == 'a1b2c3'

def decimal_to_arbitrary(decimal_num, arb_base):
    """returns a number in an arbitrary base (up to base 62) from a given decimal number"""
    symbols = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    arb_digits = []
    while decimal_num > 0:
        arb_digits.append(str(symbols[(decimal_num % arb_base)]))
        decimal_num = decimal_num // arb_base
    return "".join(arb_digits[::-1])

assert decimal_to_arbitrary(389, 2) == '110000101'
assert decimal_to_arbitrary(43981, 16) == 'abcd'
assert decimal_to_arbitrary(32109809, 42) == 'adgzb'
assert decimal_to_arbitrary(10123114140, 62) == 'b35yqw'

def arbitrary_to_decimal(arbitrary_str, arb_base):
    """returns a decimal number from a given in an arbitrary base (up to base 62)"""
    symbols = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    i = 0
    result = 0

    for _ in str(arbitrary_str[::-1]):
        result +=  symbols.index(_) * arb_base**i
        i += 1
    return result

assert arbitrary_to_decimal('110000101', 2) == 389
assert arbitrary_to_decimal('abcd', 16) == 43981
assert arbitrary_to_decimal('adgzb', 42) == 32109809
assert arbitrary_to_decimal('b35yqw', 62) == 10123114140

        
    