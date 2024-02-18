from domain.interfaces import SerializerController


class SerializerControllerStringTools(SerializerController):
    def to_lowercase(self, text: str) -> str:
        return text.lower()

    def repeat_to_match(self, text_to_repeat: str, match_text: str) -> str:
        return text_to_repeat * ((len(match_text) // len(text_to_repeat)) + 1)
       