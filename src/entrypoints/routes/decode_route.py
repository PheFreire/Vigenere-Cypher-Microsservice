from domain.models.decode_data import DecodeData
from domain.usecases.decode import Decode
from domain.usecases.get_injections_payload import GetInjectionsPayload
from fastapi import APIRouter
from entrypoints.basemodels.decode_request import DecodeRequest
from infrastructure.dependency_injection_bridges.dependency_injection_bridge_core import DependencyInjectionBridgeCore

from infrastructure.environment_variables_controllers.environment_variables_controller_json import EnvironmentVariablesControllerJson


decode_route = APIRouter(
    prefix="/decode",
    responses={404: {"description": "Not found"}},
)

@decode_route.post("/")
def decode(decode_request: DecodeRequest):
    environment_variables_controller = EnvironmentVariablesControllerJson()
    dependency_injection_bridge = DependencyInjectionBridgeCore()

    get_injections_payload = GetInjectionsPayload(
        environment_variables_controller,
        dependency_injection_bridge,
    )

    injections_payload = get_injections_payload.call()
    
    decode_data = DecodeData(
        decode_request.encode_word,
        decode_request.key,
        decode_request.global_alphabet
    )

    decode = Decode(
        injections_payload.serializer_controller(),
        injections_payload.vigenere_alphabet_factory(),
        injections_payload.vigenere_decode_controller(),
    )

    decode_word = decode.call(decode_data)
    return {"response": decode_word}