def leapyr(inp_year: int):
    if inp_year % 4 != 0:
        return "Not a leap year"

    elif inp_year % 4 == 0:
        return "Leap Year"