import unittest
import daycalculator


class TestCalculationMethods(unittest.TestCase):

    def test_calculate_number_of_days(self):
        self.assertEqual(daycalculator.calculate_number_of_days(
            3, 8, 2018, 4, 8, 2018), 0)
        self.assertEqual(daycalculator.calculate_number_of_days(
            1, 1, 2000, 3, 1, 2000), 1)
        self.assertEqual(daycalculator.calculate_number_of_days(
            2, 6, 1983, 22, 6, 1983), 19)
        self.assertEqual(daycalculator.calculate_number_of_days(
            4, 7, 1984, 25, 12, 1984), 173)
        self.assertEqual(daycalculator.calculate_number_of_days(
            3, 1, 1989, 3, 8, 1983), 1979)

    def test_is_leap_year(self):
        self.assertEqual(daycalculator.is_leap_year(2004), True)
        self.assertEqual(daycalculator.is_leap_year(2008), True)
        self.assertEqual(daycalculator.is_leap_year(2012), True)
        self.assertEqual(daycalculator.is_leap_year(2016), True)
        self.assertEqual(daycalculator.is_leap_year(2020), True)

        self.assertEqual(daycalculator.is_leap_year(2005), False)
        self.assertEqual(daycalculator.is_leap_year(2009), False)
        self.assertEqual(daycalculator.is_leap_year(2013), False)
        self.assertEqual(daycalculator.is_leap_year(2017), False)
        self.assertEqual(daycalculator.is_leap_year(2021), False)

    def test_get_date(self):
        self.assertEqual(daycalculator.get_date("02/05/1990"), (2, 5, 1990))
        self.assertEqual(daycalculator.get_date("04/03/1987"), (4, 3, 1987))
        self.assertEqual(daycalculator.get_date("03/08/1983"), (3, 8, 1983))

        self.assertRaises(ValueError, daycalculator.get_date, "01/01")
        self.assertRaises(ValueError, daycalculator.get_date, "not a date")
        self.assertRaises(ValueError, daycalculator.get_date, "02/Feb/1983")
        self.assertRaises(ValueError, daycalculator.get_date, "-01/03/2000")


if __name__ == '__main__':
    unittest.main()
