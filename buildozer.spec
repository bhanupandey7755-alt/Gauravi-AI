[app]
title = Gauravi AI
package.name = gauraviai
package.domain = org.gauravi
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# ऐप का आइकॉन (Logo) सेट करने के लिए
icon.filename = %(source.dir)s/logo.png

# ऐप खुलते समय दिखने वाली फोटो
presplash.filename = %(source.dir)s/logo.png

# ज़रूरी लाइब्रेरीज़
requirements = python3, kivy

# परमिशन
android.permissions = INTERNET, CALL_PHONE, READ_CONTACTS, RECORD_AUDIO

orientation = portrait
fullscreen = 1
android.arch = arm64-v8a
android.api = 31
