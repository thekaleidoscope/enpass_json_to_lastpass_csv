from main.base.constants.enpass_constants import VALUE, LABEL
from main.base.fields.enpass_field import EnpassField
from main.base.fields.password_field import PasswordField
from main.base.fields.url_field import URLField
from main.base.fields.user_name_field import UserNameField


class ExtraField(EnpassField):
    enpass_field_name = ""
    lastpass_field_name = "extra"

    def __init__(self, value) -> None:
        self.field_value = value

    def __eq__(self, other) -> bool:
        return self.__class__ == other.__class__ and self.field_value == other.field_value

    @classmethod
    def get_lastpass_field_name(cls):
        return cls.lastpass_field_name

    @classmethod
    def get_enpass_field_name(cls) -> str:
        return cls.enpass_field_name

    @classmethod
    def get_parsed_value(cls, input_value) -> str:
        return f"{input_value[LABEL]} : {input_value[VALUE]}\n"

    @classmethod
    def is_applicable(cls, input_value) -> bool:
        return input_value[VALUE] != "" and input_value[LABEL] not in [URLField.enpass_field_name,
                                                                       UserNameField.enpass_field_name,
                                                                       PasswordField.enpass_field_name]
