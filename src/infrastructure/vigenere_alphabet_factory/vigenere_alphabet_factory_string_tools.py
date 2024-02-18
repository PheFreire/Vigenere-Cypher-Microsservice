from domain.interfaces import VigenereAlphabetFactory


class VigenereAlphabetFactoryStringTools(VigenereAlphabetFactory):
    def call(self, letter: str, global_alphabet: str) -> list[str]:
        start = global_alphabet.index(letter)
        normal_alphabet = [
            global_alphabet[idx] for idx in range(start, len(global_alphabet))
        ]
        normal_alphabet.extend([global_alphabet[idx] for idx in range(0, start)])
        return normal_alphabet
