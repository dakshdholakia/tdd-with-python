def arithmetics(inp):
    if inp.count('(') != inp.count(')'):
        return "Invalid record error"
    else:
        inp = inp.replace(" ", "") # ((4*5))
        inp = inp.replace("(", "") # 4*5))
        inp = inp.replace(")", "") # 4*5

        spl = inp.split('*')
        num = [int(n) for n in spl]

        res = 1
        for i in num:
            res *= i
        return res


# 1. Check parentheses
# 2. Remove whitespaces, special characters
# 3. Split input
# 4. Extract arithmetic operators
# 5. Extract numbers
# 6. Function to apply Step 4 on 5
# 7. Final output