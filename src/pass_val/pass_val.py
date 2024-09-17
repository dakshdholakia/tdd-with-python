from abc import ABC, abstractmethod
import re

class PasswordValidatorAbs(ABC):
    def __init__(self, pw):
        self.pw = pw
        self.errors = []
        self.valid = "Valid Password"

    # each class will implement this abstract method
    @abstractmethod
    def validate_pass(self):
        pass

    # common Helper Functions
    def has_upper(self):
        if re.search(r'[A-Z]', self.pw) is None:
            self.errors.append("Invalid Password: Must contain at least 1 Upper Case Letter")

    def has_lower(self):
        if re.search(r'[a-z]', self.pw) is None:
            self.errors.append("Invalid Password: Must contain at least 1 Lower Case Letter")

    def has_num(self):
        if re.search(r'\d', self.pw) is None:
            self.errors.append("Invalid Password: Must contain at least 1 Number")

    def has_underscore(self):
        if '_' not in self.pw:
            self.errors.append("Invalid Password: Must contain at least 1 Underscore (_)")


class ValidationRule1(PasswordValidatorAbs):
    def validate_pass(self):
        self.errors.clear()
        if len(self.pw) <= 8:
            self.errors.append("Invalid Password: Length must be more than 8 Characters")
        self.has_upper()
        self.has_lower()
        self.has_num()
        self.has_underscore()
        return self.valid if not self.errors else self.errors

class ValidationRule2(PasswordValidatorAbs):
    def validate_pass(self):
        self.errors.clear()
        if len(self.pw) <= 6:
            self.errors.append("Invalid Password: Length must be more than 6 Characters")
        self.has_upper()
        self.has_lower()
        self.has_num()
        return self.valid if not self.errors else self.errors

class ValidationRule3(PasswordValidatorAbs):
    def validate_pass(self):
        self.errors.clear()
        if len(self.pw) <= 16:
            self.errors.append("Invalid Password: Length must be more than 16 Characters")
        self.has_upper()
        self.has_lower()
        self.has_underscore()
        return self.valid if not self.errors else self.errors

# allow one rule failure
class ValidationAllowOneFail(PasswordValidatorAbs):
    def validate_pass(self):
        self.errors.clear()
        rule_failures = []

        if len(self.pw) <= 8:
            rule_failures.append("Invalid Password: Length must be more than 8 Characters")
        if re.search(r'[a-z]', self.pw) is None:
            rule_failures.append("Invalid Password: Must contain at least 1 Lower Case Letter")
        if re.search(r'[A-Z]', self.pw) is None:
            rule_failures.append("Invalid Password: Must contain at least 1 Upper Case Letter")
        if re.search(r'\d', self.pw) is None:
            rule_failures.append("Invalid Password: Must contain at least 1 Number")
        if '_' not in self.pw:
            rule_failures.append("Invalid Password: Must contain at least 1 Underscore (_)")

        # Allow one failure
        if len(rule_failures) > 1:
            self.errors.extend(rule_failures)
            return self.errors
        return self.valid

class PasswordValidatorRule:
    @staticmethod
    def get_validator(rule_type, pw):
        if rule_type == 1:
            return ValidationRule1(pw)
        elif rule_type == 2:
            return ValidationRule2(pw)
        elif rule_type == 3:
            return ValidationRule3(pw)
        elif rule_type == "allow_one_fail":
            return ValidationAllowOneFail(pw)
        else:
            raise ValueError("Invalid rule type")
