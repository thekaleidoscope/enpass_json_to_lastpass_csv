import unittest

from main.base import LastPassRow
from main.base.fields.name_field import NameField
from main.base.fields.password_field import PasswordField
from main.base.fields.url_field import URLField
from main.base.fields.user_name_field import UserNameField
from test.fixture.base_test_fixture import row_with_all_fields


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.row_parse = LastPassRow.parse(row_with_all_fields)

    def test_shouldParseEnpassJSON(self):
        self.assertTrue(len(self.row_parse) > 0)

    def test_shouldParseURLField(self):
        expected_row_data = getColumnValueFromEnpassJSON(URLField.enpass_field_name)
        self.assertEquals(expected_row_data, self.row_parse[URLField.lastpass_field_name])

    def test_shouldParseUserNameField(self):
        expected_row_data = getColumnValueFromEnpassJSON(UserNameField.enpass_field_name)
        self.assertEquals(expected_row_data, self.row_parse[UserNameField.lastpass_field_name])

    def test_shouldParsePasswordField(self):
        expected_row_data = getColumnValueFromEnpassJSON(PasswordField.enpass_field_name)
        self.assertEquals(expected_row_data, self.row_parse[PasswordField.lastpass_field_name])

    def test_shouldParseNameField(self):
        expected_row_data = row_with_all_fields[NameField.enpass_field_name]
        self.assertEquals(expected_row_data, self.row_parse[NameField.lastpass_field_name])


def getColumnValueFromEnpassJSON(column_name):
    enpass_column = next(column for column in row_with_all_fields["fields"] if column["label"] == column_name)
    return enpass_column["value"]


if __name__ == '__main__':
    unittest.main()
