class SerializerController:
    def to_lowercase(self, text: str) -> str:
        raise NotImplementedError()

    def repeat_to_match(self, text_to_repeat: str, match_text: str) -> str:
        raise NotImplementedError()
