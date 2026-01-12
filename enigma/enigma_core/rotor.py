class Rotor:
    base_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, wiring, notch=None, position='A', ring_setting=1):
        self.wiring = wiring.upper()
        self.notch = notch.upper() if notch else None
        self.position = self.base_alphabet.index(position.upper())
        # Ring settingは1-26、内部では0-25として扱う
        if isinstance(ring_setting, int):
            self.ring_setting = ring_setting - 1
        else:
            self.ring_setting = 0

    def get_display_letter(self):
        return self.base_alphabet[self.position]

    def step(self):
        self.position = (self.position + 1) % 26

    def at_notch(self):
        if self.notch is None:
            return False
        # Ring settingを考慮したnotch判定
        notch_pos = self.base_alphabet.index(self.notch)
        adjusted_notch = (notch_pos - self.ring_setting) % 26
        return self.position == adjusted_notch

    def encode_forward(self, c):
        # Ring settingを考慮したエンコード
        shift = self.position - self.ring_setting
        index = (self.base_alphabet.index(c.upper()) + shift) % 26
        substituted = self.wiring[index]
        output_index = (self.base_alphabet.index(substituted) - shift) % 26
        return self.base_alphabet[output_index]

    def encode_backward(self, c):
        # Ring settingを考慮した逆エンコード
        shift = self.position - self.ring_setting
        index = (self.base_alphabet.index(c.upper()) + shift) % 26
        letter_at_index = self.base_alphabet[index]
        wiring_index = self.wiring.index(letter_at_index)
        output_index = (wiring_index - shift) % 26
        return self.base_alphabet[output_index]

    # テスト用メソッド
    def encode_right_to_left(self, c):
        return self.encode_forward(c)

    def encode_left_to_right(self, c):
        return self.encode_backward(c)


def rotor_from_name(name):
    """ローター名からRotorインスタンスを生成"""
    ROTORS = {
        'Beta': ('LEYJVCNIXWPBQMDRTAKZGFUHOS', None),
        'Gamma': ('FSOKANUERHMBTIYCWLQPZXVGJD', None),
        'I': ('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q'),
        'II': ('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E'),
        'III': ('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V'),
        'IV': ('ESOVPZJAYQUIRHXLNFTGKDCMWB', 'J'),
        'V': ('VZBRGITYUPSDNHLXAWMJQOFECK', 'Z'),
    }

    if name not in ROTORS:
        raise ValueError(f"Unknown rotor: {name}")
    wiring, notch = ROTORS[name]
    return Rotor(wiring=wiring, notch=notch, position='A')
