from src.pass_val.pass_val import PasswordValidator

# basic password validation
def test_iter1():
    assert PasswordValidator("Bhadresss_123").validate_pass() == "Valid Password"