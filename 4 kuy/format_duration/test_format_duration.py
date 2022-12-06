from unittest import TestCase
import format_duration


class Test(TestCase):
    def test_format_duration(self):
        self.assertEqual(format_duration.format_duration(0), 'now')
        self.assertEqual(format_duration.format_duration(59), '59 seconds')
        self.assertEqual(format_duration.format_duration(62), '1 minute and 2 seconds')
        self.assertEqual(format_duration.format_duration(3662), '1 hour, 1 minute and 2 seconds')
        self.assertEqual(format_duration.format_duration(83662), '23 hours, 14 minutes and 22 seconds')
        self.assertEqual(format_duration.format_duration(39983662),
                         '1 year, 97 days, 18 hours, 34 minutes and 22 seconds')
