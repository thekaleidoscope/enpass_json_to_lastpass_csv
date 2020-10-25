import unittest

from main.base.fields.url_field import URLField
from main.base.fields.user_name_field import UserNameField
from test.fixture.base_test_fixture import url_parsed_field, userName_parsed_field


class FieldsParsingTest(unittest.TestCase):
    def test_parseURLField(self):
        expected_column_data = url_parsed_field["value"]
        self.assertTrue(URLField.is_applicable(url_parsed_field))

        data = URLField.get_parsed_value(url_parsed_field)
        self.assertNotEqual("", data)
        self.assertEqual(expected_column_data, data)

    def test_parseUserNameField(self):
        expected_column_data = userName_parsed_field["value"]
        self.assertTrue(UserNameField.is_applicable(userName_parsed_field))

        data = UserNameField.get_parsed_value(userName_parsed_field)
        self.assertNotEqual("", data)
        self.assertEqual(expected_column_data, data)


if __name__ == '__main__':
    unittest.main()
