from abc import ABC, abstractmethod
import re

class PasswordValidatorAbs(ABC):
    def __init__(self, pw):
        self.pw = pw
        self.errors = []

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
        if re.search(r'[0-9]', self.pw) is None:
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
        return "Valid Password" if not self.errors else self.errors

class ValidationRule2(PasswordValidatorAbs):
    def validate_pass(self):
        self.errors.clear()
        if len(self.pw) <= 6:
            self.errors.append("Invalid Password: Length must be more than 6 Characters")
        self.has_upper()
        self.has_lower()
        self.has_num()
        return "Valid Password" if not self.errors else self.errors

class ValidationRule3(PasswordValidatorAbs):
    def validate_pass(self):
        self.errors.clear()
        if len(self.pw) <= 16:
            self.errors.append("Invalid Password: Length must be more than 16 Characters")
        self.has_upper()
        self.has_lower()
        self.has_underscore()
        return "Valid Password" if not self.errors else self.errors

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
