from main.base.fields.enpass_field import EnpassField
from test.fixture.base_test_fixture import row_with_url
from main.base.fields import url_field


def get_enpass_field_interpreter(enpass_field_data) -> EnpassField:
    for field in EnpassField.subclasses:
        if field.is_applicable(enpass_field_data):
            return field


def parse(input_enpass_json_row) -> {}:
    row_data = {}
    enpass_fields_data = input_enpass_json_row["fields"]
    for enpass_field_data in enpass_fields_data:
        enpass_field = get_enpass_field_interpreter(enpass_field_data)
        row_data[enpass_field.get_lastpass_field_name()] = enpass_field.get_parsed_value(enpass_field_data)

    return row_data


if __name__ == "__main__":
    print(parse(row_with_url))
