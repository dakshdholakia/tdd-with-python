from src.leap_year.leap_year import leapyr

def test_leap_year():
    assert leapyr(1997) == "Not a leap year"

def test_leap_year_pos():
    assert leapyr(1996) == "Leap Year"

def test_100_not_400():
    assert leapyr(1800) == "Not a leap year"