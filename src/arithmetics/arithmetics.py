import operator as ops

op = {
    '+': ops.add,
    '-': ops.sub,
    '*': ops.mul,
    '/': ops.floordiv,
    '**': ops.pow,
    '^': ops.pow
}

def precedence(oper):
    if oper in ('+', '-'):
        return 1
    elif oper in ('*', '/'):
        return 2
    elif oper in ('**', '^'):
        return 3
    else:
        return 0

def is_operator(oper):
    op_list = ['+', '-', '/', '*', '^', '**']
    return str(oper) in op_list

def apply_operator(operands, operators):
    right = operands.pop()
    left = operands.pop()
    operator = operators.pop()
    operands.append(ops[operator](left, right))

def solve(expression):
    operators = []
    operands = []

    i = 0
    exp = expression[i]

    if exp == '(':
        operators.append(exp)

    elif exp.isdigit() or (exp[0] == '-' and len(exp) > 1 and exp[1:].isdigit()):
        operands.append(int(exp))

    elif exp == ')':
        # Apply all operators until '(' is found
        while operators and operators[-1] != '(':
            apply_operator(operands, operators)
        operators.pop()  # Pop the '('

    elif is_operator(exp):
        # Handle operator precedence
        while (operators and operators[-1] != '(' and
               precedence(operators[-1]) >= precedence(exp)):
            apply_operator(operands, operators)
        operators.append(exp)

        i += 1

    while operators:
        apply_operator(operands, operators)

    return operands[0] if operands else 0

def arithmetics(inp):
    # check unmatched parentheses
    open_count = inp.count('(')
    close_count = inp.count(')')
    if open_count != close_count:
        return "Invalid record error"

    # ensure the expression starts and ends with parentheses after removing spaces
    inp = inp.strip()
    if not inp.startswith('(') or not inp.endswith(')'):
        return "Invalid record error"

    # tokenize the input
    expression = inp.replace('(', ' ( ').replace(')', ' ) ').split()

    # for cases where only parentheses exist
    if all(t in "() " for t in inp):
        return 0

    # check for valid expression (numbers, operators, parentheses)
    for exp in expression:
        if not (exp.isdigit() or exp in "() +-*/^"):
            return "Invalid record error"

    # evaluate the expression
    try:
        result = solve(expression)
        return result
    except:
        return "Invalid record error"

    # if inp.count('(') != inp.count(')'):
    #     return "Invalid record error"
    # else:
    #     inp = inp.replace(" ", "") # ((4*5))
    #     inp = inp.replace("(", "") # 4*5))
    #     inp = inp.replace(")", "") # 4*5
    #
    #     spl = inp.split('*')
    #     num = [int(n) for n in spl]
    #
    #     res = 1
    #     for i in num:
    #         res *= i
    #     return res


# 1. Check parentheses
# 2. Remove whitespaces, special characters
# 3. Split input
# 4. Extract arithmetic operators
# 5. Extract numbers
# 6. Function to apply Step 4 on 5
# 7. Final output