#!/usr/bin/env python
import argparse
import daycalculator


parser = argparse.ArgumentParser()
parser.add_argument('--fromDate', type=str, required=True,
                    help='the start date (DD/MM/YYYY)')
parser.add_argument('--toDate', type=str, required=True,
                    help='the end date (DD/MM/YYYY)')
args = parser.parse_args()


from_day, from_month, from_year = daycalculator.get_date(args.fromDate)
to_day, to_month, to_year = daycalculator.get_date(args.toDate)

total_days = daycalculator.calculate_number_of_days(
    from_day, from_month, from_year, to_day, to_month, to_year)

print(total_days)
