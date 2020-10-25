import unittest

from main.base.fields.extra_field import ExtraField
from main.base.fields.password_field import PasswordField
from main.base.fields.url_field import URLField
from main.base.fields.user_name_field import UserNameField
from test.fixture.base_test_fixture import url_parsed_field, username_parsed_field, password_parsed_field, \
    extra_parsed_field


class FieldsParsingTest(unittest.TestCase):
    def test_parseURLField(self):
        expected_column_data = url_parsed_field["value"]
        self.assertTrue(URLField.is_applicable(url_parsed_field))

        data = URLField.get_parsed_value(url_parsed_field)
        self.assertNotEqual("", data)
        self.assertEqual(expected_column_data, data)

    def test_parseUserNameField(self):
        expected_column_data = username_parsed_field["value"]
        self.assertTrue(UserNameField.is_applicable(username_parsed_field))

        data = UserNameField.get_parsed_value(username_parsed_field)
        self.assertNotEqual("", data)
        self.assertEqual(expected_column_data, data)

    def test_parsePasswordField(self):
        expected_column_data = password_parsed_field["value"]
        self.assertTrue(PasswordField.is_applicable(password_parsed_field))

        data = PasswordField.get_parsed_value(password_parsed_field)
        self.assertNotEqual("", data)
        self.assertEqual(expected_column_data, data)

    def test_parseExtraField(self):
        expected_column_data = f"{extra_parsed_field['label']} : {extra_parsed_field['value']}\n"
        self.assertTrue(ExtraField.is_applicable(extra_parsed_field))

        data = ExtraField.get_parsed_value(extra_parsed_field)
        self.assertNotEqual("", data)
        self.assertEqual(expected_column_data, data)


if __name__ == '__main__':
    unittest.main()
