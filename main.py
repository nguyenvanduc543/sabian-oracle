import random
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader

# --- Load Sabian Symbols ---
def load_sabian_symbols():
    symbols = {}
    file_path = os.path.join(os.path.dirname(__file__), "1158872025.txt")
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and ":" in line:
                key, value = line.split(":", 1)
                symbols[key.strip()] = value.strip()
    return symbols

SABIAN_SYMBOLS = load_sabian_symbols()

def get_sabian_symbol(dice1, dice2):
    key = f"{dice1}-{dice2}"
    return SABIAN_SYMBOLS.get(key, "Không tìm thấy biểu tượng cho kết quả này.")

# --- Layout Class ---
class SabianLayout(BoxLayout):
    def roll_dice(self):
        # Play sound
        base_path = os.path.dirname(os.path.abspath(__file__))
        sound_path = os.path.join(base_path, "assets", "dice_roll.mp3")
        sound = SoundLoader.load(sound_path)
        if sound:
            sound.play()

        # Dice roll
        dice1 = random.randint(1, 12)
        dice2 = random.randint(1, 30)
        result_text = f"🎲 Kết quả xúc xắc: {dice1}-{dice2}\n\n🔮 Dự đoán Sabian:\n\n"
        result_text += get_sabian_symbol(dice1, dice2)
        self.ids.output_box.text = result_text

# --- Main App ---
class SabianApp(App):
    def build(self):
        return SabianLayout()

if __name__ == "__main__":
    SabianApp().run()
