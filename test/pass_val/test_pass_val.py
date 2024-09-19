import pytest
from src.pass_val.pass_val import PasswordValidatorRule, PasswordValidatorAbs


# basic password validation
def test_iter1():
    val = PasswordValidatorRule.get_validator(1, "Bhadresss_123")
    assert val.validate_pass() == "Valid Password"

# rules abstraction
def test_iter2():
    val = PasswordValidatorRule.get_validator(2, "Bhadresss123")
    errors = val.validate_pass()
    assert errors == "Valid Password"

    val = PasswordValidatorRule.get_validator(3, "bhadresss12345")
    errors = val.validate_pass()
    assert errors == [
                      "Invalid Password: Length must be more than 16 Characters",
                      "Invalid Password: Must contain at least 1 Upper Case Letter",
                      "Invalid Password: Must contain at least 1 Underscore (_)"
                      ]

def test_iter3():
    val = PasswordValidatorRule.get_validator(3, "bhadresss_123")
    errors = val.validate_pass()
    assert errors == ["Invalid Password: Length must be more than 16 Characters",
                      "Invalid Password: Must contain at least 1 Upper Case Letter"]

def test_iter4():
    # Fails the underscore rule but still valid
    val = PasswordValidatorRule.get_validator("allow_one_fail", "Bhadresss123")
    assert val.validate_pass() == "Valid Password"

    # Fails the uppercase rule but still valid
    val = PasswordValidatorRule.get_validator("allow_one_fail", "bhadresss_123")
    assert val.validate_pass() == "Valid Password"

    # Fails the uppercase and number rule - so invalid
    val = PasswordValidatorRule.get_validator("allow_one_fail", "bhadress_")
    errors = val.validate_pass()
    assert errors == ["Invalid Password: Must contain at least 1 Upper Case Letter",
                      "Invalid Password: Must contain at least 1 Number"]

def test_invalid_rule():
    with pytest.raises(ValueError) as exc:
        PasswordValidatorRule.get_validator(5, "Bhadress")
    assert str(exc.value)

def test_no_lower():
    val = PasswordValidatorRule.get_validator(2, "BHADRESSS_123")
    errors = val.validate_pass()
    assert errors == ["Invalid Password: Must contain at least 1 Lower Case Letter"]

def test_no_num():
    val = PasswordValidatorRule.get_validator(2, "BHADREsss")
    errors = val.validate_pass()
    assert errors == ["Invalid Password: Must contain at least 1 Number"]

def test_len_less_than_8():
    val = PasswordValidatorRule.get_validator(1, "BHADs_1")
    errors = val.validate_pass()
    assert errors == ["Invalid Password: Length must be more than 8 Characters"]

def test_len_less_than_6():
    val = PasswordValidatorRule.get_validator(2, "BHs_1")
    errors = val.validate_pass()
    assert errors == ["Invalid Password: Length must be more than 6 Characters"]

def test_1fail_lt8_low():
    val = PasswordValidatorRule.get_validator("allow_one_fail", "BHADS_1")
    errors = val.validate_pass()
    assert errors == ["Invalid Password: Length must be more than 8 Characters",
                      "Invalid Password: Must contain at least 1 Lower Case Letter"]
