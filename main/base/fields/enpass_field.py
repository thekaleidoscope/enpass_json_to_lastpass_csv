

class EnpassField:
    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    @classmethod
    def get_lastpass_field_name(cls) -> str:
        pass

    @classmethod
    def get_enpass_field_name(cls) -> str:
        pass

    @classmethod
    def get_parsed_value(cls, input_value) -> str:
        pass

    @classmethod
    def is_applicable(cls, input_value) -> bool:
        pass
