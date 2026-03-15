[app]
title = Gauravi AI
package.name = gauraviai
package.domain = org.gauravi
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

# नया वर्जन ताकि फ्रेश इंस्टॉल हो सके
version = 4.0

icon.filename = %(source.dir)s/logo.png
presplash.filename = %(source.dir)s/logo.png

# यहाँ 'android' जोड़ना बहुत ज़रूरी था
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
