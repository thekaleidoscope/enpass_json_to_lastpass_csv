import unittest

from main.base.fields.url_field import URLField
from test.fixture.base_test_fixture import url_parsed_field


class FieldsParsingTest(unittest.TestCase):
    def test_parseURLField(self):
        expected_column_data = url_parsed_field["value"]
        self.assertTrue(URLField.is_applicable(url_parsed_field))

        data = URLField.get_parsed_value(url_parsed_field)
        self.assertNotEqual("", data)
        self.assertEqual(expected_column_data, data)


if __name__ == '__main__':
    unittest.main()
