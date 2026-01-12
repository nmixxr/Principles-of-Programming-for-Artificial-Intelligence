class Reflector:
    base_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, wiring):
        if len(wiring) != 26 or not wiring.isalpha():
            raise ValueError("Reflector wiring must be a 26-letter alphabet string.")
        self.wiring = wiring.upper()

    def encode(self, c):
        index = self.base_alphabet.index(c.upper())
        return self.wiring[index]
