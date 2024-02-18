from dataclasses import dataclass

@dataclass
class DecodeData:
    encode_word: str
    key: str 
    global_alphabet: str