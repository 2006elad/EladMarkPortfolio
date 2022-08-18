numbers = iter(list(range(1, 101)))
for i in numbers:
    try:
        next(numbers)
        print(next(numbers))
    except StopIteration:
        break