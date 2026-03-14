[app]
title = Gauravi AI
package.name = gauraviai
package.domain = org.gauravi
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

# नया वर्जन ताकि फ्रेश इंस्टॉल हो
version = 3.0

icon.filename = %(source.dir)s/logo.png
presplash.filename = %(source.dir)s/logo.png

requirements = python3, kivy, pyjnius, android

android.permissions = INTERNET, RECORD_AUDIO, MODIFY_AUDIO_SETTINGS
orientation = portrait
fullscreen = 1
android.arch = arm64-v8a
android.api = 31
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1
