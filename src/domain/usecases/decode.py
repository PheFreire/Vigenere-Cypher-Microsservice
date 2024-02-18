from domain.interfaces import (
    SerializerController,
    VigenereAlphabetFactory,
    VigenereDecodeController
)

from domain.models import DecodeData


class Decode:
    def __init__(
        self,
        serializer_controller: SerializerController,
        vigenere_alphabet_factory: VigenereAlphabetFactory,
        vigenere_decode_controller: VigenereDecodeController,
    ):
        self.serializer_controller = serializer_controller
        self.vigenere_alphabet_factory = vigenere_alphabet_factory
        self.vigenere_decode_controller = vigenere_decode_controller

    def call(self, decode_data: DecodeData):
        encode_word, key = (
            self.serializer_controller.to_lowercase(decode_data.encode_word),
            self.serializer_controller.to_lowercase(decode_data.key),
        )

        key = self.serializer_controller.repeat_to_match(key, encode_word)
        vigenere_key_alphabets = [
            self.vigenere_alphabet_factory.call(letter, decode_data.global_alphabet)
            for letter in key
        ]

        return self.vigenere_decode_controller.decode(
            vigenere_key_alphabets,
            encode_word,
            decode_data.global_alphabet,
        )