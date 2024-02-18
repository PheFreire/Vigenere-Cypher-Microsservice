from pydantic import BaseModel

class EncodeRequest(BaseModel):
    text: str
    key: str
    global_alphabet: str

    