from domain.interfaces import DependencyInjectionBridge
from domain.models import Injections, InjectionsPayload
from infrastructure.serializer_controllers.serializer_controller_string_tools import SerializerControllerStringTools
from infrastructure.vigenere_alphabet_factory.vigenere_alphabet_factory_string_tools import VigenereAlphabetFactoryStringTools
from infrastructure.vigenere_decode_controllers.vigenere_decode_controller_list_tools import VigenereDecodeControllerListTools
from infrastructure.vigenere_encode_controllers.vigenere_encode_controller_list_tools import VigenereEncodeControllerListTools


class DependencyInjectionBridgeCore(DependencyInjectionBridge):
    def __init__(self):
        self.adapters = {
            "serializer_controller_string_tools": SerializerControllerStringTools,
            "vigenere_alphabet_factory_string_tools": VigenereAlphabetFactoryStringTools,
            "vigenere_decode_controller_list_tools": VigenereDecodeControllerListTools,
            "vigenere_encode_controller_list_tools": VigenereEncodeControllerListTools,
        }

    def get_injections_payload(self, injections: Injections) -> InjectionsPayload:
        return InjectionsPayload(
            self.adapters[injections.serializer_controller],
            self.adapters[injections.vigenere_alphabet_factory],
            self.adapters[injections.vigenere_decode_controller],
            self.adapters[injections.vigenere_encode_controller],
        )
