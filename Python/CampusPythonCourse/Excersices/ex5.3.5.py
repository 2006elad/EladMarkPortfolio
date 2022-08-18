def abs_is_one(num_1, num_2):
    if abs(num_1 - num_2) == 1:
        return True
    else:
        return False


def abs_is_bigger_than_one(num_1, num_2):
    if abs(num_1 - num_2) >= 2:
        return True
    else:
        return False


def distance(num1, num2, num3):
    if (abs_is_one(num1, num2) or abs_is_one(num1, num3)) and \
            (abs_is_bigger_than_one(num1, num2) or abs_is_bigger_than_one(num1, num3)):
        return True
    else:
        return False


num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
num3 = int(input("Enter num3"))
print(distance(num1, num2, num3))
