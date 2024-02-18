from dataclasses import dataclass

@dataclass
class Injections:
    serializer_controller: str
    vigenere_alphabet_factory: str
    vigenere_decode_controller: str
    vigenere_encode_controller: str