from src.leap_year.leap_year import leapyr

def test_leap_year():
    assert leapyr(2013) == "Not a leap year"

def test_leap_year_pos():
    assert leapyr(2016) == "Leap Year"

