from domain.usecases.encode import Encode
from domain.usecases.get_injections_payload import GetInjectionsPayload
from entrypoints.basemodels import EncodeRequest
from fastapi import APIRouter

from domain.models import EncodeData
from infrastructure.dependency_injection_bridges.dependency_injection_bridge_core import DependencyInjectionBridgeCore

from infrastructure.environment_variables_controllers.environment_variables_controller_json import EnvironmentVariablesControllerJson

from infrastructure.serializer_controllers.serializer_controller_string_tools import SerializerControllerStringTools
from infrastructure.vigenere_alphabet_factory.vigenere_alphabet_factory_string_tools import VigenereAlphabetFactoryStringTools
from infrastructure.vigenere_encode_controllers.vigenere_encode_controller_list_tools import VigenereEncodeControllerListTools


encode_route = APIRouter(
    prefix="/encode",
    responses={404: {"description": "Not found"}},
)

@encode_route.post("/")
def encode(encode_request: EncodeRequest):
    environment_variables_controller = EnvironmentVariablesControllerJson()
    dependency_injection_bridge = DependencyInjectionBridgeCore()

    get_injections_payload = GetInjectionsPayload(
        environment_variables_controller,
        dependency_injection_bridge,
    )

    injections_payload = get_injections_payload.call()
    
    encode_data = EncodeData(
        encode_request.text,
        encode_request.key,
        encode_request.global_alphabet
    )

    encode = Encode(
        injections_payload.serializer_controller(),
        injections_payload.vigenere_alphabet_factory(),
        injections_payload.vigenere_encode_controller(),
    )

    encode_word = encode.call(encode_data)
    return {"response": encode_word}