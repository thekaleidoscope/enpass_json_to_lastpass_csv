import unittest

from main.base import lastpass_row
from main.base.fields.extra_field import ExtraField
from main.base.fields.favourite_field import FavouriteField
from main.base.fields.name_field import NameField
from main.base.fields.password_field import PasswordField
from main.base.fields.url_field import URLField
from main.base.fields.user_name_field import UserNameField
from test.fixture.base_test_fixture import row_with_all_fields


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.row_parse = lastpass_row.parse(row_with_all_fields)

    def test_shouldParseEnpassJSON(self):
        self.assertTrue(len(self.row_parse) > 0)

    def test_shouldParseURLField(self):
        expected_row_data = getColumnValueFromEnpassJSON(URLField.enpass_field_name, row_with_all_fields)
        self.assertEquals(expected_row_data, self.row_parse[URLField.lastpass_field_name])

    def test_shouldParseUserNameField(self):
        expected_row_data = getColumnValueFromEnpassJSON(UserNameField.enpass_field_name, row_with_all_fields)
        self.assertEquals(expected_row_data, self.row_parse[UserNameField.lastpass_field_name])

    def test_shouldParsePasswordField(self):
        expected_row_data = getColumnValueFromEnpassJSON(PasswordField.enpass_field_name, row_with_all_fields)
        self.assertEquals(expected_row_data, self.row_parse[PasswordField.lastpass_field_name])

    def test_shouldParseNameField(self):
        expected_row_data = row_with_all_fields[NameField.enpass_field_name]
        self.assertEquals(expected_row_data, self.row_parse[NameField.lastpass_field_name])

    def test_shouldParseFavouriteField(self):
        expected_row_data = row_with_all_fields[FavouriteField.enpass_field_name]
        self.assertEquals(expected_row_data, self.row_parse[FavouriteField.lastpass_field_name])

    def test_shouldParseExtraField(self):
        self.assertEquals(getExtraValues(row_with_all_fields), self.row_parse[ExtraField.lastpass_field_name])


def getColumnValueFromEnpassJSON(column_name, row):
    enpass_column = next(column for column in row["fields"] if column["label"] == column_name)
    return enpass_column["value"]


def getExtraValues(row):
    extra_value = ""
    for column in row["fields"]:
        if column["value"] != "" and column["label"] not in [URLField.enpass_field_name,
                                                             UserNameField.enpass_field_name,
                                                             PasswordField.enpass_field_name]:
            extra_value += f"{column['label']} : {column['value']}\n"
    return extra_value


if __name__ == '__main__':
    unittest.main()
