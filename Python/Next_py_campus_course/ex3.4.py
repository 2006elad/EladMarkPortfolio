import string


class UsernameContainsIllegalCharacter(Exception):
    """
    Exception when username isn't include Digit, Alpha or "_"
    """
    def __init__(self, username):
        self._username = username

    def error_message(self):
        for i, char in enumerate(self._username):
            if not char.isalpha() and not char.isdigit() and char != "_":
                return "the username:'{}' Contains an illegal character {} at index {}!".format(self._username, char, i)


class UsernameTooShort(Exception):
    def __init__(self, username):
        self._username = username

    def error_message(self):
        return "the username:'{}' is too short(Less than 3)!".format(self._username)


class UsernameTooLong (Exception):
    def __init__(self, username):
        self._username = username

    def error_message(self):
        return "the username:'{}' is too Long(More than 16)!".format(self._username)


class PasswordMissingCharacter(Exception):
    """
    :exception that raised when password missing 1 Dig, 1 Upper, 1 Lower and 1 special
    """
    def __init__(self, password):
        self._password = password

    def error_message(self):
        return "The password:{} is missing a character ".format(self._password)


class PasswordMissingUpperCase(PasswordMissingCharacter):
    def __init__(self, password):
        super().__init__(password)

    def error_message(self):
        return super().error_message() + "(UpperCase)"


class PasswordMissingLowerCase(PasswordMissingCharacter):
    def __init__(self, password):
        super().__init__(password)

    def error_message(self):
        return super().error_message() + "(LowerCase)"


class PasswordMissingDigit(PasswordMissingCharacter):
    def __init__(self, password):
        super().__init__(password)

    def error_message(self):
        return super().error_message() + "(Digit)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __init__(self, password):
        super().__init__(password)

    def error_message(self):
        return super().error_message() + "(Special)"


class PasswordTooShort(Exception):
    def __init__(self, password):
        self._password = password

    def error_message(self):
        return "the password:'{}' is too short(Less than 8)!".format(self._password)


class PasswordTooLong(Exception):
    def __init__(self, password):
        self._password = password

    def error_message(self):
        return "the password:'{}' is too Long(More than 40)!".format(self._password)


def validate_username(username):
    for char in username:
        if not char.isalpha() and not char.isdigit() and char != "_":
            return False
    return True


def check_must_password_characters(password):
    must_list = [False, False, False, False]    # [Big, Small, Num, Punc]
    for char in password:
        if char.isupper():
            must_list[0] = True
        elif char.islower():
            must_list[1] = True
        elif char.isdigit():
            must_list[2] = True
        elif char in string.punctuation:
            must_list[3] = True
    for i, rule_is_found in enumerate(must_list):
        if not rule_is_found:
            return False, i
    return True, None


def check_input(username, password):
    """
    Function that valid user name and password and print "ok" if validate
    :param username: username that must include only alpha, dec or _. len 3-16
    :type: str
    :param password: password must include one upper, one lower, one number and one special sign(punctuation).
    len between 3-16
    :type: str
    :return: None
    """
    try:
        if len(username) < 3:
            raise UsernameTooShort(username)
        elif len(username) > 16:
            raise UsernameTooLong(username)
        elif not validate_username(username):
            raise UsernameContainsIllegalCharacter(username)
        elif len(password) < 8:
            raise PasswordTooShort(password)
        elif len(password) > 40:
            raise PasswordTooLong(password)

        else:
            is_missing, i = check_must_password_characters(password)
            if not is_missing:
                if i == 0:
                    raise PasswordMissingUpperCase(password)
                elif i == 1:
                    raise PasswordMissingLowerCase(password)
                elif i == 2:
                    raise PasswordMissingDigit(password)
                elif i == 3:
                    raise PasswordMissingSpecial(password)

    except UsernameTooShort as e:
        print(e.error_message())
    except UsernameTooLong as e:
        print(e.error_message())
    except UsernameContainsIllegalCharacter as e:
        print(e.error_message())
    except PasswordTooShort as e:
        print(e.error_message())
    except PasswordTooLong as e:
        print(e.error_message())
    except PasswordMissingUpperCase as e:
        print(e.error_message())
    except PasswordMissingLowerCase as e:
        print(e.error_message())
    except PasswordMissingDigit as e:
        print(e.error_message())
    except PasswordMissingSpecial as e:
        print(e.error_message())

    else:
        print("OK")


def main():
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1.", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")


if __name__ == '__main__':
    main()