from dataclasses import dataclass
from domain.interfaces.decode.vigenere_decode_controller import VigenereDecodeController
from domain.interfaces.encode.vigenere_encode_controller import VigenereEncodeController
from domain.interfaces.serialize.serializer_controller import SerializerController
from domain.interfaces.vigenere_utils.vigenere_alphabet_factory import VigenereAlphabetFactory

@dataclass
class InjectionsPayload:
    serializer_controller: SerializerController
    vigenere_alphabet_factory: VigenereAlphabetFactory
    vigenere_decode_controller: VigenereDecodeController
    vigenere_encode_controller: VigenereEncodeController