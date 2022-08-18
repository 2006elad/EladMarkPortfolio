import time
import timeit

real_password = "2678"


def check_password(password):   # Don't change it
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1)     # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True


def crack_password():
    cracked_password_list = ["0", "0", "0", "0"]
    for i in range(4):
        for x in range(0, 10):
            cracked_password_list[i] = str(x)
            start_time = timeit.default_timer()
            pass_right_check = check_password(''.join(cracked_password_list))
            end_time = timeit.default_timer()
            if (int((end_time - start_time) * 10) > (i + 1)) or pass_right_check:
                cracked_password_list[i] = str(x)
                break
    print("".join(cracked_password_list))


crack_password()
