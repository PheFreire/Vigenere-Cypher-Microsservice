from pydantic import BaseModel

class DecodeRequest(BaseModel):
    encode_word: str
    key: str
    global_alphabet: str

    