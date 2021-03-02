
# from : https://docs.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year
# To determine whether a year is a leap year, follow these steps:
# 1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# 2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# 3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# 4. The year is a leap year (it has 366 days).
# 5. The year is not a leap year (it has 365 days).
def is_leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            return True if year % 400 == 0 else False
        else:
            return True
    else:
        return False


def get_date(date: str) -> (int, int, int):

    date_parts = date.split("/")
    if len(date_parts) != 3:
        raise ValueError(f"Wrong date format: {date}")

    try:
        day = int(date_parts[0])
        month = int(date_parts[1])
        year = int(date_parts[2])
    except:
        raise ValueError(f"Unable to convert date: {date}")

    if day <= 0 or day > 31:
        raise ValueError(f"Wrong day input: {day}")

    if month <= 0 or day > 12:
        raise ValueError(f"Wrong month input: {month}")

    if year < 1901 or day > 2999:
        raise ValueError(f"Wrong year input: {year}")

    return (day, month, year)


def _calculate_number_of_days_for_date(day: int, month: int, year: int) -> int:
    number_of_days = [31, 29 if is_leap_year(
        year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = [m for m in number_of_days[:month]]
    return sum(days)+day


def calculate_number_of_days(from_day: int, from_month: int, from_year: int, to_day: int, to_month: int, to_year: int) -> int:
    if from_year > to_year:
        temp_day, temp_month, temp_year = from_day, from_month, from_year
        from_day, from_month, from_year = to_day, to_month, to_year
        to_day, to_month, to_year = temp_day, temp_month, temp_year

    days_between_years = [366 if is_leap_year(
        y) else 365 for y in range(from_year, to_year)]

    total_days = sum(days_between_years)

    from_total_days = _calculate_number_of_days_for_date(
        from_day, from_month, from_year)

    to_total_days = _calculate_number_of_days_for_date(
        to_day, to_month, to_year)

    total_days += to_total_days - from_total_days
    return total_days - 1
