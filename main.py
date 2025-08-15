# -*- coding: utf-8 -*-
import random
import re
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput


def get_sabian_symbol(dice1, dice2):
    try:
        # Lấy đường dẫn file kèm theo APK
        base_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_path, "1158872025.txt")

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        symbol_key = f"{dice1}-{dice2}"
        pattern = rf"{symbol_key}\:.*?(\n\d+\-\d+\:|\Z)"
        match = re.search(pattern, content, re.DOTALL)

        if match:
            symbol_text = match.group(0)
            symbol_text = re.sub(r"\n\d+\-\d+\:.*$", "", symbol_text, flags=re.DOTALL)
            return symbol_text.strip()
        else:
            return f"❌ Không tìm thấy Sabian Symbol cho {symbol_key}"
    except FileNotFoundError:
        return "⚠️ Lỗi: Không tìm thấy file '1158872025.txt'."
    except UnicodeDecodeError:
        return "⚠️ Lỗi: Không thể đọc file, hãy lưu file ở dạng UTF-8."
    except Exception as e:
        return f"⚠️ Lỗi: {str(e)}"


class SabianLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # Nút lắc xúc xắc
        self.roll_button = Button(
            text="🎲 Lắc xúc xắc",
            font_size=22,
            size_hint=(1, None),
            height=60
        )
        self.roll_button.bind(on_release=self.roll_dice)
        self.add_widget(self.roll_button)

        # Khung scroll hiển thị kết quả
        self.scroll = ScrollView(size_hint=(1, 1))
        self.output_box = TextInput(
            text="🔮 Chào mừng đến với Sabian Oracle!",
            readonly=True,
            font_size=16,
            size_hint_y=None,
            height=800,
        )
        self.output_box.bind(minimum_height=self.output_box.setter('height'))
        self.scroll.add_widget(self.output_box)
        self.add_widget(self.scroll)

    def roll_dice(self, instance):
        dice1 = random.randint(1, 12)
        dice2 = random.randint(1, 30)
        result_text = f"🎲 Kết quả xúc xắc: {dice1}-{dice2}\n\n🔮 Dự đoán Sabian:\n\n"
        result_text += get_sabian_symbol(dice1, dice2)
        self.output_box.text = result_text


class SabianOracleApp(App):
    def build(self):
        self.title = "Sabian Oracle 🎲🔮"
        return SabianLayout()


if __name__ == "__main__":
    SabianOracleApp().run()
