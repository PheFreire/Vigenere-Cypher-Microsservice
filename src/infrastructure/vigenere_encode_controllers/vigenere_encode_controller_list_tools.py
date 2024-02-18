class VigenereEncodeControllerListTools:
    def encode(
        self, vigenere_alphabets: list[list[str]], key: str, global_alphabet: str
    ) -> str:
        key_idx = [global_alphabet.index(idx) for idx in key]
        encoded_array = [
            vigenere_alphabets[idx_l][key_idx[idx_l]]
            for idx_l in range(0, len(vigenere_alphabets))
        ]
        return "".join(encoded_array)
