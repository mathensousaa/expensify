import re


class Validation:
    def __init__(self) -> None:
        pass

    def is_empty(value):
        if value == "":
            return True
        else:
            return False

    def is_valid_email(email):
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if re.match(email_regex, email):
            return True
        else:
            return False

    def is_valid_password(password):
        if len(password) < 8:
            return False

        if not any(c.isdigit() for c in password):
            return False

        if not any(c.isalpha() for c in password):
            return False

        if not any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in password):
            return False

        return True
