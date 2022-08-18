import itertools


def gen_secs():
    for second in range(60):
        yield second


def gen_minutes():
    for minute in range(60):
        yield minute


def gen_hours():
    for hour in range(0, 24):
        yield hour


def gen_time():
    for hour in list(gen_hours()):
        for minute in list(gen_minutes()):
            for second in list(gen_secs()):
                yield "{}:{}:{}".format(str(hour).zfill(2), str(minute).zfill(2), str(second).zfill(2))


def gen_years(start=2019):
    for year in itertools.count(start):
        yield year


def gen_months():
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    full_month = [1, 3, 5, 7, 8, 10, 12]
    not_full_month = [4, 6, 9, 11]
    if month in full_month:
        yield 31
    elif month in not_full_month:
        yield 30
    elif leap_year:
        yield 29
    else:
        yield 28


def gen_date():
    for year in gen_years():
        is_leap = False
        for month in gen_months():
            if year % 4 == 0 and not year % 100:
                is_leap = True
            elif year % 400 == 0:
                is_leap = True
            for day in range(1, next(gen_days(month, is_leap)) + 1):
                for time in gen_time():
                    yield "{}/{}/{} {}".format(str(day).zfill(2), str(month).zfill(2), str(year).zfill(2), time)


def main():
    date_gen = gen_date()
    for i in itertools.count(1, 100):
        if i % 100 == 0:
            print(next(date_gen))
        else:
            next(date_gen)


if __name__ == '__main__':
    main()
