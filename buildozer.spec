[app]
title = Gauravi AI
package.name = gauraviai
package.domain = org.gauravi
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# यह सबसे जरूरी लाइन है जो आपके स्क्रीनशॉट में नहीं थी
requirements = python3, kivy

# कॉल, मैसेज और फोन कंट्रोल की ताकत
android.permissions = INTERNET, CALL_PHONE, READ_CONTACTS, RECORD_AUDIO

orientation = portrait
fullscreen = 1
android.arch = arm64-v8a
android.api = 31
