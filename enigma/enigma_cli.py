import sys
import string
from enigma_core.rotor import Rotor
from enigma_core.reflector import Reflector
from enigma_core.plugboard import Plugboard, PlugLead
from enigma_core.enigma_machine import EnigmaMachine
from enigma_core import ROTORS as ALL_ROTORS, REFLECTORS as ALL_REFLECTORS


def get_number_of_rotors():
    while True:
        choice = input("使用するローターの数を選択してください (3 or 4): ")
        if choice in ['3', '4']:
            return int(choice)
        else:
            print("無効な入力です。3 または 4 を入力してください。")


def get_rotor_selection(available_rotors, position_name):
    while True:
        print(f"利用可能なローター: {', '.join(available_rotors)}")
        choice = input(f"<{position_name}> の位置に使用するローターを選択してください: ")
        if choice in available_rotors:
            return choice
        else:
            print(f"無効な選択です: '{choice}'。利用可能なローターから選んでください。")


def get_reflector_selection():
    while True:
        print(f"利用可能なリフレクター: {', '.join(ALL_REFLECTORS.keys())}")
        choice = input("使用するリフレクターを選択してください (A, B, C): ").upper()
        if choice in ALL_REFLECTORS:
            return choice
        else:
            print(f"無効な選択です: '{choice}'。A, B, C のいずれかを選んでください。")


def get_rotor_positions(num_rotors):
    positions = []
    position_labels = ["左端", "中左", "中右", "右端"] if num_rotors == 4 else ["左", "中央", "右"]
    for name in position_labels:
        while True:
            pos = input(f"<{name}> ローターの初期位置をアルファベット一文字で入力してください (A-Z): ").upper()
            if len(pos) == 1 and pos in string.ascii_uppercase:
                positions.append(pos)
                break
            else:
                print("無効な入力です。AからZまでの一文字を入力してください。")
    return positions


def get_plugboard_settings():
    while True:
        print("プラグボードの設定を入力してください (例: AB CD EF)。")
        print("最大10ペアまで設定可能です。設定しない場合は、何も入力せずEnterキーを押してください。")
        settings_str = input("> ").upper()

        if not settings_str:
            return []

        pairs = settings_str.split()

        if len(pairs) > 10:
            print("エラー: プラグは10ペアまでしか設定できません。")
            continue

        all_chars = "".join(pairs)
        if len(all_chars) != len(set(all_chars)):
            print("エラー: 同じ文字を複数のペアで使用することはできません。")
            continue

        valid = True
        for pair in pairs:
            if len(pair) != 2 or not pair.isalpha():
                print(f"エラー: '{pair}' は不正なペアです。ペアはアルファベット2文字で指定してください。")
                valid = False
                break

        if valid:
            return pairs


def print_separator():
    print("-" * 100)


def main():
    try:
        print("Enigmaシミュレータ 起動")
        print_separator()
        print("設定を開始します。")
        print_separator()

        num_rotors = get_number_of_rotors()
        print(f"\n{num_rotors}個のローター構成で動作します。")
        print_separator()

        available_rotors = list(ALL_ROTORS.keys())
        chosen_rotor_names = []
        position_labels = ["左端", "中左", "中右", "右端"] if num_rotors == 4 else ["左", "中央", "右"]

        for i in range(num_rotors):
            choice = get_rotor_selection(available_rotors, position_labels[i])
            chosen_rotor_names.append(choice)
            available_rotors.remove(choice)

        print(f"\n選択されたローター: {chosen_rotor_names}")
        print_separator()

        reflector_choice = get_reflector_selection()
        print(f"\n選択されたリフレクター: {reflector_choice}")
        print_separator()

        rotor_positions = get_rotor_positions(num_rotors)
        print(f"\nローターの初期位置: {rotor_positions}")
        print_separator()

        machine_rotors = []
        for i in range(num_rotors):
            name = chosen_rotor_names[i]
            wiring, notch = ALL_ROTORS[name]
            rotor = Rotor(wiring=wiring, notch=notch, position=rotor_positions[i])
            machine_rotors.append(rotor)

        plugboard_pairs = get_plugboard_settings()
        plugboard = Plugboard(plugboard_pairs)
        print_separator()

        reflector = Reflector(ALL_REFLECTORS[reflector_choice])

        machine = EnigmaMachine(
            rotors=machine_rotors,
            reflector=reflector,
            plugboard=plugboard
        )

        print("設定が完了しました。")
        print_separator()

        while True:
            print("暗号化したい平文、または復号化したい暗号文を入力してください。")
            print("システムを終了するには 'exit' と入力するか、Ctrl+C を押してください。")
            input_text = input("平文(または暗号文) > ")

            if input_text.lower() == 'exit':
                print_separator()
                print("Enigmaシミュレータを終了します。")
                break

            cleaned_text = "".join(filter(str.isalpha, input_text)).upper()
            encrypted = []
            for char in cleaned_text:
                encrypted.append(machine.encode(char))

            print("暗号文(または平文) > " + "".join(encrypted))
            print_separator()

    except KeyboardInterrupt:
        print("\n\nCtrl+Cが検出されました。Enigmaシミュレータを終了します。")
        sys.exit(0)


if __name__ == "__main__":
    main()
