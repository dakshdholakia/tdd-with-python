import re

def add(strnum: str):
    if strnum == "":
        return 0

    if strnum.startswith("//"):
        if strnum[2] == '[':
            # maxsplit 1 (from left of string)
            delimiter_part, strnum = strnum.split("\n", 1)
            # extracting delimiters within square brackets
            cust_dlim = re.findall(r'\[(.*?)\]', delimiter_part)
            #  escape and join multiple delimiters
            cust_dlim = '|'.join(map(re.escape, cust_dlim))
        else:
            # Custom single character delimiter
            delimiter_part, strnum = strnum.split("\n", 1)
            # Extract single delimiter and escape if necessary
            cust_dlim = re.escape(delimiter_part[2:])
    else:
        # Default delimiters
        cust_dlim = ',|\n'

    # splitting the string based on the delimiter
    numbers = re.split(cust_dlim, strnum)
    ans = [int(i) for i in numbers if i and int(i) <= 1000]
    neg = [num for num in ans if num < 0]
    if neg:
        raise Exception("error: negatives not allowed: {' '.join(map(str, neg))}")

    ans_sum = sum(ans)

    return int(ans_sum)