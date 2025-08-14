[app]
title = Sabian Oracle 🎲🔮
package.name = sabianoracle
package.domain = org.example
source.main = main.py
source.include_exts = py, txt, png
source.include_patterns = 1158872025.txt, sabianoracle.png
requirements = python3,kivy
icon.filename = sabianoracle.png
android.minapi = 21
orientation = portrait
android.permissions = INTERNET
log_level = 1
android.exclude_exts = pyc,pyo
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
