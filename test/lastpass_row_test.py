import unittest

from main.base import LastPassRow
from main.base.fields.url_field import URLField
from main.base.fields.user_name_field import UserNameField
from test.fixture.base_test_fixture import row_with_all_fields


class BaseTest(unittest.TestCase):
    def test_shouldParseEnpassJSON(self):
        row_data = LastPassRow.parse(row_with_all_fields)
        self.assertTrue(len(row_data) > 0)

    def test_shouldParseURLField(self):
        row_data = LastPassRow.parse(row_with_all_fields)
        expected_row_data = getColumnValueFromEnpassJSON(URLField.enpass_field_name)
        self.assertEquals(expected_row_data, row_data[URLField.lastpass_field_name])

    def test_shouldParseUserNameField(self):
        row_data = LastPassRow.parse(row_with_all_fields)
        expected_row_data = getColumnValueFromEnpassJSON(UserNameField.enpass_field_name)
        self.assertEquals(expected_row_data, row_data[UserNameField.lastpass_field_name])


def getColumnValueFromEnpassJSON(column_name):
    column = next(column for column in row_with_all_fields["fields"] if column["label"] == column_name)
    return column["value"]


if __name__ == '__main__':
    unittest.main()
