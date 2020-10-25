from main.base.fields.enpass_field import EnpassField


class URLField(EnpassField):
    enpass_field_name = "Website"
    lastpass_field_name = "url"

    def __init__(self, value) -> None:
        self.field_value = value

    def __eq__(self, other) -> bool:
        return self.__class__ == other.__class__ and self.field_value == other.field_value

    @classmethod
    def get_lastpass_field_name(cls):
        return cls.lastpass_field_name

    @classmethod
    def get_parsed_value(cls, input_value) -> str:

        return input_value["value"]

    @classmethod
    def is_applicable(cls, input_value) -> bool:
        return input_value["label"] == cls.enpass_field_name
