data = ("self", "py", 1.543)
format_string = "Hello {0[0]}.{0[1]} learner, you have only {0[2]:.1f} " \
                "units left before you master the course!".format(data)

print(format_string)