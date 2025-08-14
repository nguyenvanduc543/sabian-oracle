# -*- coding: utf-8 -*-
import random
import re
import tkinter as tk
from tkinter import scrolledtext

def get_sabian_symbol(dice1, dice2):
    try:
        with open("1158872025.txt", "r", encoding="utf-8") as file:
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

def roll_dice():
    dice1 = random.randint(1, 12)
    dice2 = random.randint(1, 30)
    result_text = f"🎲 Kết quả xúc xắc: {dice1}-{dice2}\n🔮 Dự đoán Sabian:\n\n"
    result_text += get_sabian_symbol(dice1, dice2)
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, result_text)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Sabian Oracle 🎲🔮")
root.geometry("600x500")

# Nút bấm xúc xắc
roll_button = tk.Button(root, text="🎲 Lắc xúc xắc", font=("Arial", 14), command=roll_dice)
roll_button.pack(pady=10)

# Khung hiển thị kết quả
output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
output_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
