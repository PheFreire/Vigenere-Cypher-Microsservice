from domain.interfaces import (
    SerializerController,
    VigenereAlphabetFactory,
    VigenereEncodeController,
)
from domain.models import EncodeData


class Encode:
    def __init__(
        self,
        serializer_controller: SerializerController,
        vigenere_alphabet_factory: VigenereAlphabetFactory,
        vigenere_encode_controller: VigenereEncodeController,
    ):
        self.serializer_controller = serializer_controller
        self.vigenere_alphabet_factory = vigenere_alphabet_factory
        self.vigenere_encode_controller = vigenere_encode_controller

    def call(self, encode_data: EncodeData) -> str:
        text, key = (
            self.serializer_controller.to_lowercase(encode_data.text),
            self.serializer_controller.to_lowercase(encode_data.key),
        )

        key = self.serializer_controller.repeat_to_match(key, text)
        vigenere_alphabets = [
            self.vigenere_alphabet_factory.call(letter, encode_data.global_alphabet)
            for letter in encode_data.text
        ]

        return self.vigenere_encode_controller.encode(
            vigenere_alphabets,
            key,
            encode_data.global_alphabet,
        )
