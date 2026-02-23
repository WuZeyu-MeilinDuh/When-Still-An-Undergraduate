
# Using recursion to convert any number to any numerical system
def deci2x_recursion(n, base):
	convertString = "0123456789ABCDEF"
	if n < base:
		return convertString[n]
	else:
		return deci2x_recursion(n // base, base) + convertString[n % base]
#deci2x_recursion ends.

# Using looping to convert any number to any numerical system
def deci2x_no_recursion(n, base):
    convertString = "0123456789ABCDEF"
    result = ""
    remainder_list = []  

    dividend = n 
    quotient = dividend // base 
    remainder = dividend % base 


    if quotient == 0:
        result = convertString[remainder]
        return result


    while quotient > 0:
        remainder_list.insert(0, convertString[remainder])
        dividend = quotient
        quotient = dividend // base
        remainder = dividend % base
        if quotient == 0:
            remainder_list.insert(0, convertString[remainder])

    for item in remainder_list:
        result += str(item)
        
    return result

#deci2x_no_recursion ends.

# main codes
print('please input a decimal number: ')
input_str = input()
if input_str.isdigit():
    dec_num = int(input())
    print('you input decimal number is: , the corresponding binary number is(using recursion algorithm): ' + deci2x_recursion(dec_num, 2))
    print('you input decimal number is: , the corresponding binary number is(using non-recursion algorithm): ' + str(deci2x_no_recursion(dec_num, 2)))

    print('you input decimal number is: , the corresponding hexadecimal number is(using recursion algorithm): ' + deci2x_recursion(dec_num, 16))
    print('you input decimal number is: , the corresponding hexadecimal number is(using non-recursion algorithm): ' + str(deci2x_no_recursion(dec_num, 16)))
else:
    print('your input isn\'t an integer.')

# Using a general algorithm to convert any number to any numerical system

def deci2x_no_recursion(n, base):
    convertString = "0123456789ABCDEF"
    result = ""

    dividend = n 
    quotient = dividend // base 
    remainder = dividend % base

    result = convertString[remainder]

    while quotient > 0:
        dividend = quotient
        quotient = dividend // base
        remainder = dividend % base
        result = convertString[remainder] + result

    return result
#deci2x_no_recursion ends.