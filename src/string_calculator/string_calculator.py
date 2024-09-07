def add(strnum: str):
    if strnum == "":
        return 0
    else:
        ans = strnum.split(sep=',')
        ans = [eval(i) for i in ans]
        ans_sum = sum(ans)
        return int(ans_sum)
