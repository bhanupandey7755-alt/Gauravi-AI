[app]
title = Gauravi AI
package.name = gauraviai
package.domain = org.gauravi
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

# इसे 6.0 कर दें, ताकि फोन नया अपडेट मान ले
version = 6.0

icon.filename = %(source.dir)s/logo.png
presplash.filename = %(source.dir)s/logo.png

# इसमें android, pyjnius होना ज़रूरी है
requirements = python3, kivy, android, pyjnius

android.permissions = INTERNET, RECORD_AUDIO, MODIFY_AUDIO_SETTINGS
orientation = portrait
fullscreen = 1
android.arch = arm64-v8a
android.api = 31
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1
