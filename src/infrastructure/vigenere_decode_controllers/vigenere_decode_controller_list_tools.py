class VigenereDecodeControllerListTools:
    def decode(self, vigenere_key_alphabets: list[list[str]], encode_word: str, global_alphabet: str) -> str:
        encode_word_letters_idx_by_key_alphabet = [
            vigenere_key_alphabets[i].index(encode_word[i]) for i in range(0, len(encode_word))
        ]
        return "".join([global_alphabet[i] for i in encode_word_letters_idx_by_key_alphabet])