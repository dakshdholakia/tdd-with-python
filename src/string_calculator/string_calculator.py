import re

def add(strnum: str):
    if strnum == "":
        return 0
    else:
        # rep = strnum.replace('\n', ',')
        # rep = rep.split(',')
        if strnum.startswith("//"):
            # maxsplit 1 (from left of string)
            delimiter_part, strnum = strnum.split("\n", 1)
            # extracting custom delimiter
            cust_dlim = delimiter_part[2:]
            # escaping special characters
            cust_dlim = re.escape(cust_dlim)
        else:
            # Default delimiters
            delimiter = ',|\n'

        # splitting the string based on the delimiter
        numbers = re.split(cust_dlim, strnum)
        ans = [int(i) for i in numbers if i]
        ans_sum = sum(ans)
        return int(ans_sum)
