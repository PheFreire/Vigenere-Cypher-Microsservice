from dataclasses import dataclass


@dataclass
class EncodeData:
    text: str
    key: str
    global_alphabet: str
