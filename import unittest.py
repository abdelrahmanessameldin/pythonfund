import unittest
from io import StringIO
from unittest.mock import patch


calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"


def days_to_sec(num_of_days, custom_message):
    print(f"{num_of_days} Days are {num_of_days* calculation_to_seconds} {name_of_unit}")
    print(f"{custom_message}")


class TestDaysToSec(unittest.TestCase):
    
    def test_days_to_sec(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            days_to_sec(10, "good")
            expected_output = "10 Days are 864000 seconds\ngood"
            self.assertEqual(fake_out.getvalue().strip(), expected_output)
            

if __name__ == '__main__':
    unittest.main()
