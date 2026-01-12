"""
Jupyter Notebook用のショートカットモジュール
"""
from enigma.enigma_core import (
    Rotor,
    Reflector,
    Plugboard,
    PlugLead,
    EnigmaMachine,
    ROTORS,
    REFLECTORS,
    rotor_from_name
)

__all__ = [
    'Rotor', 'Reflector', 'Plugboard', 'PlugLead', 'EnigmaMachine',
    'ROTORS', 'REFLECTORS', 'rotor_from_name'
]

# References
#
# Sekiguchi, BTM. (2025, September 5). Enigma Simulator CLI Implementation [EnigmaシミュレータCLI作ってみました]. Qiita.
#     https://qiita.com/btm-sekiguchi/items/97bcc78f13ba4ce385dd
#
# Tamagaki. (n.d.). Enigma Cipher [エニグマ Enigma 暗号 cipher]. Tamagaki Mathematics.
# https://tamagaki.com/math/Enigma.html
