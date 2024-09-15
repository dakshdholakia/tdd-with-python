from src.pass_val.pass_val import PasswordValidatorRule, PasswordValidatorAbs


# basic password validation
def test_iter1():
    assert PasswordValidatorRule.get_validator(1, "Bhadresss_123") == "Valid Password"

# rules abstraction
def test_iter2():
    val = PasswordValidatorRule.get_validator(2, "Bhadresss123")
    assert val.validate_pass() == "Valid Password"
    val = PasswordValidatorRule.get_validator(3, "Bhadresssbhai_12345")
    assert val.validate_pass() == "Valid Password"

def test_iter3():
    val = PasswordValidatorRule.get_validator(3, "Bhadresss_123")
    assert val.validate_pass() == "Invalid Password: Length must be more than 16 Characters"