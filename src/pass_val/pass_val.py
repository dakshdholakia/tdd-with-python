import re

class PasswordValidator:
    def __init__(self, pw):
        self.pw = pw

    def validate_pass(self):
        if not self.min_len():
            return "Invalid Password"
        if not self.has_upper():
            return "Invalid Password"
        if not self.has_lower():
            return "Invalid Password"
        if not self.has_num():
            return "Invalid Password"
        if not self.has_underscore():
            return "Invalid Password"
        return "Valid Password"

    # Helper Functions
    def min_len(self):
        return len(self.pw) > 8

    def has_upper(self):
        return re.search(r'[A-Z]', self.pw) is not None

    def has_lower(self):
        return re.search(r'[a-z]', self.pw) is not None

    def has_num(self):
        return re.search(r'[0-9]', self.pw) is not None

    def has_underscore(self):
        return '_' in self.pw