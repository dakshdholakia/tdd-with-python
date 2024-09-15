import operator as ops

# Define basic arithmetic operations
op = {
    '+': ops.add,
    '-': ops.sub,
    '*': ops.mul,
    '/': ops.truediv,  # Use truediv for floating-point division
    '**': ops.pow,
    '^': ops.pow
}

# Define operator precedence
def precedence(oper):
    if oper in ('+', '-'):
        return 1
    elif oper in ('*', '/'):
        return 2
    elif oper in ('**', '^'):
        return 3
    else:
        return 0

# Check if a token is an operator
def is_operator(oper):
    return oper in op

# Apply an operator on the operands stack
def apply_operator(operands, operators):
    right = operands.pop()
    left = operands.pop()
    operator = operators.pop()
    operands.append(op[operator](left, right))

# Evaluate a tokenized expression using a stack-based approach
def solve(expression):
    operators = []
    operands = []

    i = 0
    while i < len(expression):
        exp = expression[i]

        if exp == '(':
            operators.append(exp)

        elif exp.isdigit() or (exp[0] == '-' and len(exp) > 1 and exp[1:].isdigit()):
            operands.append(float(exp))  # Use float for fractional calculations

        elif exp == ')':
            # Apply operators inside the parentheses
            while operators and operators[-1] != '(':
                apply_operator(operands, operators)
            operators.pop()  # Remove the '('

        elif is_operator(exp):
            # Handle operator precedence
            while (operators and operators[-1] != '(' and
                   precedence(operators[-1]) >= precedence(exp)):
                apply_operator(operands, operators)
            operators.append(exp)

        i += 1

    # Apply the remaining operators
    while operators:
        apply_operator(operands, operators)

    return operands[0] if operands else 0

def arithmetics(inp):
    # strip spaces and ensure the input is non-empty
    inp = inp.strip()
    if not inp:
        return "Invalid record error"

    # check for balanced parentheses
    open_count = inp.count('(')
    close_count = inp.count(')')
    if open_count != close_count:
        return "Invalid record error"

    # ensure the expression is fully enclosed in parentheses after removing spaces
    clean_inp = inp.replace(" ", "")
    if clean_inp[0] != '(' or clean_inp[-1] != ')':
        return "Invalid record error"

    # tokenize the input
    expression = inp.replace('(', ' ( ').replace(')', ' ) ').split()

    # handle case where only parentheses exist
    if all(t in "() " for t in inp):
        return 0

    # check for valid tokens (numbers, operators, parentheses)
    for exp in expression:
        if not (exp.isdigit() or exp in "() +-*/^"):
            return "Invalid record error"

    return evaluate(expression)

def evaluate(expression):
    try:
        result = solve(expression)
        return int(result) if result.is_integer() else result  # Return integer if possible
    except:
        return "Invalid record error"
