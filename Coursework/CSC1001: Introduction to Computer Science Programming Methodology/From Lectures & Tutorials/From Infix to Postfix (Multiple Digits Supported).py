def digit_to_number(lst):
    a = lst[-1]
    if len(lst) > 1:
        for i in range(2, len(lst) + 1):
            a = a + lst[-i]*(10**(i-1))
    return a

def convert_to_single_note(expre):
    expr = expre + "="
    result = []
    for i in range(0, len(expr) - 1):
        item = expr[i]
        if item.isdigit() and i == 0:
            lst = []
            k = i
            while expr[k].isdigit():
                lst.append(int(expr[k]))
                k = k + 1
            result.append(str(digit_to_number(lst)))
        elif item.isdigit() and not expr[i - 1].isdigit() and i >= 1:
            lst1 = []
            m = i
            while expr[m].isdigit():
                lst1.append(int(expr[m]))
                m = m + 1
            result.append(str(digit_to_number(lst1)))
        elif item.isdigit() and expr[i - 1].isdigit():
            continue
        else:
            result.append(item)
    return result


precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

def infix_to_postfix(expression1):
    expression = convert_to_single_note(expression1)
    stack = [] 
    output = [] 
    for token in expression:
        if token.isdigit():
            output.append(token)
        elif token =='(': 
            stack.append(token)
        elif token ==')': 
            while stack and stack[-1]!='(':
                output.append(stack.pop())
            stack.pop() 
        else: 
            while stack and precedence.get(stack[-1],0)>= precedence[token]:
                output.append(stack.pop())
            stack.append(token)   
    
    while stack:
        output.append(stack.pop())
    return output


def evaluate_postfix(postfix):
    stack =[]
    for token in postfix:
        if token.isdigit(): 
            stack.append(float(token))
        else: 
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            if token == '+':
                stack.append(operand_1 + operand_2)
            elif token =='-':
                stack.append(operand_1-operand_2)
            elif token =='*':
                stack.append(operand_1 * operand_2)
            elif token == '/':
                stack.append(operand_1 / operand_2)
            elif token =='^':
                stack.append(operand_1 ** operand_2)
    return stack[0]  


#expression = '12.03+24.02*(2^3-6)^(1+2*2)-15'
expression = '211+4*(2^3-6)^(1+2*2)-5'
print('infix = ' + expression)

#postfix = infix_to_postfix(expression.replace('^', '**'))
postfix = infix_to_postfix(expression)
print('postfix = ' + str(postfix))

result = evaluate_postfix(postfix)
print('evaluation = ' + str(result))