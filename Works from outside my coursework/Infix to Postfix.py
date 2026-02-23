

precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

def infix_to_postfix(expression):
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
expression = '2+4*(2^3-6)^(1+2*2)-5'
print('infix = ' + expression)

#postfix = infix_to_postfix(expression.replace('^', '**'))
postfix = infix_to_postfix(expression)
print('postfix = ' + str(postfix))

result = evaluate_postfix(postfix)
print('evaluation = ' + str(result))
