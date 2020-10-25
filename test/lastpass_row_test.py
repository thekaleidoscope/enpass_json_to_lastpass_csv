import unittest

from main.base import LastPassRow
from test.fixture.base_test_fixture import row_with_url


class BaseTest(unittest.TestCase):
    def test_shouldParseURLField(self):
        row_data = LastPassRow.parse(row_with_url)
        self.assertEqual(1, len(row_data))
        expected_row_data = row_with_url["fields"][0]["value"]
        self.assertEquals(expected_row_data, row_data["url"])


if __name__ == '__main__':
    unittest.main()
