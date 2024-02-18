from domain.interfaces import EnvironmentVariablesController
from domain.models import Injections

import json
import os

class EnvironmentVariablesControllerJson(EnvironmentVariablesController):
    def get_injections(self) -> Injections:
        env_path = os.getenv("ENVIRONMENT_VARIABLES_PATH")
        env_file = open(env_path)
        env = json.load(env_file)

        return Injections(
            env["serializer_controller"],
            env["vigenere_alphabet_factory"],
            env["vigenere_decode_controller"],
            env["vigenere_encode_controller"],
        )
        