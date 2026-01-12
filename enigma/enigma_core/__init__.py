"""
Enigma Machine Package
"""
from .plugboard import PlugLead, Plugboard
from .reflector import Reflector
from .rotor import Rotor, rotor_from_name  # ← rotor_from_nameを追加
from .enigma_machine import EnigmaMachine

# ローターとリフレクターの定義
ROTORS = {
    'Beta': ('LEYJVCNIXWPBQMDRTAKZGFUHOS', None),
    'Gamma': ('FSOKANUERHMBTIYCWLQPZXVGJD', None),
    'I': ('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q'),
    'II': ('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E'),
    'III': ('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V'),
    'IV': ('ESOVPZJAYQUIRHXLNFTGKDCMWB', 'J'),
    'V': ('VZBRGITYUPSDNHLXAWMJQOFECK', 'Z'),
}

REFLECTORS = {
    'A': 'EJMZALYXVBWFCRQUONTSPIKHGD',
    'B': 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
    'C': 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
}

__all__ = ['PlugLead', 'Plugboard', 'Reflector', 'Rotor', 'EnigmaMachine', 'ROTORS', 'REFLECTORS', 'rotor_from_name']
