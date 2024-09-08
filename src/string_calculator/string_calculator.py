import re

def add(strnum: str):
    if strnum == "":
        return 0

    if strnum.startswith("//"):
        # maxsplit 1 (from left of string)
        delimiter_part, strnum = strnum.split("\n", 1)
        # extracting custom delimiter
        cust_dlim = delimiter_part[2:]
        # escaping special characters
        cust_dlim = re.escape(cust_dlim)
    else:
        # Default delimiters
        cust_dlim = ',|\n'

    # splitting the string based on the delimiter
    numbers = re.split(cust_dlim, strnum)
    ans = [int(i) for i in numbers if i]
    neg = [num for num in numbers if num < 0]
    if neg:
        raise Exception("error: negatives not allowed: {' '.join(map(str, neg))}")

    ans_sum = sum(ans)
    return int(ans_sum)
