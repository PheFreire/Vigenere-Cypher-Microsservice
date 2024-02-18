from fastapi import FastAPI
from entrypoints.routes import *

# origins = [
#     "http://localhost:3000",
#     "http://192.168.18.43:3000",
#     os.getenv("FRONTEND_API_HOST")
# ]
# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app = FastAPI()

app.include_router(encode_route)
app.include_router(decode_route)

# key = "pa"
# global_alphabet = "abcdefghijklmnopqrstuvwxyz" 


# decode_data = DecodeData(
#     encode_word,
#     key,
#     global_alphabet,
# ) 

# decode = Decode(
#     SerializerControllerStringTools(),
#     VigenereAlphabetFactoryStringTools(),
#     VigenereDecodeControllerListTools(),
# )

# decode_res = decode.call(decode_data)

