class EnigmaMachine:
    def __init__(self, rotors, reflector, plugboard):
        if len(rotors) not in [3, 4]:
            raise ValueError("EnigmaMachine requires 3 or 4 rotors.")
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard

    def get_rotor_positions(self):
        """現在のローター位置を返す"""
        return [rotor.get_display_letter() for rotor in self.rotors]

    def step_rotors(self):
        """ローターを進める（ダブルステッピング対応）"""
        if len(self.rotors) == 3:
            left, middle, right = self.rotors

            # Double-stepping: middleがnotchにいる場合
            if middle.at_notch():
                middle.step()
                left.step()
            # Rightがnotchにいる場合、middleを回転
            elif right.at_notch():
                middle.step()

            # 常にrightを回転
            right.step()

        elif len(self.rotors) == 4:
            # 4ローター構成では左端は静止（Greek wheel）
            # 実際に動くのは右3つのみ
            mid_left, mid_right, right = self.rotors[1], self.rotors[2], self.rotors[3]

            # Double-stepping: mid_rightがnotchにいる場合
            if mid_right.at_notch():
                mid_right.step()
                mid_left.step()
            # rightがnotchにいる場合
            elif right.at_notch():
                mid_right.step()

            # 常にrightを回転
            right.step()

    def encode(self, message):
        """メッセージ全体をエンコード"""
        if isinstance(message, str):
            # 文字列の場合は1文字ずつエンコード
            result = []
            for c in message:
                if c.isalpha():
                    result.append(self._encode_char(c.upper()))
                else:
                    result.append(c)
            return ''.join(result)
        else:
            # 単一文字の場合
            return self._encode_char(message.upper())

    def _encode_char(self, c):
        """1文字をエンコード（内部メソッド）"""
        # ローターを回転
        self.step_rotors()

        # プラグボード（入力）
        c = self.plugboard.encode(c)

        # ローター（右から左）
        for rotor in reversed(self.rotors):
            c = rotor.encode_forward(c)

        # リフレクター
        c = self.reflector.encode(c)

        # ローター（左から右）
        for rotor in self.rotors:
            c = rotor.encode_backward(c)

        # プラグボード（出力）
        c = self.plugboard.encode(c)

        return c
