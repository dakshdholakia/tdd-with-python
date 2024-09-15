from abc import ABC, abstractmethod
import re

class PasswordValidatorAbs(ABC):
    def __init__(self, pw):
        self.pw = pw

    # each class will implement this abstract method
    @abstractmethod
    def validate_pass(self):
        pass

    # common Helper Functions
    def has_upper(self):
        return re.search(r'[A-Z]', self.pw) is not None

    def has_lower(self):
        return re.search(r'[a-z]', self.pw) is not None

    def has_num(self):
        return re.search(r'[0-9]', self.pw) is not None

    def has_underscore(self):
        return '_' in self.pw

class ValidationRule1(PasswordValidatorAbs):
    def validate_pass(self):
        if len(self.pw) <= 8:
            return "Invalid Password: Length must be more than than 8 Characters"
        if not self.has_upper():
            return "Invalid Password: Must contain at least 1 Upper Case Letter"
        if not self.has_lower():
            return "Invalid Password: Must contain at least 1 Lower Case Letter"
        if not self.has_num():
            return "Invalid Password: Must contain at least 1 Number"
        if not self.has_underscore():
            return "Invalid Password: Must contain at least 1 Underscore (_)"
        return "Valid Password"

class ValidationRule2(PasswordValidatorAbs):
    def validate_pass(self):
        if len(self.pw) <= 6:
            return "Invalid Password: Length must be more than than 6 Characters"
        if not self.has_upper():
            return "Invalid Password: Must contain at least 1 Upper Case Letter"
        if not self.has_lower():
            return "Invalid Password: Must contain at least 1 Lower Case Letter"
        if not self.has_num():
            return "Invalid Password: Must contain at least 1 Number"
        return "Valid Password"

class ValidationRule3(PasswordValidatorAbs):
    def validate_pass(self):
        if len(self.pw) <= 16:
            return "Invalid Password: Length must be more than 16 Characters"
        if not self.has_upper():
            return "Invalid Password: Must contain at least 1 Upper Case Letter"
        if not self.has_lower():
            return "Invalid Password: Must contain at least 1 Lower Case Letter"
        if not self.has_underscore():
            return "Invalid Password: Must contain at least 1 Underscore (_)"
        return "Valid Password"

class PasswordValidatorRule:
    @staticmethod
    def get_validator(rule_type, pw):
        if rule_type == 1:
            return ValidationRule1(pw)
        elif rule_type == 2:
            return ValidationRule2(pw)
        elif rule_type == 3:
            return ValidationRule3(pw)
        else:
            raise ValueError("Invalid rule type")
