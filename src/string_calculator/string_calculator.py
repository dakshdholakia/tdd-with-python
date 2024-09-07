import re

def add(strnum: str):
    if strnum == "":
        return 0
    else:
        rep = strnum.replace('\n', ',')
        rep = rep.split(',')
        ans = [eval(i) for i in rep]
        ans_sum = sum(ans)
        return int(ans_sum)
